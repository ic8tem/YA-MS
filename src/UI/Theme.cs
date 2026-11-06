// YA-MS - tavolozza "Scia meteorica" (azzurro, viola, verde chiaro, giallo, arancione) e caratteri
using Avalonia.Media;
using Avalonia.Media.Immutable;

namespace YAMS
{
    public static class Pal
    {
        public static readonly Color Back = Color.FromRgb(22, 18, 48);       // sfondo
        public static readonly Color Panel = Color.FromRgb(28, 23, 64);      // riquadri
        public static readonly Color Panel2 = Color.FromRgb(34, 28, 71);     // righe dei comandi
        public static readonly Color Panel3 = Color.FromRgb(43, 33, 96);     // bottoni secondari, etichette a pillola
        public static readonly Color Track = Color.FromRgb(14, 11, 34);      // fondo della barra delle linguette
        public static readonly Color Border = Color.FromRgb(58, 50, 112);
        public static readonly Color Fore = Color.FromRgb(238, 235, 250);
        public static readonly Color Muted = Color.FromRgb(179, 173, 214);
        public static readonly Color Azure = Color.FromRgb(56, 189, 248);
        public static readonly Color AzureDark = Color.FromRgb(11, 34, 51);
        public static readonly Color Violet = Color.FromRgb(167, 139, 250);
        public static readonly Color Green = Color.FromRgb(134, 239, 172);
        public static readonly Color Yellow = Color.FromRgb(253, 224, 71);
        public static readonly Color Orange = Color.FromRgb(251, 146, 60);
        public static readonly Color OrangeDark = Color.FromRgb(58, 35, 18);
        public static readonly Color OrangeText = Color.FromRgb(254, 215, 170);
        public static readonly Color Pink = Color.FromRgb(240, 171, 252);
        public static readonly Color Red = Color.FromRgb(248, 113, 113);
        public static readonly Color HotPink = Color.FromRgb(240, 120, 240);     // Hot fuori dal lobo
        public static readonly Color HotGrey = Color.FromRgb(150, 150, 150);     // Hot dentro il lobo
        public static readonly Color Silver = Color.FromRgb(192, 192, 192);

        public static Color A(int alpha, Color c) { return Color.FromArgb((byte)alpha, c.R, c.G, c.B); }
        public static Color Rgb(int r, int g, int b) { return Color.FromRgb((byte)r, (byte)g, (byte)b); }
        public static Color Argb(int a, int r, int g, int b) { return Color.FromArgb((byte)a, (byte)r, (byte)g, (byte)b); }
        public static IBrush B(Color c) { return new ImmutableSolidColorBrush(c); }
        public static IPen P(Color c, double w = 1) { return new ImmutablePen(new ImmutableSolidColorBrush(c), w); }
        public static IPen P(Color c, double w, ImmutableDashStyle dash) { return new ImmutablePen(new ImmutableSolidColorBrush(c), w, dash); }
        public static readonly ImmutableDashStyle Dash = new ImmutableDashStyle(new double[] { 4, 3 }, 0);
        public static readonly ImmutableDashStyle Dot = new ImmutableDashStyle(new double[] { 1, 2 }, 0);
        public static readonly ImmutableDashStyle DashDot = new ImmutableDashStyle(new double[] { 5, 2, 1, 2 }, 0);

        // carattere a spaziatura fissa: il primo disponibile sul sistema
        public static readonly FontFamily Mono = new FontFamily("Cascadia Mono, Consolas, DejaVu Sans Mono, Menlo, Liberation Mono, monospace");
        public static readonly FontFamily Ui = FontFamily.Default;
    }
}
