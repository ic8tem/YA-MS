// YA-MS - volta celeste con mappa d'Europa, Hot A/B, miglior puntamento e legenda dei colori
//
// Due scale radiali sovrapposte, con lo stesso azimut:
//  - cielo: zenit al centro, orizzonte sul bordo (cerchi = elevazione del radiante);
//  - mappa: proiezione azimutale equidistante centrata sulla stazione, bordo = MapRadiusKm.
// Vista dall'alto (E a destra) come una mappa e come il rotore d'antenna; con la vista dal basso
// (E a sinistra, come swan.ms) la mappa non viene disegnata perche' risulterebbe specchiata.
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Runtime.InteropServices;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Media.Imaging;
using Avalonia.Media.Immutable;
using Avalonia.Platform;

namespace YAMS
{
    // Punto di riflessione previsto (zona PREV in pianta): posizione alla quota delle scie e peso ZHR x contributo
    public class PrevSpot
    {
        public LatLon Pos;
        public double W;
        public bool Left;   // lato A (sinistra della tratta)
    }

    public class SkyView : Control
    {
        public PathModel Model;
        public LatLon Station;
        public List<RadiantMark> Marks = new List<RadiantMark>();
        public string Selected;
        public bool ShowHeat = false, ShowHot = true, ShowMap = true, TopView = true;
        public double AntennaAz = 0, HpbwDeg = 0;   // lobo d'antenna (HPBW = 0: non disegnato)
        public double MapRadiusKm = 2600;
        public List<System.Drawing.PointF[]> MapLines = new List<System.Drawing.PointF[]>();     // coste (lon, lat)
        public List<System.Drawing.PointF[]> MapBorders = new List<System.Drawing.PointF[]>();   // confini (lon, lat)
        public string Caption = "";
        // pianta: senza radianti e senza cerchi di elevazione, con la scala dei gradi; cielo piccolo: senza legenda
        public bool ShowRadiants = true, ShowSkyRings = true, ShowLegend = true, ShowDial = false;
        public List<PrevSpot> Prev = new List<PrevSpot>();   // zone PREV (punti di riflessione piu' probabili)

        WriteableBitmap heat; PathModel heatFor; bool heatTop;

        // colori di sistema usati dal vecchio programma
        static readonly Color Gainsboro = Color.FromRgb(220, 220, 220);
        static readonly Color White = Color.FromRgb(255, 255, 255);
        static readonly Color Wheat = Color.FromRgb(245, 222, 179);
        static readonly Color Cyan = Color.FromRgb(0, 255, 255);
        static readonly Color LightCyan = Color.FromRgb(224, 255, 255);

        // dimensioni dei caratteri (1 pt WinForms ~ 1.33 px)
        const double F7 = 9.3, F75 = 10, F8 = 10.7, F85 = 11.3, F9 = 12, F12 = 16;

        public SkyView()
        {
            ClipToBounds = true;
        }

        public void InvalidateHeat() { heatFor = null; InvalidateVisual(); }

        void Geom(out double cx, out double cy, out double rad)
        {
            double W = Bounds.Width, H = Bounds.Height;
            double w = ShowLegend ? W - 120 : W;   // spazio a destra per la legenda
            double s = Math.Min(w, H);
            rad = s / 2.0 - (ShowDial ? 40.0 : (ShowLegend ? 34.0 : 22.0)); if (rad < 20) rad = 20;
            cx = w / 2.0; cy = H / 2.0;
        }

        double Sgn { get { return TopView ? 1.0 : -1.0; } }

        Point SkyXY(double az, double el, double cx, double cy, double rad)
        {
            double r = rad * (90.0 - el) / 90.0, a = az * Astro.D2R;
            return new Point(cx + Sgn * r * Math.Sin(a), cy - r * Math.Cos(a));
        }

        Point MapXY(LatLon p, double cx, double cy, double rad)
        {
            double d = Astro.DistanceKm(Station, p), b = Astro.Bearing(Station, p) * Astro.D2R;
            double r = rad * d / MapRadiusKm;
            return new Point(cx + Sgn * r * Math.Sin(b), cy - r * Math.Cos(b));
        }

        public static Color HeatColor(double eff)
        {
            // 0 % = trasparente (resta il blu del cielo), circa 50 % = verde acqua, 100 % = giallo
            double t = Math.Max(0, Math.Min(1, eff / 100.0));
            int a = (int)(170 * Math.Pow(t, 0.8));
            int r = (int)(255 * Math.Max(0, (t - 0.45) / 0.55));
            int g = (int)(120 + 135 * t);
            int b = (int)(200 * (1 - t));
            return Color.FromArgb((byte)Math.Min(255, a), (byte)Math.Min(255, r), (byte)Math.Min(255, g), (byte)Math.Max(0, b));
        }

        void BuildHeat(int size)
        {
            if (heat != null) heat.Dispose();
            heat = new WriteableBitmap(new PixelSize(size, size), new Vector(96, 96), PixelFormat.Bgra8888, AlphaFormat.Premul);
            heatFor = Model; heatTop = TopView;
            int[] buf = new int[size * size];
            if (Model != null && Model.Valid)
            {
                double c = size / 2.0, rad = size / 2.0;
                for (int y = 0; y < size; y++)
                    for (int x = 0; x < size; x++)
                    {
                        double dx = x + 0.5 - c, dy = y + 0.5 - c;
                        double rr = Math.Sqrt(dx * dx + dy * dy);
                        if (rr > rad) continue;
                        double el = 90.0 - 90.0 * rr / rad;
                        double az = Astro.Norm360(Math.Atan2(Sgn * dx, -dy) / Astro.D2R);
                        double lf;
                        double eff = Model.Efficiency(Astro.FromAltAz(Station, az, el), out lf);
                        if (eff > 1)
                        {
                            Color hc = HeatColor(eff);
                            int a = hc.A;
                            int r = hc.R * a / 255, g = hc.G * a / 255, b = hc.B * a / 255;   // alfa premoltiplicato
                            buf[y * size + x] = (a << 24) | (r << 16) | (g << 8) | b;
                        }
                    }
            }
            using (ILockedFramebuffer fb = heat.Lock())
            {
                for (int y = 0; y < size; y++)
                    Marshal.Copy(buf, y * size, fb.Address + y * fb.RowBytes, size);
            }
        }

        // ---------- testo ----------
        static FormattedText Ft(string s, double size, Color c, FontWeight w = FontWeight.Normal)
        {
            return new FormattedText(s ?? "", CultureInfo.CurrentCulture, FlowDirection.LeftToRight,
                new Typeface(FontFamily.Default, FontStyle.Normal, w), size, new ImmutableSolidColorBrush(c));
        }

        static void Txt(DrawingContext ctx, string s, double size, Color c, double x, double y, FontWeight w = FontWeight.Normal)
        {
            ctx.DrawText(Ft(s, size, c, w), new Point(x, y));
        }

        static IPen RoundPen(Color c, double w)
        {
            return new ImmutablePen(new ImmutableSolidColorBrush(c), w, null, PenLineCap.Round, PenLineJoin.Round);
        }

        public override void Render(DrawingContext ctx)
        {
            double W = Bounds.Width, H = Bounds.Height;
            ctx.DrawRectangle(Pal.B(Pal.Back), null, new Rect(0, 0, W, H));
            if (W < 10 || H < 10) return;
            double cx, cy, rad; Geom(out cx, out cy, out rad);
            Rect dome = new Rect(cx - rad, cy - rad, 2 * rad, 2 * rad);
            bool map = ShowMap && TopView;

            RadialGradientBrush pb = new RadialGradientBrush();
            pb.GradientStops.Add(new GradientStop(map ? Color.FromRgb(22, 36, 110) : Color.FromRgb(32, 52, 160), 0));
            pb.GradientStops.Add(new GradientStop(Color.FromRgb(8, 12, 48), 1));
            ctx.DrawEllipse(pb, null, dome);
            if (map)
            {
                using (ctx.PushGeometryClip(new EllipseGeometry(dome)))
                    DrawMap(ctx, cx, cy, rad);
            }
            if (ShowHeat && Model != null && Model.Valid)
            {
                if (heatFor != Model || heat == null || heatTop != TopView) BuildHeat(240);
                if (map)
                {
                    using (ctx.PushOpacity(0.72))
                        ctx.DrawImage(heat, dome);
                }
                else ctx.DrawImage(heat, dome);
            }

            IPen ring = Pal.P(Pal.Argb(130, 220, 220, 230), 1);
            IPen dash = Pal.P(Pal.Argb(80, 220, 220, 230), 1, Pal.Dash);
            Color tc = Pal.Argb(200, 230, 230, 230);
            if (!map || ShowSkyRings)
                for (int el = 0; el < 90; el += 10)
                {
                    double r = rad * (90 - el) / 90.0;
                    ctx.DrawEllipse(null, el % 20 == 0 ? ring : dash, new Point(cx, cy), r, r);
                    if (el % 20 == 0 && el > 0) Txt(ctx, el + "°", ShowLegend || map ? F8 : F7, tc, cx + 2, cy - r - 1);
                }
            if (map && ShowDial) DrawDial(ctx, cx, cy, rad);
            ctx.DrawLine(dash, new Point(cx - rad, cy), new Point(cx + rad, cy));
            ctx.DrawLine(dash, new Point(cx, cy - rad), new Point(cx, cy + rad));
            if (map)
                Txt(ctx, "mappa: bordo = " + MapRadiusKm.ToString("F0") + " km dalla stazione", F8, tc, 6, 6);   // in alto a sinistra: non copre la didascalia

            if (!(map && ShowDial))
            {
                double fs = ShowLegend || map ? F12 : F9;
                Color oc = Color.FromRgb(240, 90, 40);
                FormattedText n = Ft("N", fs, oc), s = Ft("S", fs, oc);
                FormattedText w = Ft(TopView ? "W" : "E", fs, oc), e = Ft(TopView ? "E" : "W", fs, oc);
                ctx.DrawText(n, new Point(cx - n.Width / 2, cy - rad - n.Height - 4));
                ctx.DrawText(s, new Point(cx - s.Width / 2, cy + rad + 4));
                ctx.DrawText(w, new Point(cx - rad - w.Width - 8, cy - w.Height / 2));
                ctx.DrawText(e, new Point(cx + rad + 8, cy - e.Height / 2));
            }

            DrawLobe(ctx, cx, cy, rad);
            if (map) DrawPrev(ctx, cx, cy, rad);
            if (Model != null && Model.Valid) DrawPath(ctx, cx, cy, rad, map);
            if (map) DrawFlow(ctx, cx, cy, rad); else DrawBestPointing(ctx, cx, cy, rad);
            if (ShowRadiants || !map) DrawRadiants(ctx, cx, cy, rad);
            if (ShowLegend) DrawSymbolLegend(ctx, cx + rad + 44, cy - rad);
            if (!string.IsNullOrEmpty(Caption))
            {
                FormattedText ft = Ft(Caption, F85, Pal.Silver);
                ctx.DrawText(ft, new Point(6, H - ft.Height - 4));
            }
        }

        void DrawMap(DrawingContext ctx, double cx, double cy, double rad)
        {
            EnsureMapGeometry(cx, cy, rad);
            IPen coast = Pal.P(Pal.Argb(200, 120, 170, 200), 1.1);
            IPen border = Pal.P(Pal.Argb(120, 120, 140, 170), 0.8, Pal.Dot);
            if (borderGeo != null) ctx.DrawGeometry(null, border, borderGeo);
            if (coastGeo != null) ctx.DrawGeometry(null, coast, coastGeo);
            IPen dr = Pal.P(Pal.Argb(60, 255, 200, 120), 1, Pal.DashDot);
            Color lc = Pal.Argb(150, 255, 200, 120);
            for (int km = 500; km < MapRadiusKm; km += 500)
            {
                double r = rad * km / MapRadiusKm;
                ctx.DrawEllipse(null, dr, new Point(cx, cy), r, r);
                Txt(ctx, km + " km", F7, lc, cx + 2, cy + r - 13);
            }
        }

        // proiezione delle linee della mappa in coordinate normalizzate (raggio 1 = MapRadiusKm), rifatta solo se cambia
        // la stazione (o la vista, o i dati); la geometria in pixel si rifa' solo se cambiano anche centro o raggio
        List<Point[]> projCoast = new List<Point[]>(), projBorders = new List<Point[]>();
        LatLon projFor; bool projTop; int projCount = -1; double projRadiusKm;
        List<System.Drawing.PointF[]> projLinesRef, projBordersRef;
        StreamGeometry coastGeo, borderGeo;
        double geoCx = double.NaN, geoCy, geoRad;

        List<Point[]> Project(List<System.Drawing.PointF[]> lines)
        {
            List<Point[]> outl = new List<Point[]>();
            if (lines == null) return outl;
            double maxDeg = (MapRadiusKm + 300) / 111.0;
            List<Point> cur = new List<Point>();
            foreach (System.Drawing.PointF[] line in lines)
            {
                cur.Clear();
                if (line == null) continue;
                for (int i = 0; i < line.Length; i++)
                {
                    LatLon q = new LatLon(line[i].Y, line[i].X);
                    bool ok = Math.Abs(q.Lat - Station.Lat) <= maxDeg;
                    double d = ok ? Astro.DistanceKm(Station, q) : 0;
                    if (!ok || d > MapRadiusKm + 200) { if (cur.Count > 1) outl.Add(cur.ToArray()); cur.Clear(); continue; }
                    double r = d / MapRadiusKm, b = Astro.Bearing(Station, q) * Astro.D2R;
                    cur.Add(new Point(Sgn * r * Math.Sin(b), -r * Math.Cos(b)));
                }
                if (cur.Count > 1) outl.Add(cur.ToArray());
            }
            return outl;
        }

        public void InvalidateMap() { projCount = -1; coastGeo = null; borderGeo = null; InvalidateVisual(); }

        void EnsureMapGeometry(double cx, double cy, double rad)
        {
            int cnt = (MapLines != null ? MapLines.Count : 0) + (MapBorders != null ? MapBorders.Count : 0);
            if (projCount != cnt || projFor.Lat != Station.Lat || projFor.Lon != Station.Lon || projTop != TopView
                || projRadiusKm != MapRadiusKm || !ReferenceEquals(projLinesRef, MapLines) || !ReferenceEquals(projBordersRef, MapBorders))
            {
                projCoast = Project(MapLines); projBorders = Project(MapBorders);
                projFor = Station; projTop = TopView; projCount = cnt; projRadiusKm = MapRadiusKm;
                projLinesRef = MapLines; projBordersRef = MapBorders;
                coastGeo = null; borderGeo = null;
            }
            if (coastGeo == null || borderGeo == null || geoCx != cx || geoCy != cy || geoRad != rad)
            {
                coastGeo = BuildGeo(projCoast, cx, cy, rad);
                borderGeo = BuildGeo(projBorders, cx, cy, rad);
                geoCx = cx; geoCy = cy; geoRad = rad;
            }
        }

        static StreamGeometry BuildGeo(List<Point[]> lines, double cx, double cy, double rad)
        {
            StreamGeometry g = new StreamGeometry();
            using (StreamGeometryContext c = g.Open())
            {
                foreach (Point[] line in lines)
                {
                    if (line.Length < 2) continue;
                    c.BeginFigure(new Point(cx + rad * line[0].X, cy + rad * line[0].Y), false);
                    for (int i = 1; i < line.Length; i++) c.LineTo(new Point(cx + rad * line[i].X, cy + rad * line[i].Y));
                    c.EndFigure(false);
                }
            }
            return g;
        }

        static Color HotColor(HotPoint h)
        {
            // rosso = consigliato dall'efficienza, grigio = gia' nel lobo, rosa = fuori dal lobo
            return h.Recommended ? Pal.Red : h.InLobe ? Pal.HotGrey : Pal.HotPink;
        }

        void DrawPath(DrawingContext ctx, double cx, double cy, double rad, bool map)
        {
            IPen pp = Pal.P(Pal.A(230, Pal.Green), 2);
            IBrush gb = Pal.B(Pal.Green);
            if (map)
            {
                Point pd = MapXY(Model.Dx, cx, cy, rad);
                ctx.DrawLine(pp, new Point(cx, cy), pd);
                ctx.DrawEllipse(gb, null, pd, 4, 4);
                Txt(ctx, "DX", F85, Pal.Green, pd.X + 5, pd.Y - 9, FontWeight.Bold);
                Point pm = MapXY(Model.Mid, cx, cy, rad);
                ctx.DrawEllipse(null, Pal.P(Pal.Green, 1), pm, 3, 3);
                DrawCommonZone(ctx, cx, cy, rad);
            }
            else
            {
                Point p = SkyXY(Model.BearingHomeToDx, 0, cx, cy, rad);
                ctx.DrawLine(pp, new Point(cx, cy), p);
            }
            ctx.DrawEllipse(Pal.B(White), null, new Point(cx, cy), 3, 3);
            if (!ShowHot) return;
            HotPoint[] hs = { Model.HotA, Model.HotB };
            foreach (HotPoint h in hs)
            {
                if (h == null) continue;
                Color hc = HotColor(h);
                IPen hp = Pal.P(Pal.A(220, hc), 1.5, Pal.Dash);
                Point rim = SkyXY(h.BearingFromHome, 0, cx, cy, rad);
                ctx.DrawLine(hp, new Point(cx, cy), rim);
                string lab = (h.Label ?? "").Replace("Hot ", "");
                if (map)
                {
                    Point p = MapXY(h.Pos, cx, cy, rad);
                    ctx.DrawEllipse(Pal.B(hc), null, p, 5, 5);
                    Txt(ctx, "Hot " + lab, F85, hc, p.X + 6, p.Y - 9, FontWeight.Bold);
                }
                else
                {
                    FormattedText ft = Ft(lab, F85, hc, FontWeight.Bold);
                    // etichetta appena fuori dal bordo, lungo la direzione
                    double a = h.BearingFromHome * Astro.D2R;
                    double lx = cx + Sgn * (rad + 9) * Math.Sin(a), ly = cy - (rad + 9) * Math.Cos(a);
                    ctx.DrawText(ft, new Point(lx - ft.Width / 2, ly - ft.Height / 2));
                }
            }
        }

        // Zona dello strato E vista da entrambe le stazioni (articolo): due cerchi di raggio pari alla portata
        // alla quota delle scie, attorno alla stazione e al corrispondente; i loro incroci sono i Limiti A e B
        void DrawCommonZone(DrawingContext ctx, double cx, double cy, double rad)
        {
            if (Model.HotRadiusKm <= 0) return;
            Color lc = Color.FromRgb(150, 150, 210);
            IPen zp = Pal.P(Pal.A(110, lc), 1, Pal.Dot);
            foreach (LatLon c in new LatLon[] { Station, Model.Dx })
            {
                StreamGeometry g = new StreamGeometry();
                using (StreamGeometryContext gc = g.Open())
                {
                    gc.BeginFigure(MapXY(Astro.Destination(c, 0, Model.HotRadiusKm), cx, cy, rad), false);
                    for (int i = 1; i <= 72; i++) gc.LineTo(MapXY(Astro.Destination(c, i * 5, Model.HotRadiusKm), cx, cy, rad));
                    gc.EndFigure(false);
                }
                ctx.DrawGeometry(null, zp, g);
            }
            IPen lp = Pal.P(lc, 1.3);
            foreach (HotPoint h in new HotPoint[] { Model.LimitA, Model.LimitB })
            {
                if (h == null) continue;
                Point p = MapXY(h.Pos, cx, cy, rad);
                ctx.DrawEllipse(null, lp, p, 4, 4);
                Txt(ctx, (h.Label ?? "").Replace("Limite", "lim."), F75, lc, p.X + 6, p.Y - 7);
            }
        }

        // Lobo principale dell'antenna: settore di +-HPBW/2 attorno al puntamento
        void DrawLobe(DrawingContext ctx, double cx, double cy, double rad)
        {
            if (HpbwDeg <= 0) return;
            StreamGeometry g = new StreamGeometry();
            using (StreamGeometryContext gc = g.Open())
            {
                gc.BeginFigure(new Point(cx, cy), true);
                for (double a = -HpbwDeg / 2; a <= HpbwDeg / 2 + 0.01; a += Math.Max(0.5, HpbwDeg / 40))
                    gc.LineTo(SkyXY(AntennaAz + a, 0, cx, cy, rad));
                gc.EndFigure(true);
            }
            ctx.DrawGeometry(Pal.B(Pal.Argb(45, 255, 240, 200)), Pal.P(Pal.Argb(140, 255, 240, 200), 1), g);
            Point t = SkyXY(AntennaAz, 2, cx, cy, rad);
            Txt(ctx, "lobo " + HpbwDeg.ToString("F0") + "°", F8, Wheat, t.X + 4, t.Y);
        }

        // Da un punto del controllo alla posizione geografica (proiezione azimutale equidistante inversa)
        public bool MapToLatLon(Point pt, out LatLon p)
        {
            p = new LatLon();
            double cx, cy, rad; Geom(out cx, out cy, out rad);
            double dx = pt.X - cx, dy = pt.Y - cy;
            double r = Math.Sqrt(dx * dx + dy * dy) / rad;
            if (r > 1 || !TopView) return false;
            double brg = Astro.Norm360(Math.Atan2(Sgn * dx, -dy) / Astro.D2R);
            p = Astro.Destination(Station, brg, r * MapRadiusKm);
            return true;
        }

        // Miglior puntamento: ortogonale alla direzione di arrivo dello sciame selezionato
        void DrawBestPointing(DrawingContext ctx, double cx, double cy, double rad)
        {
            RadiantMark m = null;
            if (Marks != null) foreach (RadiantMark x in Marks) if (x.Code == Selected) m = x;
            if (m == null || m.El <= 0) return;
            Point a = SkyXY(m.Az + 90, 0, cx, cy, rad), b = SkyXY(m.Az - 90, 0, cx, cy, rad);
            IPen p = Pal.P(Pal.A(230, Pal.Orange), 2.5);
            IPen w = Pal.P(Pal.A(70, Pal.Orange), 1);
            Color tc = Color.FromRgb(255, 170, 60);
            ctx.DrawLine(p, a, b);
            // tolleranza +-45° (SM6FHZ: +-40-50°)
            foreach (double off in new double[] { 45, -45 })
            {
                Point a2 = SkyXY(m.Az + 90 + off, 0, cx, cy, rad), b2 = SkyXY(m.Az - 90 + off, 0, cx, cy, rad);
                ctx.DrawLine(w, a2, b2);
            }
            Txt(ctx, Astro.Norm360(m.Az + 90).ToString("F0") + "°", F85, tc, a.X + 3, a.Y - 16, FontWeight.Bold);
            Txt(ctx, Astro.Norm360(m.Az - 90).ToString("F0") + "°", F85, tc, b.X + 3, b.Y - 16, FontWeight.Bold);
            // direzione di arrivo dello sciame: linea a puntini con freccia verso il centro
            Point r = SkyXY(m.Az, 0, cx, cy, rad);
            Color dc = Pal.A(150, Pal.Orange);
            ctx.DrawLine(Pal.P(dc, 1, Pal.Dot), r, new Point(cx, cy));
            double vx = cx - r.X, vy = cy - r.Y, len = Math.Sqrt(vx * vx + vy * vy);
            if (len > 1)
            {
                vx /= len; vy /= len;
                Point tip = new Point(cx, cy);
                Point bl = new Point(cx - 9 * vx + 4 * vy, cy - 9 * vy - 4 * vx);
                Point br = new Point(cx - 9 * vx - 4 * vy, cy - 9 * vy + 4 * vx);
                StreamGeometry g = new StreamGeometry();
                using (StreamGeometryContext gc = g.Open())
                {
                    gc.BeginFigure(tip, true); gc.LineTo(bl); gc.LineTo(br); gc.EndFigure(true);
                }
                ctx.DrawGeometry(Pal.B(dc), null, g);
            }
        }

        // Scala dei gradi attorno al bordo della mappa (come il rotore d'antenna)
        void DrawDial(DrawingContext ctx, double cx, double cy, double rad)
        {
            IPen tk = Pal.P(Pal.Argb(150, 200, 200, 210), 1);
            IPen rim = Pal.P(Pal.Argb(170, 200, 200, 210), 1.5);
            Color oc = Color.FromRgb(240, 120, 60);
            ctx.DrawEllipse(null, rim, new Point(cx, cy), rad + 3, rad + 3);
            for (int a = 0; a < 360; a += 5)
            {
                double ar = a * Astro.D2R;
                double l = a % 30 == 0 ? 9 : (a % 10 == 0 ? 6 : 3);
                double sx = Sgn * Math.Sin(ar), sy = -Math.Cos(ar);
                ctx.DrawLine(tk, new Point(cx + (rad + 3) * sx, cy + (rad + 3) * sy), new Point(cx + (rad + 3 + l) * sx, cy + (rad + 3 + l) * sy));
                if (a % 30 == 0)
                {
                    FormattedText ft = Ft(a.ToString(), F9, oc);
                    ctx.DrawText(ft, new Point(cx + (rad + 24) * sx - ft.Width / 2, cy + (rad + 24) * sy - ft.Height / 2));
                }
            }
        }

        // Zone PREV: dove cadono le scie piu' probabili (per ciascun lato della tratta un'ellisse
        // con centro e assi dati dalla media e dalla dispersione pesata dei punti di riflessione)
        void DrawPrev(DrawingContext ctx, double cx, double cy, double rad)
        {
            if (Prev == null || Prev.Count == 0) return;
            double tot = 0; foreach (PrevSpot sp in Prev) tot += sp.W;
            if (tot <= 0) return;
            foreach (bool left in new bool[] { true, false })
            {
                double sw = 0, mx = 0, my = 0;
                List<Point> pts = new List<Point>(); List<double> ws = new List<double>();
                foreach (PrevSpot sp in Prev)
                {
                    if (sp.Left != left || sp.W <= 0) continue;
                    Point p = MapXY(sp.Pos, cx, cy, rad);
                    pts.Add(p); ws.Add(sp.W);
                    sw += sp.W; mx += sp.W * p.X; my += sp.W * p.Y;
                }
                if (sw < 0.05 * tot || pts.Count < 3) continue;
                mx /= sw; my /= sw;
                double sxx = 0, syy = 0, sxy = 0;
                for (int i = 0; i < pts.Count; i++)
                {
                    double dx = pts[i].X - mx, dy = pts[i].Y - my;
                    sxx += ws[i] * dx * dx; syy += ws[i] * dy * dy; sxy += ws[i] * dx * dy;
                }
                sxx /= sw; syy /= sw; sxy /= sw;
                // autovalori e direzione dell'asse maggiore della matrice di covarianza
                double tr = sxx + syy, det = sxx * syy - sxy * sxy;
                double disc = Math.Sqrt(Math.Max(0, tr * tr / 4 - det));
                double l1 = tr / 2 + disc, l2 = Math.Max(0, tr / 2 - disc);
                double ang = 0.5 * Math.Atan2(2 * sxy, sxx - syy);   // radianti
                double a1 = Math.Max(6, 2 * Math.Sqrt(l1)), a2 = Math.Max(5, 2 * Math.Sqrt(l2));
                using (ctx.PushTransform(Matrix.CreateRotation(ang) * Matrix.CreateTranslation(mx, my)))
                {
                    ctx.DrawEllipse(Pal.B(Pal.Argb(95, 235, 225, 190)), Pal.P(Pal.Argb(170, 245, 235, 200), 1.2), new Point(0, 0), a1, a2);
                }
                string lab = "PREV " + (left ? "A" : "B") + " " + (100 * sw / tot).ToString("F0") + "%";
                Txt(ctx, lab, F85, Color.FromRgb(250, 240, 210), mx - 30, my - 9, FontWeight.Bold);
            }
        }

        // Direzione di scorrimento dello sciame (linea gialla per la stazione, lungo l'azimut del radiante):
        // le riflessioni migliori stanno ai due lati, in direzione ortogonale (punti arancioni sul bordo)
        void DrawFlow(DrawingContext ctx, double cx, double cy, double rad)
        {
            RadiantMark m = FlowMark();
            if (m == null) return;
            Point a = SkyXY(m.Az, 0, cx, cy, rad), b = SkyXY(m.Az + 180, 0, cx, cy, rad);
            ctx.DrawLine(Pal.P(Pal.Argb(200, 120, 90, 20), 6), a, b);
            ctx.DrawLine(Pal.P(Pal.Argb(240, 255, 210, 90), 2.5), a, b);
            Txt(ctx, m.Code + " (dal radiante, az. " + m.Az.ToString("F0") + "°)", F85, Color.FromRgb(255, 220, 110), a.X + 6, a.Y + 4, FontWeight.Bold);
            IBrush ob = Pal.B(Pal.Orange);
            foreach (double off in new double[] { 90, -90 })
            {
                Point q = SkyXY(m.Az + off, 0, cx, cy, rad);
                ctx.DrawEllipse(ob, null, q, 5, 5);
                Txt(ctx, Astro.Norm360(m.Az + off).ToString("F0") + "°", F85, Pal.Orange, q.X + 6, q.Y - 18, FontWeight.Bold);
            }
        }

        // Sciame per la linea di scorrimento: quello selezionato, altrimenti il piu' favorevole (ZHR x efficienza)
        RadiantMark FlowMark()
        {
            RadiantMark best = null; double bs = 0;
            if (Marks == null) return null;
            foreach (RadiantMark x in Marks)
            {
                if (x.El <= 0) continue;
                if (x.Code == Selected) return x;
                double sc = x.Zhr * x.Eff;
                if (sc > bs) { bs = sc; best = x; }
            }
            return best;
        }

        void DrawRadiants(DrawingContext ctx, double cx, double cy, double rad)
        {
            if (Marks == null) return;
            IBrush cyan = Pal.B(Cyan);
            foreach (RadiantMark m in Marks)
            {
                if (m.Track == null) continue;
                bool sel = m.Code == Selected;
                IPen tp = RoundPen(sel ? Pal.A(240, Pal.Azure) : Pal.A(140, Pal.Azure), sel ? 2.2 : 1.3);
                StreamGeometry g = new StreamGeometry();
                List<Point> hours = new List<Point>(); List<int> hv = new List<int>();
                using (StreamGeometryContext gc = g.Open())
                {
                    bool open = false;
                    for (int i = 0; i < m.Track.Count; i++)
                    {
                        System.Drawing.PointF t = m.Track[i];
                        if (t.Y < 0) { if (open) gc.EndFigure(false); open = false; continue; }
                        Point p = SkyXY(t.X, t.Y, cx, cy, rad);
                        if (!open) { gc.BeginFigure(p, false); open = true; }
                        else gc.LineTo(p);
                        if (sel && m.TrackHours != null && i < m.TrackHours.Count && m.TrackHours[i] >= 0)
                        {
                            hours.Add(p); hv.Add(m.TrackHours[i]);
                        }
                    }
                    if (open) gc.EndFigure(false);
                }
                ctx.DrawGeometry(null, tp, g);
                for (int i = 0; i < hours.Count; i++)
                {
                    ctx.DrawEllipse(cyan, null, hours[i], 2, 2);
                    Txt(ctx, hv[i].ToString("00"), F7, LightCyan, hours[i].X + 3, hours[i].Y - 7);
                }
            }
            IPen selPen = Pal.P(White, 1);
            foreach (RadiantMark m in Marks)
            {
                if (m.El < 0) continue;
                Point p = SkyXY(m.Az, m.El, cx, cy, rad);
                Color c;
                if (m.Zhr < 1) c = Color.FromRgb(130, 130, 130);
                else if (m.Eff >= 50 && m.Zhr >= 2) c = Pal.Yellow;
                else if (m.Eff >= 20) c = Pal.Orange;
                else c = Color.FromRgb(194, 65, 12);
                ctx.DrawEllipse(Pal.B(c), null, p, 7, 7);
                if (m.Code == Selected) ctx.DrawEllipse(null, selPen, p, 9, 9);
                Txt(ctx, m.Code, F85, White, p.X + 9, p.Y - 10, FontWeight.Bold);
            }
        }

        // Legenda dei simboli
        void DrawSymbolLegend(DrawingContext ctx, double x, double y)
        {
            double yy = y;
            Txt(ctx, "Legenda", F75, Gainsboro, x, yy, FontWeight.Bold); yy += 22;
            Item(ctx, x, ref yy, Pal.Green, "tratta / DX");
            Item(ctx, x, ref yy, Pal.Red, "Hot consigliato");
            Item(ctx, x, ref yy, Pal.HotPink, "Hot fuori lobo");
            Item(ctx, x, ref yy, Color.FromRgb(150, 150, 210), "limiti zona comune");
            Item(ctx, x, ref yy, Pal.HotGrey, "Hot nel lobo");
            Item(ctx, x, ref yy, Color.FromRgb(255, 240, 200), "lobo antenna");
            Item(ctx, x, ref yy, Color.FromRgb(255, 210, 90), "scorrimento sciame");
            Item(ctx, x, ref yy, Pal.Orange, "miglior punt.");
            Item(ctx, x, ref yy, Color.FromRgb(235, 225, 190), "zona PREV");
            if (ShowRadiants || !(ShowMap && TopView))
            {
                Item(ctx, x, ref yy, Pal.Azure, "percorso rad.");
                yy += 8;
                Txt(ctx, "Radiante:", F75, Gainsboro, x, yy, FontWeight.Bold); yy += 20;
                Item(ctx, x, ref yy, Pal.Yellow, "effic. >= 50%");
                Item(ctx, x, ref yy, Pal.Orange, "effic. >= 20%");
                Item(ctx, x, ref yy, Color.FromRgb(194, 65, 12), "effic. < 20%");
                Item(ctx, x, ref yy, Color.FromRgb(130, 130, 130), "quasi inattivo");
            }
            yy += 8;
            string[] note = { "Mappa:", "clic sinistro =", "corrispondente", "clic destro =", "la mia stazione" };
            foreach (string n in note) { Txt(ctx, n, F75, Pal.Silver, x, yy); yy += 16; }
        }

        static void Item(DrawingContext ctx, double x, ref double y, Color c, string text)
        {
            ctx.DrawEllipse(Pal.B(c), null, new Point(x + 4.5, y + 7), 4.5, 4.5);
            Txt(ctx, text, F75, Gainsboro, x + 13, y);
            y += 18;
        }

        public string HitTest(Point pt)
        {
            if (!ShowRadiants && ShowMap && TopView) return null;   // in pianta i radianti non sono disegnati
            if (Marks == null) return null;
            double cx, cy, rad; Geom(out cx, out cy, out rad);
            string best = null; double bd = 15;
            foreach (RadiantMark m in Marks)
            {
                if (m.El < 0) continue;
                Point p = SkyXY(m.Az, m.El, cx, cy, rad);
                double d = Math.Sqrt((p.X - pt.X) * (p.X - pt.X) + (p.Y - pt.Y) * (p.Y - pt.Y));
                if (d < bd) { bd = d; best = m.Code; }
            }
            return best;
        }
    }
}
