// YA-MS - linguetta "Mappa quadrati": quadrati Maidenhead lavorati letti da un file ADIF (nessun collegamento a LoTW)
// Il caricamento di un nuovo ADIF sostituisce i dati precedenti; i dati restano in data/adif_quadrati.csv.
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Platform.Storage;

namespace YAMS
{
    public partial class MainWindow
    {
        List<GridMapView> gridViews = new List<GridMapView>();
        TextBlock lblAdif;

        void BuildGridTab()
        {
            DockPanel p = Page("Mappa quadrati");
            Button bLoad = B("Carica file ADIF...");
            Button bClear = B("Cancella memoria");
            bClear.Background = Pal.B(Pal.Rgb(127, 29, 29));
            lblAdif = L("");
            bLoad.Click += async (s, e) => await LoadAdifFile();
            bClear.Click += async (s, e) =>
            {
                try
                {
                    if (!await Dialogs.Confirm(this, "Cancella memoria", "Cancellare tutti i quadrati caricati dal file ADIF?")) return;
                    AdifStore.Clear(dataDir);
                    RefreshGrids();
                }
                catch (Exception ex) { await Dialogs.Message(this, "Cancella memoria", ex.Message); }
            };
            DockTop(p, Row(bLoad, bClear, lblAdif, L("Rotellina = zoom, trascina = sposta, mouse sopra un quadrato = QSO")));
            // sotto-linguette a pillola, una per banda
            PillTabs sub = new PillTabs();
            for (int i = 0; i < AdifStore.Bands.Length; i++)
            {
                GridMapView v = new GridMapView();
                v.Band = AdifStore.Bands[i];
                sub.Add(AdifStore.BandNames[i], v);
                gridViews.Add(v);
            }
            DockTop(p, sub.Bar);
            p.Children.Add(sub.Host);
            try { AdifStore.Load(dataDir); } catch { }
            RefreshGrids();
        }

        async Task LoadAdifFile()
        {
            try
            {
                IReadOnlyList<IStorageFile> files = await StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions
                {
                    Title = "File ADIF del log",
                    AllowMultiple = false,
                    FileTypeFilter = new[]
                    {
                        new FilePickerFileType("File ADIF") { Patterns = new[] { "*.adi", "*.adif", "*.ADI", "*.ADIF" } },
                        new FilePickerFileType("Tutti i file") { Patterns = new[] { "*" } }
                    }
                });
                if (files == null || files.Count == 0) return;
                string path = files[0].TryGetLocalPath();
                if (path == null) { await Dialogs.Message(this, "File ADIF", "Il file scelto non e' un file locale."); return; }
                try
                {
                    string msg;
                    AdifStore.LoadAdif(path, out msg);   // sostituisce i dati precedenti
                    AdifStore.Save(dataDir);
                    status.Text = msg;
                }
                catch (Exception ex) { await Dialogs.Message(this, "File ADIF", ex.Message); }
                RefreshGrids();
            }
            catch (Exception ex) { await Dialogs.Message(this, "File ADIF", ex.Message); }
        }

        void RefreshGrids()
        {
            if (lblAdif == null) return;
            lblAdif.Text = AdifStore.Qsos.Count == 0 ? "nessun ADIF caricato" : "ADIF: " + AdifStore.SourceName + " (" + AdifStore.Qsos.Count + " quadrati-QSO)";
            string home = txtHome != null ? Up(txtHome) : "";
            foreach (GridMapView v in gridViews)
            {
                v.HomeGrid = home.Length >= 4 ? home.Substring(0, 4) : "";
                if (sky != null) { v.Coast = sky.MapLines; v.Borders = sky.MapBorders; }
                v.InvalidateVisual();
            }
        }
    }
}
