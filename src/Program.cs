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
                if (args[i] == "--prova-dj5hg") { ProvaDj5hg(); return; }
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
            foreach (double layer in new[] { 89.5, 102.0 })
                foreach (bool trail in new[] { false, true })
                {
                    PathModel.TrailLength = trail; PathModel.HotSpotAuto = true;
                    Console.WriteLine();
                    Console.WriteLine("=== quota " + layer.ToString("F1", ci) + " km, lunghezza delle scie " + (trail ? "accesa" : "spenta"));
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
        }

        public static AppBuilder BuildAvaloniaApp()
        {
            return AppBuilder.Configure<App>().UsePlatformDetect().WithInterFont().LogToTrace();
        }
    }
}
