# YA-MS - convenzioni del porting da WinForms (.NET Framework) a .NET 8 + Avalonia 11.2.3

Vecchio programma (WinForms, C# 5, NON modificare): `/home/claude/MSSciami/src/*.cs`
Nuovo progetto: `/home/claude/YA-MS` (progetto `YA-MS.csproj`, net8.0, Avalonia 11.2.3, Fluent, Inter).

## Regole generali
- Namespace unico: `YAMS`. `Nullable` disabilitato, `ImplicitUsings` disabilitato: scrivere sempre gli `using`.
- C# moderno permesso (C# 12). Nessun compilatore disponibile in locale: la compilazione avviene su GitHub Actions.
  Quindi usare SOLO API Avalonia 11.2 certe e semplici; niente pacchetti oltre a quelli del csproj
  (Avalonia, Avalonia.Desktop, Avalonia.Themes.Fluent, Avalonia.Fonts.Inter; SkiaSharp e' gia' dipendenza).
- Niente XAML per finestre e controlli: interfaccia costruita in codice C#. Gli stili esistono gia' in `src/App.axaml`
  (classi: `Button.pill`, `Button.accent`, `ToggleButton.tab`, `TextBlock.label`).
- Colori e caratteri: `src/UI/Theme.cs` (classe `Pal`): `Pal.Back, Panel, Panel2, Panel3, Track, Border, Fore, Muted, Azure,
  Violet, Green, Yellow, Orange, OrangeDark, OrangeText, Pink, Red, HotPink, HotGrey, Silver`; helper `Pal.A(alpha, color)`,
  `Pal.Rgb`, `Pal.Argb`, `Pal.B(color)` -> IBrush, `Pal.P(color, width)` / `Pal.P(color, width, Pal.Dash|Pal.Dot|Pal.DashDot)` -> IPen,
  `Pal.Mono` (FontFamily monospace), `Pal.Ui`.
- Dati SEMPRE in `AppPaths.DataDir` (cartella `data` accanto al programma). Documenti in `AppPaths.DocDir`.
  Titolo finestra: `AppPaths.Title` ("YA-MS 1.0.0 - a cura di Costantino IC8TEM").
- La logica di calcolo e' gia' portata in `src/Core/` (Astro, Catalog, MsModel, RadarFlux, Config, MapData, AppPaths):
  stesse classi e metodi del vecchio programma. `System.Drawing.PointF/Color/Rectangle` di System.Drawing.Primitives
  esistono anche in .NET 8 ma NON vanno usati per disegnare: per disegnare si usano i tipi Avalonia.
  `MapData.Load` restituisce `List<System.Drawing.PointF[]>` (X = lon, Y = lat): va bene tenerlo cosi'.
- Testi dell'interfaccia in italiano, identici al vecchio programma salvo "MS Sciami" -> "YA-MS".

## Lingue dell'interfaccia (src/UI/Lang.cs)
- L'italiano e' la lingua di partenza: ogni testo visibile passa da `Lang.T("testo italiano")` oppure, con valori,
  da `Lang.F("testo con {0} e {1:F1}", a, b)` (UNA sola chiave per frase, mai frasi spezzate con +). Le chiavi devono essere
  stringhe letterali; i testi che arrivano dai dati (nomi degli sciami, etichette Hot/Limite) con `Lang.T(variabile)`
  e vanno elencati in `tools/estrai_chiavi.py` (EXTRA / KNOWN_DYNAMIC).
- Traduzioni in `data/lingue/<codice>.txt` (chiave TAB traduzione, `\n` = a capo). Dopo ogni modifica dei testi:
  `python3 tools/estrai_chiavi.py --controlla` rigenera `data/lingue/chiavi.txt` e mostra le chiavi mancanti.
- Mai confrontare un testo mostrato per decidere il comportamento (usare indici o codici).
- La lettura dei file di dati usa sempre `CultureInfo.InvariantCulture` (la cultura corrente segue la lingua scelta).

## Promemoria API Avalonia 11.2
- Controllo disegnato: `public class X : Control { public override void Render(DrawingContext ctx) { ... } }`,
  dimensioni `Bounds.Width/Height`, ridisegno `InvalidateVisual()`. Riempire sempre tutto lo sfondo nel Render
  (serve anche per ricevere i clic).
- Disegno: `ctx.DrawLine(IPen, Point, Point)`, `ctx.DrawRectangle(IBrush, IPen, Rect)` (o con raggio: `DrawRectangle(brush, pen, rect, rx, ry)`),
  `ctx.DrawEllipse(IBrush, IPen, Point centro, rx, ry)`, `ctx.DrawGeometry(IBrush, IPen, Geometry)` con
  `var g = new StreamGeometry(); using (var c = g.Open()) { c.BeginFigure(p0, isFilled); c.LineTo(p1); c.EndFigure(isClosed); }`.
- Testo: `var ft = new FormattedText(text, CultureInfo.CurrentCulture, FlowDirection.LeftToRight, new Typeface(fontFamily, FontStyle.Normal, FontWeight.Bold), emSize, brush); ctx.DrawText(ft, new Point(x, y));` misure `ft.Width`, `ft.Height`.
  Dimensioni carattere: 1 pt WinForms ~ 1.33 px Avalonia (8 pt -> ~11 px, 9 pt -> 12 px, 12 pt -> 16 px).
- Ritaglio/trasformazioni/opacita': `using (ctx.PushClip(rect))`, `using (ctx.PushGeometryClip(geometry))`,
  `using (ctx.PushTransform(Matrix.CreateRotation(rad) * Matrix.CreateTranslation(x, y)))`, `using (ctx.PushOpacity(0.5))`.
- Mouse: `PointerPressed += (s, e) => { var p = e.GetPosition(this); var pp = e.GetCurrentPoint(this).Properties; if (pp.IsRightButtonPressed) ... }`,
  `PointerMoved`, `PointerReleased`, `PointerWheelChanged` (`e.Delta.Y`), `PointerEntered/PointerExited`. Tooltip: `ToolTip.SetTip(this, testo)`.
- Immagini: `new Avalonia.Media.Imaging.Bitmap(path)`; controllo `new Image { Source = bmp, Stretch = Stretch.Uniform }`; disegno `ctx.DrawImage(bmp, new Rect(...))`.
- Layout: `DockPanel` (`DockPanel.SetDock(c, Dock.Top)`), `Grid` (`ColumnDefinitions = new ColumnDefinitions("60*,40*")`, `Grid.SetColumn/SetRow`),
  `StackPanel { Orientation = Orientation.Horizontal, Spacing = 6 }`, `WrapPanel`, `ScrollViewer`, `Border { Background, CornerRadius, Padding, Child }`.
- Input: `TextBox.Text`, `CheckBox.IsChecked` (bool?), `NumericUpDown` (`Value` decimal?, `Minimum/Maximum/Increment` decimal, `FormatString`),
  `ComboBox` (`ItemsSource`, `SelectedIndex`), `Slider.Value`, `CalendarDatePicker.SelectedDate` (DateTime?). Eventi: `TextChanged`, `IsCheckedChanged`, `ValueChanged`, `SelectionChanged`, `Click`.
- Timer: `new DispatcherTimer { Interval = TimeSpan.FromSeconds(1) }` + `Tick`. Da thread secondario alla UI: `Dispatcher.UIThread.Post(() => ...)` (namespace `Avalonia.Threading`).
- Finestre di messaggio: Avalonia non ha MessageBox: usare `Dialogs.Message(owner, titolo, testo)` (in `src/UI/Dialogs.cs`, da scrivere nel porting UI).
- File: `await StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions { Title = "...", AllowMultiple = false, FileTypeFilter = new[] { new FilePickerFileType("ADIF") { Patterns = new[] { "*.adi", "*.adif" } } } })`,
  percorso con `file.TryGetLocalPath()` (namespace `Avalonia.Platform.Storage`); salvataggio `SaveFilePickerAsync(new FilePickerSaveOptions { SuggestedFileName = "...", DefaultExtension = "docx" })`.
- Aprire un file con il programma predefinito: `Dialogs.OpenWithDefaultApp(path)` (Windows: `Process.Start(new ProcessStartInfo(path) { UseShellExecute = true })`, Mac: `open`, Linux: `xdg-open`).
- Testo selezionabile con parti colorate: `new SelectableTextBlock { FontFamily = Pal.Mono, Inlines = new InlineCollection { new Run("...") { Foreground = ..., FontWeight = FontWeight.Bold }, new LineBreak() } }` (namespace `Avalonia.Controls.Documents`).

## Controlli disegnati (src/Controls) - contratto fra i due porting
Mantengono gli STESSI membri pubblici delle classi WinForms (SkyView.cs, SectionView.cs, Controls.cs, GridMap.cs: GridMapView),
con i tipi Avalonia al posto di quelli WinForms: `Point` (Avalonia) al posto di `System.Drawing.Point` nei metodi
`HitTest(Point)` e `MapToLatLon(Point, out LatLon)`; `Invalidate()` diventa `InvalidateVisual()`; `Color` = `Avalonia.Media.Color`.
In particolare:
- `SkyView`: `Model, Station, Marks (List<RadiantMark>, assegnabile), Selected, ShowHeat, ShowHot, ShowMap, TopView, ShowRadiants, ShowSkyRings, ShowLegend, ShowDial,
  AntennaAz, HpbwDeg, MapRadiusKm, MapLines, MapBorders (List<System.Drawing.PointF[]>), Caption, Prev (List<PrevSpot>)`, metodi `InvalidateHeat()`, `InvalidateMap()`,
  `MapToLatLon(Point, out LatLon)`, `HitTest(Point)`, `static HeatColor(double)`.
- `RadiantMark` (Code, Az, El, Eff, LeftFrac, Zhr, `Track` = `List<System.Drawing.PointF>` (X=az, Y=el), TrackHours), `PrevSpot`, `TrailSeg`.
- `SectionView`: `Model, Trails, AntennaAz, HpbwDeg, LobeElevDeg, Note`.
- `SimpleChart` + `ChartSeries` (Name, Color = Avalonia Color, Values, Bars, RightAxis, LineWidth, Dotted): `Title, YLabel, Y2Label, XLabels, XLabelEvery, Series, YMaxFixed, Y2MaxFixed, MarkIndex`.
- `GridMapView` e `GridQso`, `AdifStore` come in GridMap.cs (AdifStore e' logica pura: va in src/Core/AdifStore.cs).
- NUOVO `TableView` (sostituisce ListView e DataGridView): tabella disegnata, scorrimento con la rotella, intestazione chiara (sfondo quasi bianco, testo nero, come il ListView attuale),
  righe su fondo `Pal.Back`/`Pal.Panel`:
  ```csharp
  public class TableRow { public string[] Cells; public Color? Fore; public Color?[] CellBack; public Color?[] CellFore; public bool Italic; public bool Bold; public double FontSize = 12; public object Tag; }
  public class TableView : Control {
      public List<string> Columns; public List<double> ColumnWidths;   // px; l'ultima colonna puo' riempire
      public List<TableRow> Rows; public int SelectedIndex = -1; public bool Selectable = true;
      public double RowHeight = 20; public double HeaderHeight = 24;
      public event Action<int> RowClicked;   // indice della riga cliccata (dopo aver impostato SelectedIndex)
      public void Refresh();                 // ridisegna e ricalcola lo scorrimento
      public void EnsureVisible(int row);
  }
  ```
