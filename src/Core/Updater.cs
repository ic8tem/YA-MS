// YA-MS - aggiornamento automatico dalle Release di GitHub e controllo dei file del programma
//  - si legge l'ultima Release (api.github.com/repos/ic8tem/YA-MS/releases/latest) e, se la versione e' piu' nuova,
//    si scarica il pacchetto portatile adatto al sistema (zip per Windows, tar.gz per Linux e Raspberry Pi, app.zip per Mac);
//  - i file del programma si sostituiscono sul posto (su Windows quelli in uso si rinominano in *.old-aggiornamento e si
//    cancellano al riavvio successivo; su Mac si sostituisce l'intero YA-MS.app, per non rompere la firma);
//  - la cartella data resta: i file nuovi si aggiungono, quelli del programma che cambiano si copiano prima in
//    data/backup/<versione vecchia>; i file dell'utente (impostazioni, copie dei radar, ADIF) non si toccano;
//  - l'elenco dei file del programma (data e doc) e' scritto nell'eseguibile durante la compilazione (manifesto.txt):
//    all'avvio si controlla che ci siano tutti e quelli mancanti si possono riscaricare da GitHub.
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Formats.Tar;
using System.Globalization;
using System.IO;
using System.IO.Compression;
using System.Net;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text.Json;

namespace YAMS
{
    public class ReleaseInfo
    {
        public string Tag, VersionText, Notes, PageUrl, AssetName, AssetUrl;
        public long AssetSize;
        public Version Ver;
    }

    public static class Updater
    {
        public const string Repo = "ic8tem/YA-MS";
        public const string LatestApi = "https://api.github.com/repos/" + Repo + "/releases/latest";
        public const string ReleasesPage = "https://github.com/" + Repo + "/releases/latest";
        const string OldSuffix = ".old-aggiornamento";

        public static Version Current { get { return ParseVersion(AppPaths.Version); } }

        public static Version ParseVersion(string s)
        {
            s = (s ?? "").Trim().TrimStart('v', 'V');
            int cut = s.IndexOfAny(new[] { '-', '+', ' ' });
            if (cut > 0) s = s.Substring(0, cut);
            Version v;
            return Version.TryParse(s, out v) ? v : new Version(0, 0);
        }

        static HttpWebRequest Req(string url)
        {
            HttpWebRequest r = (HttpWebRequest)WebRequest.Create(url);
            r.UserAgent = "YA-MS/" + AppPaths.Version + " (+https://github.com/" + Repo + ")";
            r.Timeout = 30000; r.ReadWriteTimeout = 60000;
            r.AllowAutoRedirect = true;
            return r;
        }

        // suffisso del pacchetto portatile adatto a questo sistema
        public static string AssetSuffix()
        {
            Architecture a = RuntimeInformation.ProcessArchitecture;
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
                return a == Architecture.X86 ? "-windows-x86-portatile.zip"
                     : a == Architecture.Arm64 ? "-windows-arm64-portatile.zip" : "-windows-x64-portatile.zip";
            if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
                return a == Architecture.Arm64 ? "-mac-apple-silicon-app.zip" : "-mac-intel-app.zip";
            // Alpine e altri Linux con musl: il programma e' stato compilato per linux-musl-*
            if (RuntimeInformation.RuntimeIdentifier.Contains("musl"))
                return a == Architecture.Arm64 ? "-alpine-arm64.tar.gz" : "-alpine-x64.tar.gz";
            if (a == Architecture.Arm64) return "-raspberry-pi-64bit.tar.gz";
            if (a == Architecture.Arm) return "-raspberry-pi-32bit.tar.gz";
            return "-linux-x64.tar.gz";
        }

        // legge l'ultima Release; lancia un'eccezione con il messaggio da mostrare se non riesce
        public static ReleaseInfo GetLatest()
        {
            string json;
            HttpWebRequest r = Req(LatestApi);
            r.Accept = "application/vnd.github+json";
            using (HttpWebResponse resp = (HttpWebResponse)r.GetResponse())
            using (StreamReader sr = new StreamReader(resp.GetResponseStream())) json = sr.ReadToEnd();
            using (JsonDocument doc = JsonDocument.Parse(json))
            {
                JsonElement root = doc.RootElement;
                ReleaseInfo ri = new ReleaseInfo();
                ri.Tag = root.GetProperty("tag_name").GetString();
                ri.Ver = ParseVersion(ri.Tag);
                ri.VersionText = ri.Ver.ToString(3);
                JsonElement e;
                ri.Notes = root.TryGetProperty("body", out e) && e.ValueKind == JsonValueKind.String ? e.GetString() : "";
                ri.PageUrl = root.TryGetProperty("html_url", out e) && e.ValueKind == JsonValueKind.String ? e.GetString() : ReleasesPage;
                string suf = AssetSuffix();
                if (root.TryGetProperty("assets", out e))
                    foreach (JsonElement a in e.EnumerateArray())
                    {
                        string n = a.GetProperty("name").GetString() ?? "";
                        if (!n.EndsWith(suf, StringComparison.OrdinalIgnoreCase)) continue;
                        ri.AssetName = n;
                        ri.AssetUrl = a.GetProperty("browser_download_url").GetString();
                        ri.AssetSize = a.TryGetProperty("size", out JsonElement sz) ? sz.GetInt64() : 0;
                        break;
                    }
                return ri;
            }
        }

        public static string StageDir { get { return Path.Combine(AppPaths.DataDir, "aggiornamento"); } }

        // scarica il pacchetto (progress: 0..100) e lo estrae; restituisce la cartella estratta
        public static string DownloadAndExtract(ReleaseInfo ri, Action<int> progress)
        {
            string dir = StageDir;
            if (Directory.Exists(dir)) Directory.Delete(dir, true);
            Directory.CreateDirectory(dir);
            string file = Path.Combine(dir, ri.AssetName);
            using (HttpWebResponse resp = (HttpWebResponse)Req(ri.AssetUrl).GetResponse())
            using (Stream rs = resp.GetResponseStream())
            using (FileStream fs = File.Create(file))
            {
                long total = resp.ContentLength > 0 ? resp.ContentLength : ri.AssetSize, got = 0;
                byte[] buf = new byte[81920]; int n, last = -1;
                while ((n = rs.Read(buf, 0, buf.Length)) > 0)
                {
                    fs.Write(buf, 0, n); got += n;
                    int p = total > 0 ? (int)(got * 100 / total) : -1;
                    if (p != last && progress != null) { last = p; progress(p); }
                }
            }
            string outDir = Path.Combine(dir, "nuova");
            Directory.CreateDirectory(outDir);
            if (file.EndsWith(".zip", StringComparison.OrdinalIgnoreCase)) ZipFile.ExtractToDirectory(file, outDir, true);
            else
                using (FileStream fs = File.OpenRead(file))
                using (GZipStream gz = new GZipStream(fs, CompressionMode.Decompress))
                    TarFile.ExtractToDirectory(gz, outDir, true);
            return outDir;
        }

        static bool IsWin { get { return RuntimeInformation.IsOSPlatform(OSPlatform.Windows); } }
        static bool IsMac { get { return RuntimeInformation.IsOSPlatform(OSPlatform.OSX); } }

        // YA-MS.app in esecuzione (solo Mac), altrimenti null
        public static string RunningBundle()
        {
            string b = AppContext.BaseDirectory;
            int i = b.IndexOf(".app" + Path.DirectorySeparatorChar + "Contents", StringComparison.OrdinalIgnoreCase);
            return i > 0 ? b.Substring(0, i + 4) : null;
        }

        static string FindRoot(string dir, string marker)
        {
            if (File.Exists(Path.Combine(dir, marker)) || Directory.Exists(Path.Combine(dir, marker))) return dir;
            foreach (string d in Directory.GetDirectories(dir))
                if (File.Exists(Path.Combine(d, marker)) || Directory.Exists(Path.Combine(d, marker))) return d;
            return null;
        }

        static void MakeExecutable(string f)
        {
            if (IsWin || !File.Exists(f)) return;
            try
            {
                File.SetUnixFileMode(f, UnixFileMode.UserRead | UnixFileMode.UserWrite | UnixFileMode.UserExecute | UnixFileMode.GroupRead |
                    UnixFileMode.GroupExecute | UnixFileMode.OtherRead | UnixFileMode.OtherExecute);
            }
            catch { }
        }

        // sostituisce un file anche se e' in uso (Windows: rinomina il vecchio; Linux e Mac: cancella e ricopia)
        static void Replace(string src, string dst)
        {
            Directory.CreateDirectory(Path.GetDirectoryName(dst));
            if (!File.Exists(dst)) { File.Copy(src, dst); return; }
            if (IsWin)
            {
                try { File.Copy(src, dst, true); }
                catch (Exception)
                {
                    string old = dst + OldSuffix;
                    if (File.Exists(old)) File.Delete(old);
                    File.Move(dst, old);
                    File.Copy(src, dst);
                }
            }
            else { File.Delete(dst); File.Copy(src, dst); }
        }

        static bool SameContent(string a, string b)
        {
            FileInfo fa = new FileInfo(a), fb = new FileInfo(b);
            if (fa.Length != fb.Length) return false;
            using (FileStream sa = fa.OpenRead())
            using (FileStream sb = fb.OpenRead())
            {
                byte[] ba = new byte[65536], bb = new byte[65536];
                int na;
                while ((na = sa.Read(ba, 0, ba.Length)) > 0)
                {
                    int nb = 0;
                    while (nb < na) { int r = sb.Read(bb, nb, na - nb); if (r <= 0) return false; nb += r; }
                    for (int i = 0; i < na; i++) if (ba[i] != bb[i]) return false;
                }
            }
            return true;
        }

        // cartella data del pacchetto nuovo -> cartella data del programma; restituisce quanti file del programma
        // modificati sono stati copiati in data/backup prima di sostituirli
        static int MergeData(string srcData, string backupTag)
        {
            int saved = 0;
            if (!Directory.Exists(srcData)) return 0;
            string dst = AppPaths.DataDir, bak = Path.Combine(dst, "backup", backupTag);
            foreach (string f in Directory.GetFiles(srcData, "*", SearchOption.AllDirectories))
            {
                string rel = Path.GetRelativePath(srcData, f);
                string d = Path.Combine(dst, rel);
                if (File.Exists(d))
                {
                    if (SameContent(f, d)) continue;
                    string b = Path.Combine(bak, rel);
                    Directory.CreateDirectory(Path.GetDirectoryName(b));
                    File.Copy(d, b, true);
                    saved++;
                }
                Directory.CreateDirectory(Path.GetDirectoryName(d));
                File.Copy(f, d, true);
            }
            return saved;
        }

        // installa la versione estratta in outDir; restituisce il comando per riavviare il programma
        public static ProcessStartInfo Install(string outDir, out int backedUp)
        {
            string tag = "v" + AppPaths.Version;
            string bundle = RunningBundle();
            if (IsMac && bundle != null)
            {
                string newApp = FindRoot(outDir, "YA-MS.app");
                if (newApp == null) throw new IOException(Lang.T("YA-MS.app non trovato nel pacchetto"));
                newApp = Path.Combine(newApp, "YA-MS.app");
                foreach (string f in Directory.GetFiles(Path.Combine(newApp, "Contents", "MacOS"))) if (Path.GetExtension(f) == "") MakeExecutable(f);
                backedUp = MergeData(Path.Combine(newApp, "Contents", "Resources", "data"), tag);
                string old = bundle + OldSuffix;
                if (Directory.Exists(old)) Directory.Delete(old, true);
                Directory.Move(bundle, old);
                try { Directory.Move(newApp, bundle); }
                catch { CopyDir(newApp, bundle); }
                ProcessStartInfo p = new ProcessStartInfo("open") { UseShellExecute = false };
                p.ArgumentList.Add("-n"); p.ArgumentList.Add(bundle);
                return p;
            }
            string exe = IsWin ? "YA-MS.exe" : "YA-MS";
            string root = FindRoot(outDir, exe);
            if (root == null) throw new IOException(Lang.F("{0} non trovato nel pacchetto", exe));
            string target = AppContext.BaseDirectory;
            string srcData = Path.Combine(root, "data");
            foreach (string f in Directory.GetFiles(root, "*", SearchOption.AllDirectories))
            {
                string rel = Path.GetRelativePath(root, f);
                if (rel.StartsWith("data" + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase)) continue;
                Replace(f, Path.Combine(target, rel));
            }
            backedUp = MergeData(srcData, tag);
            string exePath = Path.Combine(target, exe);
            MakeExecutable(exePath);
            return new ProcessStartInfo(exePath) { UseShellExecute = false, WorkingDirectory = target };
        }

        static void CopyDir(string src, string dst)
        {
            foreach (string f in Directory.GetFiles(src, "*", SearchOption.AllDirectories))
            {
                string d = Path.Combine(dst, Path.GetRelativePath(src, f));
                Directory.CreateDirectory(Path.GetDirectoryName(d));
                File.Copy(f, d, true);
            }
        }

        // all'avvio: toglie i resti dell'aggiornamento precedente (file *.old-aggiornamento, YA-MS.app vecchio, pacchetto scaricato)
        public static void Cleanup()
        {
            try
            {
                string b = RunningBundle();
                if (b != null && Directory.Exists(b + OldSuffix)) Directory.Delete(b + OldSuffix, true);
                string baseDir = AppContext.BaseDirectory;
                foreach (string f in Directory.GetFiles(baseDir, "*" + OldSuffix, SearchOption.AllDirectories))
                    try { File.Delete(f); } catch { }
                if (Directory.Exists(StageDir)) Directory.Delete(StageDir, true);
            }
            catch { }
        }

        // ---- file del programma mancanti
        // elenco scritto nell'eseguibile durante la compilazione (percorsi relativi: data/..., doc/...)
        public static List<string> Manifest()
        {
            List<string> l = new List<string>();
            try
            {
                using (Stream s = Assembly.GetExecutingAssembly().GetManifestResourceStream("manifesto.txt"))
                {
                    if (s == null) return l;
                    using (StreamReader r = new StreamReader(s))
                    {
                        string line;
                        while ((line = r.ReadLine()) != null)
                        {
                            line = line.Trim().Replace('\\', '/');
                            if (line.Length > 0) l.Add(line);
                        }
                    }
                }
            }
            catch { }
            return l;
        }

        static string LocalPathFor(string rel)
        {
            string r = rel.Replace('/', Path.DirectorySeparatorChar);
            if (rel.StartsWith("data/")) return Path.Combine(AppPaths.DataDir, r.Substring(5));
            string a = Path.Combine(AppPaths.AppDir, r);
            if (File.Exists(a)) return a;
            string b = Path.Combine(AppContext.BaseDirectory, r);   // su Mac i documenti stanno dentro YA-MS.app
            return File.Exists(b) ? b : a;
        }

        public static List<string> MissingFiles()
        {
            List<string> miss = new List<string>();
            foreach (string rel in Manifest())
                if (!File.Exists(LocalPathFor(rel))) miss.Add(rel);
            return miss;
        }

        // riscarica i file mancanti dal tag della versione in uso (se non c'e', dal ramo main); restituisce quanti sono arrivati
        public static int DownloadMissing(List<string> files, Action<int, int> progress)
        {
            int ok = 0, i = 0;
            foreach (string rel in files)
            {
                i++;
                if (progress != null) progress(i, files.Count);
                string dst = LocalPathFor(rel);
                foreach (string refName in new[] { "v" + AppPaths.Version, "main" })
                {
                    try
                    {
                        string url = "https://raw.githubusercontent.com/" + Repo + "/" + refName + "/" +
                                     string.Join("/", Array.ConvertAll(rel.Split('/'), Uri.EscapeDataString));
                        Directory.CreateDirectory(Path.GetDirectoryName(dst));
                        string tmp = dst + ".tmp";
                        using (HttpWebResponse resp = (HttpWebResponse)Req(url).GetResponse())
                        using (Stream rs = resp.GetResponseStream())
                        using (FileStream fs = File.Create(tmp)) rs.CopyTo(fs);
                        if (File.Exists(dst)) File.Delete(dst);
                        File.Move(tmp, dst);
                        ok++;
                        break;
                    }
                    catch { try { if (File.Exists(dst + ".tmp")) File.Delete(dst + ".tmp"); } catch { } }
                }
            }
            return ok;
        }
    }
}
