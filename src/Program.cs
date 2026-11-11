// YA-MS - avvio (Windows, Linux, Mac)
using System;
using System.IO;
using Avalonia;

namespace YAMS
{
    internal static class Program
    {
        public static string ScreenshotDir, ScreenshotDx, ScreenshotLang;
        public static string ScreenshotTheme;     // --tema <chiave>: schema di colori per le fotografie (chiaro, scuro, nero, pastello-..., scia)
        public static double ScreenshotHours;
        public static double ScreenshotFontPct;   // --carattere N: scala del carattere in % per le fotografie (0 = invariata)

        [STAThread]
        public static void Main(string[] args)
        {
            for (int i = 0; i < args.Length - 1; i++)
            {
                if (args[i] == "--screenshot") ScreenshotDir = args[i + 1];
                if (args[i] == "--dx") ScreenshotDx = args[i + 1];
                if (args[i] == "--lingua") ScreenshotLang = args[i + 1];
                if (args[i] == "--tema") ScreenshotTheme = args[i + 1];
                if (args[i] == "--ore") double.TryParse(args[i + 1], System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out ScreenshotHours);
                if (args[i] == "--carattere") double.TryParse(args[i + 1], System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out ScreenshotFontPct);
            }
            // prova senza finestra: le tratte di DJ5HG (MS-Geometrie 2004, Bild 8 e 9), Quadrantidi del 4 gennaio
            for (int i = 0; i < args.Length; i++)
            {
                if (args[i] == "--prova-dj5hg") { ProvaDj5hg(); return; }
                if (args[i] == "--confronto-brams") { ConfrontoBrams(); return; }
            }
            // prova senza finestra della fonte PSKReporter MQTT (controllo automatico): --prova-mqtt <secondi>
            for (int i = 0; i < args.Length - 1; i++)
                if (args[i] == "--prova-mqtt")
                {
                    int sec; int.TryParse(args[i + 1], out sec);
                    int n = 0;
                    PskMqtt.SpotReceived += (sp, line) => { n++; if (n <= 30) Console.WriteLine(line); };
                    PskMqtt.Connect();
                    DateTime end = DateTime.UtcNow.AddSeconds(Math.Max(5, sec));
                    while (DateTime.UtcNow < end) System.Threading.Thread.Sleep(1000);
                    Console.WriteLine("stato: " + string.Format(PskMqtt.StateKey, PskMqtt.StateArg) + " - messaggi " + PskMqtt.Messages + ", spot letti " + n);
                    PskMqtt.Disconnect();
                    return;
                }
            try
            {
                BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);
            }
            catch (Exception ex)
            {
                try { File.WriteAllText(Path.Combine(AppPaths.DataDir, "errore_avvio.txt"), ex.ToString()); } catch { }
                throw;
            }
        }

        static void ProvaDj5hg()
        {
            System.Globalization.CultureInfo ci = System.Globalization.CultureInfo.InvariantCulture;
            Catalog.Load(AppPaths.DataDir);
            Shower qua = Catalog.Showers.Find(x => x.Code == "QUA");
            string[][] tr = { new[] { "JO43XN", "JN11CJ", "Amburgo-Barcellona" }, new[] { "JO43XN", "KN12PQ", "Amburgo-Sofia" },
                              new[] { "JO43XN", "KO85TS", "Amburgo-Mosca" }, new[] { "JO43XN", "JP88RK", "Amburgo-Narvik" },
                              new[] { "JN58SD", "KO85TS", "Monaco-Mosca" }, new[] { "JN58SD", "JP53EK", "Monaco-Trondheim" } };
            foreach (bool beta in new[] { true, false })
            foreach (double layer in new[] { 89.5, 102.0 })
                foreach (bool trail in new[] { false, true })
                {
                    PathModel.TrailLength = trail; PathModel.HotSpotAuto = true; PathModel.BetaFactor = beta;
                    Console.WriteLine();
                    Console.WriteLine("=== quota " + layer.ToString("F1", ci) + " km, lunghezza delle scie " + (trail ? "accesa" : "spenta") + ", angolo beta " + (beta ? "acceso" : "spento"));
                    foreach (string[] t in tr)
                    {
                        LatLon a, b; Astro.TryLocator(t[0], out a); Astro.TryLocator(t[1], out b);
                        PathModel m = PathModel.Build(a, 0, b, 0, layer, 0);
                        Console.WriteLine("--- " + t[2] + "  " + m.DistKm.ToString("F0", ci) + " km, az " + m.BearingHomeToDx.ToString("F0", ci) +
                                          ", hot spot a " + m.HotOffsetKm.ToString("F0", ci) + " km (scarto AMS " + PathModel.AmsOffsetDeg(m.DistKm).ToString("F1", ci) + ")" + (m.Valid ? "" : " NON VALIDA " + m.Message));
                        if (!m.Valid) continue;
                        Console.WriteLine("UTC   az/el rad.   eff%   dB(rel)  dB(DJ5HG)  QTF");
                        for (int h = 0; h < 24; h++)
                        {
                            DateTime u = new DateTime(2027, 1, 4, h, 0, 0, DateTimeKind.Utc);
                            double jd = Astro.JulianDay(u), lam = Astro.SolarLongitude(jd), ra, dec;
                            qua.RadiantAt(lam, u, out ra, out dec);
                            Vec3 v = Astro.RaDecToEcef(ra, dec, jd);
                            double az, el, lf; Astro.AltAz(m.Mid, v, out az, out el);
                            double e = m.Efficiency(v, out lf);
                            double db = m.AbsoluteDb(v), q = m.WeightedBearingFromHome(v);
                            Console.WriteLine(string.Format(ci, "{0:00}   {1,3:F0}/{2,3:F0}   {3,5:F1}   {4,6}   {5,6}   {6}", h, az, el, e,
                                e > 0 ? (10 * Math.Log10(e / 100)).ToString("F1", ci) : "-inf",
                                double.IsInfinity(db) || double.IsNaN(db) ? "-inf" : db.ToString("F1", ci), double.IsNaN(q) ? "-" : q.ToString("F0", ci)));
                        }
                    }
                }
            PathModel.BetaFactor = false;
            // attenuazione al punto medio: beta 0/90 gradi e raggio iniziale (ITU-R P.843), q = 1e14 e/m
            Console.WriteLine();
            Console.WriteLine("=== attenuazione al punto medio (q = 1e14 e/m)");
            Console.WriteLine("dist   quota   f MHz   phi    L(b=0)  L(b=90)  r0 m (quota ITU)  a1 dB");
            LatLon o = new LatLon(50, 10);
            foreach (double d in new[] { 600.0, 1000, 1400, 1800, 2100 })
                foreach (double layer in new[] { 89.5, 102.0 })
                    foreach (double f in new[] { 50.0, 144, 432 })
                    {
                        LatLon x = Astro.Destination(o, 90, d), mid = Astro.Destination(o, 90, d / 2);
                        PathModel pm = PathModel.Build(o, 0, x, 0, layer, 0);
                        double phi = pm.HalfScatterAngleDeg(mid);
                        double l0 = MsGeometry.PathLossDb(o, 0, x, 0, mid, layer, f, 1e14, 0, true), l90 = MsGeometry.PathLossDb(o, 0, x, 0, mid, layer, f, 1e14, 90, true);
                        Console.WriteLine(string.Format(ci, "{0,5:F0}  {1,5:F1}  {2,5:F0}  {3,5:F1}  {4,7:F1}  {5,7:F1}  {6,4:F2}  {7,5:F1}", d, layer, f, phi, l0, l90,
                            MsGeometry.InitialRadiusM(MsGeometry.ItuMeanHeightKm(f)), MsGeometry.InitialRadiusLossDb(MsGeometry.ItuMeanHeightKm(f), f, phi)));
                    }
            Console.WriteLine();
            Console.WriteLine("=== quota minima delle scie per la tratta (stazioni a livello del mare)");
            foreach (double d in new[] { 1800.0, 2000, 2100, 2124, 2200, 2300, 2500 })
                Console.WriteLine(string.Format(ci, "{0,5:F0} km: {1,6:F1} km  (elev. al punto medio con scie a 90 km: {2:F2} gradi)", d, MsGeometry.MinLayerForPathKm(d, 0), MsGeometry.ElevationArticle(d / 2, 90, 0)));
            PathModel.BetaFactor = false;
        }

        // confronto con i rilevamenti BRAMS ricevuti a Sonneberg (radiofaro di Dourbes, 49,97 MHz; maxbundscherer/meteor-scatter-v2):
        // per ogni ora dal 12 al 28/08/2026 efficienza e ZHR delle Perseidi e somma eff x ZHR degli sciami attivi
        static void ConfrontoBrams()
        {
            System.Globalization.CultureInfo ci = System.Globalization.CultureInfo.InvariantCulture;
            Catalog.Load(AppPaths.DataDir);
            LatLon tx = new LatLon(50.097, 4.588), rx = new LatLon(50.379, 11.190);
            Console.WriteLine("# tratta Dourbes-Sonneberg; colonne: utc;quota;beta;scie;dist;effPER;zhrPER;elPER;somma_eff_zhr;effANT;zhrANT");
            foreach (double layer in new[] { 95.0, 102.0 })
            foreach (bool beta in new[] { true, false })
            foreach (bool trail in new[] { false, true })
            {
                PathModel.BetaFactor = beta; PathModel.TrailLength = trail; PathModel.HotSpotAuto = true;
                PathModel m = PathModel.Build(tx, 0.2, rx, 0.6, layer, 0);
                if (!m.Valid) { Console.WriteLine("# NON VALIDA " + m.Message); continue; }
                for (DateTime u = new DateTime(2026, 8, 12, 0, 30, 0, DateTimeKind.Utc); u < new DateTime(2026, 8, 29); u = u.AddHours(1))
                {
                    double jd = Astro.JulianDay(u), lam = Astro.SolarLongitude(jd), sum = 0, eP = 0, zP = 0, elP = -90, eA = 0, zA = 0;
                    foreach (Shower sh in Catalog.Showers)
                    {
                        if (!sh.IsActive(u)) continue;
                        double z = sh.ZhrAt(lam, u), ra, dec; sh.RadiantAt(lam, u, out ra, out dec);
                        Vec3 v = Astro.RaDecToEcef(ra, dec, jd);
                        double lf, e = m.Efficiency(v, out lf);
                        sum += e / 100 * z;
                        if (sh.Code == "PER") { eP = e; zP = z; double az; Astro.AltAz(m.Mid, v, out az, out elP); }
                        if (sh.IsAntihelion) { eA = e; zA = z; }
                    }
                    Console.WriteLine(string.Format(ci, "{0:yyyy-MM-ddTHH:mm};{1:F0};{2};{3};{4:F0};{5:F2};{6:F2};{7:F1};{8:F3};{9:F2};{10:F2}",
                        u, layer, beta ? 1 : 0, trail ? 1 : 0, m.DistKm, eP, zP, elP, sum, eA, zA));
                }
            }
            PathModel.BetaFactor = true; PathModel.TrailLength = false;
        }

        public static AppBuilder BuildAvaloniaApp()
        {
            return AppBuilder.Configure<App>().UsePlatformDetect().WithInterFont().LogToTrace();
        }
    }
}
