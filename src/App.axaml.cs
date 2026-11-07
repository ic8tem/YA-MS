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
                try { Lang.Init(new Config(System.IO.Path.Combine(AppPaths.DataDir, "config.ini")).Get("lingua", "")); } catch { }
                MainWindow w = new MainWindow();
                desktop.MainWindow = w;
                if (Program.ScreenshotDir != null)
                    w.Opened += async (s, e) => await w.RunScreenshots(Program.ScreenshotDir, Program.ScreenshotDx, Program.ScreenshotHours);
            }
            base.OnFrameworkInitializationCompleted();
        }
    }
}
