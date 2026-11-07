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

        public static AppBuilder BuildAvaloniaApp()
        {
            return AppBuilder.Configure<App>().UsePlatformDetect().WithInterFont().LogToTrace();
        }
    }
}
