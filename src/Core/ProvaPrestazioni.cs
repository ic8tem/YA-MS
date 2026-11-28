// YA-MS - prova delle prestazioni (senza finestra): --prova-prestazioni
// Confronta il calcolo di prima e quello ottimizzato della 1.8.29 sugli stessi dati: i risultati devono coincidere
// (entro l'arrotondamento) e si misurano tempi e memoria. Esce con codice 1 se un risultato differisce.
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Text;

namespace YAMS
{
    public static class ProvaPrestazioni
    {
        static readonly CultureInfo CI = CultureInfo.InvariantCulture;
        static int errors; static string DataDir = "";

        public static void Run()
        {
            string dd = Path.Combine(AppContext.BaseDirectory, "data"); DataDir = dd;
            Catalog.Load(dd);
            Nuvole();
            Mqtt();
            Call3();
            Console.WriteLine(errors == 0 ? "ESITO: risultati identici" : "ESITO: " + errors + " differenze");
            Environment.Exit(errors == 0 ? 0 : 1);
        }

        static void Report(string name, double oldMs, double newMs)
        {
            double gain = oldMs > 0 ? 100.0 * (oldMs - newMs) / oldMs : 0;
            Console.WriteLine(string.Format(CI, "{0}: prima {1:F0} ms, dopo {2:F0} ms, miglioramento {3:F1} %", name, oldMs, newMs, gain));
        }

        // ---- 1. nuvole del traffico in diretta ----
        static void Nuvole()
        {
            Random r = new Random(42);
            string[] locs = { "JN70CN", "JO62QM", "JN45NM", "KO47ES", "IO91WM", "JO31NF", "JN58TD", "KN34BB", "IN80DJ", "JP50EK", "KO85TS", "JN19AN", "KM18UQ", "IM58KQ", "JO99BL", "KN05OS" };
            DateTime[] when = { new DateTime(2026, 12, 14, 2, 0, 0, DateTimeKind.Utc), new DateTime(2026, 8, 12, 23, 0, 0, DateTimeKind.Utc),
                                new DateTime(2027, 1, 3, 6, 0, 0, DateTimeKind.Utc), new DateTime(2026, 11, 18, 4, 0, 0, DateTimeKind.Utc),
                                new DateTime(2026, 6, 7, 10, 0, 0, DateTimeKind.Utc), new DateTime(2026, 3, 15, 12, 0, 0, DateTimeKind.Utc) };
            List<Tuple<LatLon, LatLon, DateTime>> cases = new List<Tuple<LatLon, LatLon, DateTime>>();
            while (cases.Count < 60)
            {
                LatLon a, b;
                Astro.TryLocator(locs[r.Next(locs.Length)], out a); Astro.TryLocator(locs[r.Next(locs.Length)], out b);
                double d = Astro.DistanceKm(a, b);
                if (d < 400 || d > 2200) continue;
                cases.Add(Tuple.Create(a, b, when[r.Next(when.Length)].AddMinutes(r.Next(0, 600))));
            }
            List<List<TrafficCloud>> oldR = new List<List<TrafficCloud>>(), newR = new List<List<TrafficCloud>>();
            Stopwatch sw = Stopwatch.StartNew();
            foreach (var c in cases) oldR.Add(TrafficClouds.Compute(c.Item3, c.Item1, c.Item2, 90, false));
            double tOld = sw.Elapsed.TotalMilliseconds;
            sw.Restart();
            foreach (var c in cases) newR.Add(TrafficClouds.Compute(c.Item3, c.Item1, c.Item2, 90, true));
            double tNew = sw.Elapsed.TotalMilliseconds;
            int diff = 0, sporadic = 0;
            for (int i = 0; i < cases.Count; i++)
            {
                List<TrafficCloud> o = oldR[i], n = newR[i];
                if (o.Count != n.Count) { diff++; continue; }
                for (int k = 0; k < o.Count; k++)
                {
                    TrafficCloud x = o[k], y = n[k];
                    if (x.Sporadic) sporadic++;
                    if (x.Sporadic != y.Sporadic || Math.Abs(x.Centre.Lat - y.Centre.Lat) > 1e-6 || Math.Abs(x.Centre.Lon - y.Centre.Lon) > 1e-6
                        || Math.Abs(x.MajorKm - y.MajorKm) > 1e-6 || Math.Abs(x.MinorKm - y.MinorKm) > 1e-6
                        || Math.Abs(Astro.Norm180(x.AngleDeg - y.AngleDeg)) > 1e-6 || Math.Abs(x.Share - y.Share) > 1e-9) diff++;
                }
            }
            Console.WriteLine(string.Format(CI, "Nuvole: {0} tratte, nuvole di sole sporadiche {1}, differenze {2}", cases.Count, sporadic, diff));
            errors += diff;
            Report("Nuvole del traffico (60 tratte)", tOld, tNew);
        }

        // ---- 2. PSKReporter MQTT ----
        static void Mqtt()
        {
            Random r = new Random(7);
            string[] modes = { "FT8", "FT8", "FT8", "FT8", "MSK144", "FT4", "Q65" };
            string[] bands = { "6m", "2m", "4m" };
            List<byte[]> msgs = new List<byte[]>();
            long t0 = 1764320000;
            for (int i = 0; i < 200000; i++)
            {
                string md = modes[r.Next(modes.Length)];
                string sc = "IZ" + r.Next(0, 10) + (char)('A' + r.Next(26)) + (char)('A' + r.Next(26)) + (char)('A' + r.Next(26));
                string rc = (i % 5 == 0 ? "dl" : "DK") + r.Next(0, 10) + (char)('A' + r.Next(26)) + (char)('A' + r.Next(26));
                string sl = "" + (char)('I' + r.Next(5)) + (char)('L' + r.Next(5)) + r.Next(10) + r.Next(10) + (i % 3 == 0 ? "" + (char)('A' + r.Next(24)) + (char)('A' + r.Next(24)) : "");
                string rl = "JO" + r.Next(10) + r.Next(10) + (char)('A' + r.Next(24)) + (char)('A' + r.Next(24));
                string json = i % 97 == 0
                    ? "{\"sq\":" + i + ",\"f\":\"50313000\",\"md\":\"" + md + "\",\"rp\":\"-7\",\"t\":" + (t0 + i) + ",\"sc\":\"" + sc + "\",\"sl\":\"" + sl + "\",\"rc\":\"" + rc + "\",\"rl\":" + 1234 + ",\"b\":\"6m\"}"
                    : "{\"sq\":" + (30000000000L + i) + ",\"f\":" + (50313000 + r.Next(-3000, 3000)) + ",\"md\":\"" + md + "\",\"rp\":" + r.Next(-24, 15) +
                      ",\"t\":" + (t0 + i) + ",\"t_tx\":" + (t0 + i - 1) + ",\"b\":\"" + bands[r.Next(3)] + "\",\"sc\":\"" + sc + "\",\"sl\":\"" + sl + "\",\"rc\":\"" + rc +
                      "\",\"rl\":\"" + rl + "\",\"sa\":248,\"ra\":230}";
                if (i % 1001 == 0) json = "{\"f\":0,\"sc\":\"X\"}";          // scartato (frequenza)
                if (i % 1999 == 0) json = "{\"f\":50313000,\"sc\":\"IZ8XX\""; // JSON troncato
                msgs.Add(Encoding.UTF8.GetBytes(json));
            }
            DateTime now = DateTimeOffset.FromUnixTimeSeconds(t0 + 100000).UtcDateTime;
            // prima: stringa UTF-8, JsonDocument, riga della console sempre scritta
            List<MsSpot> a = new List<MsSpot>(msgs.Count), b = new List<MsSpot>(msgs.Count);
            Stopwatch sw = Stopwatch.StartNew();
            foreach (byte[] m in msgs) { string js = Encoding.UTF8.GetString(m); a.Add(PskMqtt.ParseJson(js, now)); }
            double tOld = sw.Elapsed.TotalMilliseconds;
            sw.Restart();
            foreach (byte[] m in msgs) b.Add(PskMqtt.ParseJsonFast(m, now));   // riga della console non richiesta (spot FT8 scartati prima)
            double tNew = sw.Elapsed.TotalMilliseconds;
            int diff = 0, nulls = 0;
            for (int i = 0; i < msgs.Count; i++)
            {
                MsSpot x = a[i], y = b[i];
                if (x == null || y == null) { if ((x == null) != (y == null)) diff++; else nulls++; continue; }
                if (x.FreqKHz != y.FreqKHz || x.DxCall != y.DxCall || x.Spotter != y.Spotter || x.Utc != y.Utc || x.Mode != y.Mode
                    || x.LocDx != y.LocDx || x.LocSpotter != y.LocSpotter || x.Comment != y.Comment || x.Source != y.Source || x.Line != y.Line) diff++;
            }
            Console.WriteLine(string.Format(CI, "MQTT: {0} messaggi, scartati da entrambi {1}, differenze {2}", msgs.Count, nulls, diff));
            errors += diff;
            Report("Lettura PSKReporter MQTT (200 000 messaggi)", tOld, tNew);
        }

        // ---- 3. CALL3 ----
        static void Call3()
        {
            string path = Path.Combine(DataDir, "call3.txt");
            if (!File.Exists(path)) { Console.WriteLine("CALL3: file assente, prova saltata"); return; }
            List<KeyValuePair<string, string>> list = new List<KeyValuePair<string, string>>();
            Dictionary<string, string> pool = new Dictionary<string, string>(StringComparer.Ordinal);
            using (StreamReader sr = new StreamReader(path, Encoding.Latin1))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    if (line.StartsWith("//", StringComparison.Ordinal)) continue;
                    int c1 = line.IndexOf(',');
                    if (c1 <= 0) continue;
                    int c2 = line.IndexOf(',', c1 + 1);
                    string call = line.Substring(0, c1).Trim().ToUpperInvariant();
                    string loc = (c2 > c1 ? line.Substring(c1 + 1, c2 - c1 - 1) : line.Substring(c1 + 1)).Trim().ToUpperInvariant();
                    if (call.Length == 0 || loc.Length < 4) continue;
                    string pl; if (!pool.TryGetValue(loc, out pl)) { pool[loc] = loc; pl = loc; }
                    list.Add(new KeyValuePair<string, string>(call, pl));
                }
            }
            list.Sort((x, y) => string.CompareOrdinal(x.Key, y.Key));
            int n = list.Count;
            // memoria dei soli nominativi: prima (stringhe) e dopo (blocco compatto)
            GC.Collect(); GC.WaitForPendingFinalizers(); GC.Collect();
            long m0 = GC.GetTotalMemory(true);
            string[] oldCalls = new string[n];
            for (int i = 0; i < n; i++) oldCalls[i] = new string(list[i].Key.AsSpan());   // copie: le stringhe di 'list' restano a parte
            long m1 = GC.GetTotalMemory(true);
            CallIndex idx = CallIndex.Build(list);
            long m2 = GC.GetTotalMemory(true);
            double memOld = (m1 - m0) / 1048576.0, memNew = (m2 - m1) / 1048576.0;
            // ricerche: tutti i nominativi a passo 3, poi nominativi assenti
            List<string> q = new List<string>();
            for (int i = 0; i < n; i += 3) q.Add(list[i].Key);
            Random r = new Random(3);
            for (int i = 0; i < 200000; i++) q.Add("ZZ" + r.Next(0, 10) + (char)('A' + r.Next(26)) + (char)('A' + r.Next(26)) + (i % 7 == 0 ? "/P" : ""));
            q.Add("ÀÉ9"); q.Add("IC8TEMĀ");
            int[] ro = new int[q.Count], rn = new int[q.Count];
            Stopwatch sw = Stopwatch.StartNew();
            for (int k = 0; k < q.Count; k++) ro[k] = OldFind(oldCalls, q[k]);
            double tOld = sw.Elapsed.TotalMilliseconds;
            sw.Restart();
            for (int k = 0; k < q.Count; k++) rn[k] = idx.Find(q[k]);
            double tNew = sw.Elapsed.TotalMilliseconds;
            int diff = 0;
            for (int k = 0; k < q.Count; k++) if (ro[k] != rn[k]) diff++;
            for (int i = 0; i < n; i += 997) if (idx[i] != oldCalls[i]) diff++;
            Console.WriteLine(string.Format(CI, "CALL3: {0} nominativi, {1} ricerche, differenze {2}", n, q.Count, diff));
            errors += diff;
            double gainMem = memOld > 0 ? 100.0 * (memOld - memNew) / memOld : 0;
            Console.WriteLine(string.Format(CI, "Memoria dei nominativi CALL3: prima {0:F1} MB, dopo {1:F1} MB, miglioramento {2:F1} %", memOld, memNew, gainMem));
            Report("Ricerche CALL3", tOld, tNew);
            GC.KeepAlive(oldCalls); GC.KeepAlive(idx);
        }

        static int OldFind(string[] c, string call)
        {
            int lo = 0, hi = c.Length - 1;
            while (lo <= hi)
            {
                int mid = (lo + hi) >> 1;
                int k = string.CompareOrdinal(c[mid], call);
                if (k == 0) return mid;
                if (k < 0) lo = mid + 1; else hi = mid - 1;
            }
            return -1;
        }
    }
}
