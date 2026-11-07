using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;

namespace YAMS
{
    public partial class App : Application
    {
        public override void Initialize()
        {
            AvaloniaXamlLoader.Load(this);
        }

        public override void OnFrameworkInitializationCompleted()
        {
            if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
            {
                // lingua dell'interfaccia (chiave "lingua" di config.ini) prima di costruire la finestra
                Config cfg = null;
                try { cfg = new Config(System.IO.Path.Combine(AppPaths.DataDir, "config.ini")); } catch { }
                try { Lang.Init(Program.ScreenshotLang ?? (cfg != null ? cfg.Get("lingua", "") : "")); } catch { }
                // schema di colori (chiave "tema" di config.ini, oppure --tema per le fotografie) prima di costruire la finestra
                try { Tema.Imposta(Tema.DaChiave(Program.ScreenshotTheme ?? (cfg != null ? cfg.Get("tema", "chiaro") : "chiaro"))); } catch { }
                MainWindow w = new MainWindow();
                desktop.MainWindow = w;
                if (Program.ScreenshotDir != null)
                    w.Opened += async (s, e) => await w.RunScreenshots(Program.ScreenshotDir, Program.ScreenshotDx, Program.ScreenshotHours);
            }
            base.OnFrameworkInitializationCompleted();
        }
    }
}
