// YA-MS - tabella disegnata (sostituisce ListView e DataGridView del vecchio programma)
// Intestazione chiara (sfondo quasi bianco, testo nero), righe su fondo scuro, colori per riga e per cella,
// riga selezionata evidenziata, scorrimento verticale con la rotellina e indicatore sottile a destra.
using System;
using System.Collections.Generic;
using System.Globalization;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Media;
using Avalonia.Media.Immutable;

namespace YAMS
{
    public class TableRow
    {
        public string[] Cells;
        public Color? Fore;          // colore del testo della riga (null = Pal.Fore)
        public Color?[] CellBack;    // sfondo per cella (null = fondo della riga)
        public Color?[] CellFore;    // colore del testo per cella (null = colore della riga)
        public bool Italic;
        public bool Bold;
        public double FontSize = 12;
        public object Tag;
    }

    public class TableView : Control
    {
        public List<string> Columns = new List<string>();
        public List<double> ColumnWidths = new List<double>();   // px; l'ultima colonna puo' riempire
        public List<TableRow> Rows = new List<TableRow>();
        public int SelectedIndex = -1;
        public bool Selectable = true;
        public double RowHeight = 20;
        public double HeaderHeight = 24;
        public event Action<int> RowClicked;   // indice della riga cliccata (dopo aver impostato SelectedIndex)

        // opzioni in piu' (facoltative)
        public bool StretchLastColumn = true;                  // l'ultima colonna arriva fino al bordo destro
        public List<int> ColumnAlign = new List<int>();        // per colonna: 0 = sinistra, 1 = centro, 2 = destra
        public double HeaderFontSize = 12;

        double scrollY = 0;
        const double DefaultColumnWidth = 80;
        const double CellPad = 5;

        static readonly Color HeaderBack = Color.FromRgb(244, 243, 250);
        static readonly Color HeaderLine = Color.FromRgb(200, 198, 215);
        static readonly Color HeaderFore = Color.FromRgb(0, 0, 0);

        public TableView()
        {
            ClipToBounds = true;
            Focusable = true;
        }

        // ridisegna e ricalcola lo scorrimento
        public void Refresh()
        {
            ClampScroll();
            InvalidateMeasure();
            InvalidateVisual();
        }

        public void EnsureVisible(int row)
        {
            if (Rows == null || row < 0 || row >= Rows.Count) return;
            double body = BodyHeight();
            double top = row * RowHeight, bottom = top + RowHeight;
            if (top < scrollY) scrollY = top;
            else if (bottom > scrollY + body) scrollY = bottom - body;
            ClampScroll();
            InvalidateVisual();
        }

        double BodyHeight() { return Math.Max(0, Bounds.Height - HeaderHeight); }

        double ContentHeight() { return (Rows != null ? Rows.Count : 0) * RowHeight; }

        double MaxScroll() { return Math.Max(0, ContentHeight() - BodyHeight()); }

        void ClampScroll()
        {
            double m = MaxScroll();
            if (scrollY > m) scrollY = m;
            if (scrollY < 0) scrollY = 0;
        }

        int ColumnCount()
        {
            int n = Columns != null ? Columns.Count : 0;
            if (Rows != null) foreach (TableRow r in Rows) if (r != null && r.Cells != null) n = Math.Max(n, r.Cells.Length);
            return n;
        }

        // larghezze effettive delle colonne (l'ultima puo' riempire lo spazio rimasto)
        double[] Widths(double total)
        {
            int n = ColumnCount();
            double[] w = new double[n];
            double sum = 0;
            for (int i = 0; i < n; i++)
            {
                w[i] = ColumnWidths != null && i < ColumnWidths.Count && ColumnWidths[i] > 0 ? ColumnWidths[i] : DefaultColumnWidth;
                sum += w[i];
            }
            if (StretchLastColumn && n > 0 && sum < total) w[n - 1] += total - sum;
            return w;
        }

        protected override Size MeasureOverride(Size availableSize)
        {
            double[] w = Widths(0);
            double sw = 0; foreach (double x in w) sw += x;
            double h = HeaderHeight + ContentHeight();
            if (!double.IsInfinity(availableSize.Width)) sw = Math.Min(sw, availableSize.Width);
            if (!double.IsInfinity(availableSize.Height)) h = Math.Min(h, availableSize.Height);
            return new Size(sw, h);
        }

        static FormattedText Ft(string s, double size, Color c, bool bold, bool italic)
        {
            return new FormattedText(s ?? "", CultureInfo.CurrentCulture, FlowDirection.LeftToRight,
                new Typeface(FontFamily.Default, italic ? FontStyle.Italic : FontStyle.Normal, bold ? FontWeight.Bold : FontWeight.Normal),
                size, new ImmutableSolidColorBrush(c));
        }

        int Align(int col) { return ColumnAlign != null && col < ColumnAlign.Count ? ColumnAlign[col] : 0; }

        void DrawCellText(DrawingContext ctx, FormattedText ft, Rect cell, int align)
        {
            double x;
            if (align == 1) x = cell.X + (cell.Width - ft.Width) / 2;
            else if (align == 2) x = cell.Right - CellPad - ft.Width;
            else x = cell.X + CellPad;
            if (align != 0 && x < cell.X + 1) x = cell.X + 1;
            double y = cell.Y + (cell.Height - ft.Height) / 2;
            using (ctx.PushClip(cell))
                ctx.DrawText(ft, new Point(x, y));
        }

        public override void Render(DrawingContext ctx)
        {
            double Wd = Bounds.Width, Ht = Bounds.Height;
            ctx.DrawRectangle(Pal.B(Pal.Back), null, new Rect(0, 0, Wd, Ht));
            if (Wd < 2 || Ht < 2) return;
            ClampScroll();
            double[] w = Widths(Wd);
            int n = w.Length;

            // righe
            double bodyTop = HeaderHeight, bodyH = Math.Max(0, Ht - HeaderHeight);
            if (Rows != null && Rows.Count > 0 && bodyH > 0)
            {
                using (ctx.PushClip(new Rect(0, bodyTop, Wd, bodyH)))
                {
                    int first = Math.Max(0, (int)Math.Floor(scrollY / RowHeight));
                    int last = Math.Min(Rows.Count - 1, (int)Math.Ceiling((scrollY + bodyH) / RowHeight));
                    IBrush odd = Pal.B(Pal.Panel);
                    IBrush selB = Pal.B(Pal.Panel3);
                    IPen selP = Pal.P(Pal.Azure, 1);
                    for (int r = first; r <= last; r++)
                    {
                        TableRow row = Rows[r];
                        if (row == null) continue;
                        double y = bodyTop + r * RowHeight - scrollY;
                        Rect rr = new Rect(0, y, Wd, RowHeight);
                        bool sel = Selectable && r == SelectedIndex;
                        if (sel) ctx.DrawRectangle(selB, null, rr);
                        else if (r % 2 == 1) ctx.DrawRectangle(odd, null, rr);
                        double x = 0;
                        Color rowFore = row.Fore ?? Pal.Fore;
                        double fs = row.FontSize > 0 ? row.FontSize : 12;
                        for (int c = 0; c < n; c++)
                        {
                            Rect cell = new Rect(x, y, w[c], RowHeight);
                            x += w[c];
                            if (row.CellBack != null && c < row.CellBack.Length && row.CellBack[c].HasValue)
                                ctx.DrawRectangle(Pal.B(row.CellBack[c].Value), null, new Rect(cell.X + 1, cell.Y + 1, Math.Max(0, cell.Width - 2), Math.Max(0, cell.Height - 2)));
                            if (row.Cells == null || c >= row.Cells.Length || string.IsNullOrEmpty(row.Cells[c])) continue;
                            Color fc = row.CellFore != null && c < row.CellFore.Length && row.CellFore[c].HasValue ? row.CellFore[c].Value : rowFore;
                            DrawCellText(ctx, Ft(row.Cells[c], fs, fc, row.Bold, row.Italic), cell, Align(c));
                        }
                        if (sel) ctx.DrawRectangle(null, selP, new Rect(0.5, y + 0.5, Math.Max(0, Wd - 1), Math.Max(0, RowHeight - 1)));
                    }
                }
                // indicatore di scorrimento
                double ch = ContentHeight();
                if (ch > bodyH + 0.5)
                {
                    double th = Math.Max(20, bodyH * bodyH / ch);
                    double ty = bodyTop + (bodyH - th) * (scrollY / Math.Max(1, ch - bodyH));
                    ctx.DrawRectangle(Pal.B(Pal.A(60, Pal.Muted)), null, new Rect(Wd - 5, bodyTop, 4, bodyH), 2, 2);
                    ctx.DrawRectangle(Pal.B(Pal.A(190, Pal.Muted)), null, new Rect(Wd - 5, ty, 4, th), 2, 2);
                }
            }

            // intestazione
            if (HeaderHeight > 0)
            {
                ctx.DrawRectangle(Pal.B(HeaderBack), null, new Rect(0, 0, Wd, HeaderHeight));
                IPen hl = Pal.P(HeaderLine, 1);
                double x = 0;
                for (int c = 0; c < n; c++)
                {
                    Rect cell = new Rect(x, 0, w[c], HeaderHeight);
                    x += w[c];
                    if (Columns != null && c < Columns.Count && !string.IsNullOrEmpty(Columns[c]))
                        DrawCellText(ctx, Ft(Columns[c], HeaderFontSize, HeaderFore, false, false), cell, Align(c));
                    if (c < n - 1) ctx.DrawLine(hl, new Point(Math.Round(x) - 0.5, 4), new Point(Math.Round(x) - 0.5, HeaderHeight - 4));
                }
                ctx.DrawLine(hl, new Point(0, HeaderHeight - 0.5), new Point(Wd, HeaderHeight - 0.5));
            }
        }

        protected override void OnPointerWheelChanged(PointerWheelEventArgs e)
        {
            base.OnPointerWheelChanged(e);
            double m = MaxScroll();
            if (m <= 0 || e.Delta.Y == 0) return;   // niente da scorrere: la rotellina passa al contenitore
            double old = scrollY;
            scrollY -= e.Delta.Y * RowHeight * 3;
            ClampScroll();
            if (scrollY != old) { e.Handled = true; InvalidateVisual(); }
        }

        protected override void OnPointerPressed(PointerPressedEventArgs e)
        {
            base.OnPointerPressed(e);
            if (!e.GetCurrentPoint(this).Properties.IsLeftButtonPressed) return;
            Point p = e.GetPosition(this);
            if (p.Y < HeaderHeight || Rows == null) return;
            int idx = (int)Math.Floor((p.Y - HeaderHeight + scrollY) / RowHeight);
            if (idx < 0 || idx >= Rows.Count) return;
            if (Selectable) SelectedIndex = idx;
            InvalidateVisual();
            e.Handled = true;
            RowClicked?.Invoke(idx);
        }
    }
}
