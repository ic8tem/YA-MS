// YA-MS - fotografie delle linguette per il controllo automatico su GitHub (opzione nascosta --screenshot)
using System;
using System.IO;
using System.Threading.Tasks;
using Avalonia;
using Avalonia.Media.Imaging;

namespace YAMS
{
    public partial class MainWindow
    {
        // --screenshot <cartella> [--dx LOCATOR] [--ore H]: imposta la tratta, sposta la volta celeste di H ore
        // (passi di 15 minuti), fotografa ogni linguetta e chiude il programma.
        public async Task RunScreenshots(string dir, string dx, double hours)
        {
            try
            {
                Directory.CreateDirectory(dir);
                await Task.Delay(4000);
                if (!string.IsNullOrEmpty(dx)) { txtDx.Text = dx; Recalc(); }
                trackTime.Value = Math.Max(trackTime.Minimum, Math.Min(trackTime.Maximum, Math.Round(hours * 4)));
                UpdateSky();
                await Task.Delay(8000);   // tempo per scaricare la mappa e i dati dei radar
                for (int i = 0; i < 9; i++)
                {
                    tabs.Select(i);
                    await Task.Delay(1500);
                    PixelSize ps = new PixelSize(Math.Max(100, (int)Bounds.Width), Math.Max(100, (int)Bounds.Height));
                    using (RenderTargetBitmap rtb = new RenderTargetBitmap(ps, new Vector(96, 96)))
                    {
                        rtb.Render(this);
                        rtb.Save(Path.Combine(dir, "linguetta_" + (i + 1) + ".png"));
                    }
                }
            }
            catch (Exception ex)
            {
                try { File.WriteAllText(Path.Combine(dir, "errore.txt"), ex.ToString()); } catch { }
            }
            Close();
        }
    }
}
