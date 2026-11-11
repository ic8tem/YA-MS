// YA-MS - avviso e installazione delle nuove versioni pubblicate su GitHub, controllo dei file del programma mancanti
//  - all'avvio (una volta al giorno) si guarda l'ultima Release; se e' piu' nuova compare una finestra con
//    "Aggiorna adesso", "Più tardi", "Salta questa versione"; il pulsante "Aggiornamenti" nella barra in basso
//    fa lo stesso controllo a mano, anche per una versione saltata;
//  - all'avvio si controlla che ci siano tutti i file del programma (data e doc): se ne mancano, una finestra
//    li elenca e propone di riscaricarli da GitHub.
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Threading;

namespace YAMS
{
    public partial class MainWindow
    {
        Button btnUpdate;
        static bool startupChecksDone;   // una sola volta per avvio, anche se la finestra si ricrea (lingua, tema)
        bool updateBusy;

        async Task StartupUpdateChecks()
        {
            if (startupChecksDone || Program.ScreenshotDir != null) return;
            startupChecksDone = true;
            await Task.Run(() => Updater.Cleanup());
            await CheckMissingFiles(false);
            if (!cfg.GetB("controlla_aggiornamenti", true)) return;
            DateTime last;
            if (DateTime.TryParse(cfg.Get("aggiornamenti_ultimo_controllo", ""), CultureInfo.InvariantCulture,
                    DateTimeStyles.AdjustToUniversal | DateTimeStyles.AssumeUniversal, out last) && (DateTime.UtcNow - last).TotalHours < 20) return;
            await CheckUpdates(false);
        }

        async void CheckUpdatesManual()
        {
            if (updateBusy) return;
            await CheckMissingFiles(true);
            await CheckUpdates(true);
        }

        async Task CheckMissingFiles(bool manual)
        {
            List<string> miss = await Task.Run(() => Updater.MissingFiles());
            if (miss.Count == 0) return;
            List<string> shown = miss.Count > 25 ? miss.GetRange(0, 25) : miss;
            string list = "  " + string.Join("\n  ", shown) + (miss.Count > 25 ? "\n  " + Lang.F("... e altri {0}", miss.Count - 25) : "");
            int ch = await Dialogs.Choice(this, Lang.T("File mancanti"),
                Lang.F("Mancano {0} file del programma:\n{1}\n\nLi scarico da GitHub (versione {2})?", miss.Count, list, AppPaths.Version),
                Lang.T("Scarica i file mancanti"), Lang.T("Continua senza"));
            if (ch != 0) return;
            updateBusy = true;
            int ok;
            try
            {
                ok = await Task.Run(() => Updater.DownloadMissing(miss, (i, n) =>
                    Dispatcher.UIThread.Post(() => status.Text = Lang.F("Scaricamento dei file mancanti: {0} di {1}", i, n))));
            }
            finally { updateBusy = false; }
            if (ok == miss.Count)
            {
                status.Text = Lang.F("Scaricati {0} file mancanti.", ok);
                await Dialogs.Message(this, Lang.T("File mancanti"), Lang.F("Scaricati {0} file mancanti.", ok) + "\n\n" +
                    Lang.T("Alcune modifiche si vedono solo dopo aver riavviato il programma."));
            }
            else
            {
                status.Text = Lang.F("Scaricati {0} file su {1}.", ok, miss.Count);
                await Dialogs.Message(this, Lang.T("File mancanti"), Lang.F("Scaricati {0} file su {1}.", ok, miss.Count) + "\n\n" +
                    Lang.T("Controlla la connessione a Internet, oppure scarica di nuovo il pacchetto completo dalla pagina delle release."));
            }
        }

        async Task CheckUpdates(bool manual)
        {
            if (updateBusy) return;
            updateBusy = true;
            ReleaseInfo ri = null; string err = null;
            try
            {
                if (manual) status.Text = Lang.T("Controllo degli aggiornamenti su GitHub...");
                try { ri = await Task.Run(() => Updater.GetLatest()); }
                catch (Exception ex) { err = ex.Message; }
                cfg.Set("aggiornamenti_ultimo_controllo", DateTime.UtcNow.ToString("o", CultureInfo.InvariantCulture));
                try { cfg.Save(); } catch { }
            }
            finally { updateBusy = false; }

            if (ri == null)
            {
                if (manual)
                {
                    status.Text = Lang.T("Pronto");
                    await ErrorWithReleasePage(Lang.F("Non riesco a leggere le versioni pubblicate su GitHub: {0}", err));
                }
                return;
            }
            if (ri.Ver <= Updater.Current)
            {
                if (manual)
                {
                    status.Text = Lang.F("YA-MS è aggiornato (versione {0}).", AppPaths.Version);
                    await Dialogs.Message(this, Lang.T("Aggiornamenti"), Lang.F("YA-MS è aggiornato (versione {0}).", AppPaths.Version));
                }
                return;
            }
            if (!manual && cfg.Get("aggiornamenti_salta", "") == ri.VersionText) return;

            string notes = (ri.Notes ?? "").Trim();
            if (notes.Length > 1500) notes = notes.Substring(0, 1500) + " ...";
            if (ri.AssetUrl == null)
            {
                int c = await Dialogs.Choice(this, Lang.T("Aggiornamento disponibile"),
                    Lang.F("È disponibile YA-MS {0} (questa è la {1}).", ri.VersionText, AppPaths.Version) + "\n\n" + notes + "\n\n" +
                    Lang.F("Nella release non c'è il pacchetto per questo sistema ({0}): scaricalo a mano dalla pagina delle release.", Updater.AssetSuffix().TrimStart('-')),
                    Lang.T("Apri la pagina delle release"), Lang.T("Più tardi"));
                if (c == 0) OpenUrl(ri.PageUrl);
                return;
            }
            int ch = await Dialogs.Choice(this, Lang.T("Aggiornamento disponibile"),
                Lang.F("È disponibile YA-MS {0} (questa è la {1}).", ri.VersionText, AppPaths.Version) + "\n\n" + notes + "\n\n" +
                Lang.F("Il programma scarica il pacchetto {0}, sostituisce i suoi file, tiene la cartella data (i file del programma cambiati vengono prima copiati in data/backup) e si riavvia.", ri.AssetName),
                Lang.T("Aggiorna adesso"), Lang.T("Più tardi"), Lang.T("Salta questa versione"));
            if (ch == 2) { cfg.Set("aggiornamenti_salta", ri.VersionText); try { cfg.Save(); } catch { } return; }
            if (ch != 0) return;
            await InstallUpdate(ri);
        }

        async Task InstallUpdate(ReleaseInfo ri)
        {
            if (!CanWriteProgramFolder())
            {
                await ErrorWithReleasePage(Lang.F("Non posso scrivere nella cartella del programma ({0}): installa la nuova versione a mano.", AppPaths.AppDir));
                return;
            }
            updateBusy = true;
            btnUpdate.IsEnabled = false;
            ProcessStartInfo restart = null; int backedUp = 0; string err = null;
            try
            {
                SaveConfig();
                string outDir = await Task.Run(() => Updater.DownloadAndExtract(ri, p =>
                    Dispatcher.UIThread.Post(() => status.Text = p >= 0 ? Lang.F("Scaricamento dell'aggiornamento: {0} %", p) : Lang.T("Scaricamento dell'aggiornamento..."))));
                status.Text = Lang.T("Installazione dell'aggiornamento...");
                restart = await Task.Run(() => { int b; ProcessStartInfo r = Updater.Install(outDir, out b); backedUp = b; return r; });
            }
            catch (Exception ex) { err = ex.Message; }
            finally { updateBusy = false; btnUpdate.IsEnabled = true; }

            if (restart == null)
            {
                status.Text = Lang.T("Pronto");
                await ErrorWithReleasePage(Lang.F("L'aggiornamento non è riuscito: {0}", err));
                return;
            }
            string msg = Lang.F("YA-MS {0} è installato. Il programma ora si riavvia.", ri.VersionText);
            if (backedUp > 0) msg += "\n\n" + Lang.F("{0} file della cartella data sono stati sostituiti: le copie precedenti sono in data/backup/v{1}.", backedUp, AppPaths.Version);
            await Dialogs.Message(this, Lang.T("Aggiornamento installato"), msg);
            try
            {
                cfg.Set("aggiornamenti_salta", "");
                SaveConfig();
                MsCollector.Shutdown();
                replaced = true;   // impostazioni gia' salvate
                Process.Start(restart);
            }
            catch (Exception ex)
            {
                await Dialogs.Message(this, Lang.T("Aggiornamento installato"), Lang.F("Riavvia YA-MS a mano: {0}", ex.Message));
            }
            if (Avalonia.Application.Current != null && Avalonia.Application.Current.ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
                desktop.Shutdown();
            else Close();
        }

        static bool CanWriteProgramFolder()
        {
            try
            {
                string probe = Path.Combine(AppContext.BaseDirectory, ".prova-scrittura");
                File.WriteAllText(probe, "x");
                File.Delete(probe);
                string bundle = Updater.RunningBundle();
                if (bundle != null)
                {
                    probe = Path.Combine(Path.GetDirectoryName(bundle), ".prova-scrittura");
                    File.WriteAllText(probe, "x");
                    File.Delete(probe);
                }
                return true;
            }
            catch { return false; }
        }

        async Task ErrorWithReleasePage(string text)
        {
            int c = await Dialogs.Choice(this, Lang.T("Aggiornamenti"), text, Lang.T("Apri la pagina delle release"), Lang.T("Chiudi"));
            if (c == 0) OpenUrl(Updater.ReleasesPage);
        }

        static void OpenUrl(string url)
        {
            try { Dialogs.OpenWithDefaultApp(url); } catch { }
        }
    }
}
