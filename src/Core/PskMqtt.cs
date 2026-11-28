// YA-MS - quarta fonte della Raccolta dati: gli spot di PSKReporter in diretta via MQTT (mqtt.pskreporter.info, servizio
// di M0LTE con i dati di pskreporter.info). Nessun account e nessuna interrogazione periodica: ci si abbona agli
// argomenti (topic) che interessano e il server manda ogni spot appena arriva.
// Argomento: pskr/filter/v2/{banda}/{modo}/{call tx}/{call rx}/{loc tx}/{loc rx}/{dxcc tx}/{dxcc rx}  (+ = qualsiasi, # = il resto)
// Messaggio JSON: f frequenza Hz, md modo, rp rapporto dB, t ora (epoch), sc/sl chi trasmette e locator,
// rc/rl chi riceve e locator, b banda.
// Client MQTT 3.1.1 minimo (solo abbonamento con QoS 0), senza librerie esterne.
using System;
using System.Buffers;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;

namespace YAMS
{
    public static class PskMqtt
    {
        public const string DefaultHost = "mqtt.pskreporter.info";
        public const int DefaultPort = 1883;
        // modi MS (MSK144, FSK441, PSK2K, JTMS) su 28, 50, 70, 144 e 432 MHz (nomi delle bande come li scrive PSKReporter),
        // piu' MSK144 su 222 MHz (regola dell'autore, IC8TEM, 13/11/2026)
        public static readonly string[] MsModes = { "MSK144", "FSK441", "PSK2K", "JTMS" };
        // FT8 su 6 m, 4 m, 2 m, 1,25 m e 70 cm per la clausola degli FT8 lunghi e isolati (regola dell'autore, 14/11/2026).
        // Niente FT8 sui 10 m di partenza: il traffico mondiale e' enorme; si puo' aggiungere a mano pskr/filter/v2/10m/FT8/#
        public static readonly string[] Ft8Bands = { "6m", "4m", "2m", "1.25m", "70cm" };
        public static readonly string DefaultTopics = BuildDefault(true);
        // argomenti di partenza delle versioni dalla 1.8.4 alla 1.8.11, senza FT8 (si aggiornano da soli se non cambiati)
        public static readonly string PrevDefaultTopics = BuildDefault(false);
        // argomenti di partenza delle versioni fino alla 1.8.3 (si aggiornano da soli se l'utente non li aveva cambiati)
        public const string OldDefaultTopics = "pskr/filter/v2/6m/MSK144/#; pskr/filter/v2/4m/MSK144/#; pskr/filter/v2/2m/MSK144/#; " +
                                               "pskr/filter/v2/1.25m/MSK144/#; pskr/filter/v2/70cm/MSK144/#; pskr/filter/v2/2m/FSK441/#";

        static string BuildDefault(bool ft8)
        {
            List<string> t = new List<string>();
            foreach (string b in new[] { "10m", "6m", "4m", "2m", "70cm" })
                foreach (string m in MsModes) t.Add("pskr/filter/v2/" + b + "/" + m + "/#");
            t.Add("pskr/filter/v2/1.25m/MSK144/#");
            if (ft8) foreach (string b in Ft8Bands) t.Add("pskr/filter/v2/" + b + "/FT8/#");
            return string.Join("; ", t);
        }

        public static string Host = DefaultHost;
        public static int Port = DefaultPort;
        public static string Topics = DefaultTopics;
        public static bool AutoReconnect = true;
        public static string StateKey = "Non connesso", StateArg = "";   // stato: chiave da tradurre con Lang.F e argomento
        public static bool Connected { get { return connected; } }
        public static int Messages;

        public static event Action<MsSpot, string> SpotReceived;   // spot e riga leggibile per la console (thread secondario)

        static volatile bool connected, want, running;
        static TcpClient client;
        static CancellationTokenSource cts;

        public static void Connect()
        {
            want = true;
            if (running) return;
            Task.Run(() => Loop());
        }

        public static void Disconnect()
        {
            want = false;
            try { if (cts != null) cts.Cancel(); } catch { }
            try { if (client != null) client.Close(); } catch { }
        }

        static void State(string key, string arg = "") { StateArg = arg; StateKey = key; }

        static async Task Loop()
        {
            running = true;
            int wait = 5;
            try
            {
                while (want)
                {
                    cts = new CancellationTokenSource();
                    try
                    {
                        State("Connessione a {0}...", Host + ":" + Port);
                        client = new TcpClient();
                        await client.ConnectAsync(Host, Port, cts.Token);
                        NetworkStream ns = client.GetStream();
                        string id = "YA-MS-" + Guid.NewGuid().ToString("N").Substring(0, 10);
                        Write(ns, Connect(id, 60));
                        int type; byte[] body = Read(ns, out type);
                        if (type != 2 || body.Length < 2 || body[1] != 0) throw new IOException("connection refused by the MQTT server");
                        List<string> topics = new List<string>();
                        foreach (string t in (Topics ?? "").Split(new[] { ';', '\n', ',' }, StringSplitOptions.RemoveEmptyEntries))
                            if (t.Trim().Length > 0) topics.Add(t.Trim());
                        if (topics.Count == 0) throw new IOException("no topics to subscribe");
                        Write(ns, Subscribe(1, topics));
                        connected = true; wait = 5;
                        State("Connesso: {0} argomenti", topics.Count.ToString(CultureInfo.InvariantCulture));
                        DateTime lastPing = DateTime.UtcNow;
                        client.ReceiveTimeout = 0;
                        while (want && !cts.IsCancellationRequested)
                        {
                            if ((DateTime.UtcNow - lastPing).TotalSeconds > 45) { Write(ns, new byte[] { 0xC0, 0x00 }); lastPing = DateTime.UtcNow; }
                            if (!ns.DataAvailable) { await Task.Delay(100, cts.Token); continue; }
                            body = Read(ns, out type);
                            if (type == 3) OnPublish(body);
                        }
                    }
                    catch (Exception ex)
                    {
                        if (want) State("Errore: {0}", ex.Message);
                    }
                    finally
                    {
                        connected = false;
                        try { if (client != null) client.Close(); } catch { }
                    }
                    if (!want) break;
                    if (!AutoReconnect) { want = false; break; }
                    State("Riconnessione tra {0} s", wait.ToString(CultureInfo.InvariantCulture));
                    try { await Task.Delay(wait * 1000); } catch { }
                    wait = Math.Min(120, wait * 2);
                }
            }
            finally
            {
                running = false; connected = false;
                if (!want) State("Non connesso");
            }
        }

        // ---- pacchetti MQTT 3.1.1
        static byte[] Str(string s) { byte[] b = Encoding.UTF8.GetBytes(s); byte[] r = new byte[b.Length + 2]; r[0] = (byte)(b.Length >> 8); r[1] = (byte)b.Length; Buffer.BlockCopy(b, 0, r, 2, b.Length); return r; }

        static byte[] Packet(byte head, List<byte> body)
        {
            List<byte> p = new List<byte> { head };
            int len = body.Count;
            do { byte d = (byte)(len % 128); len /= 128; if (len > 0) d |= 0x80; p.Add(d); } while (len > 0);
            p.AddRange(body);
            return p.ToArray();
        }

        static byte[] Connect(string clientId, int keepAlive)
        {
            List<byte> b = new List<byte>();
            b.AddRange(Str("MQTT")); b.Add(4); b.Add(0x02);   // livello 4 = 3.1.1, sessione pulita
            b.Add((byte)(keepAlive >> 8)); b.Add((byte)keepAlive);
            b.AddRange(Str(clientId));
            return Packet(0x10, b);
        }

        static byte[] Subscribe(int packetId, List<string> topics)
        {
            List<byte> b = new List<byte> { (byte)(packetId >> 8), (byte)packetId };
            foreach (string t in topics) { b.AddRange(Str(t)); b.Add(0); }   // QoS 0
            return Packet(0x82, b);
        }

        static void Write(NetworkStream ns, byte[] p) { ns.Write(p, 0, p.Length); ns.Flush(); }

        static void ReadExact(NetworkStream ns, byte[] buf, int n)
        {
            int got = 0;
            while (got < n) { int r = ns.Read(buf, got, n - got); if (r <= 0) throw new IOException("connection closed by the server"); got += r; }
        }

        static byte[] Read(NetworkStream ns, out int type)
        {
            byte[] one = new byte[1];
            ReadExact(ns, one, 1);
            type = one[0] >> 4;
            int len = 0, mul = 1;
            for (int i = 0; i < 4; i++)
            {
                ReadExact(ns, one, 1);
                len += (one[0] & 0x7F) * mul; mul *= 128;
                if ((one[0] & 0x80) == 0) break;
            }
            if (len > 1 << 20) throw new IOException("packet too large");   // un messaggio di PSKReporter e' di poche centinaia di byte
            byte[] body = new byte[len];
            if (len > 0) ReadExact(ns, body, len);
            return body;
        }

        static void OnPublish(byte[] body)
        {
            if (body.Length < 2) return;
            int tl = (body[0] << 8) | body[1];
            if (2 + tl > body.Length) return;
            Messages++;
            // lettura diretta dei byte (dalla 1.8.29): niente stringa intermedia, riga della console scritta solo se serve
            MsSpot s = ParseJsonFast(new ReadOnlySpan<byte>(body, 2 + tl, body.Length - 2 - tl), DateTime.UtcNow);
            if (s == null) return;
            Action<MsSpot, string> h = SpotReceived;
            if (h != null) h(s, null);   // la riga leggibile e' s.Line, calcolata al primo uso
        }

        public static MsSpot ParseJson(string json, DateTime nowUtc)
        {
            try
            {
                using (JsonDocument d = JsonDocument.Parse(json))
                {
                    JsonElement r = d.RootElement;
                    double f = Num(r, "f");
                    if (!(f > 0)) return null;
                    string md = Txt(r, "md"), sc = Txt(r, "sc").ToUpperInvariant(), rc = Txt(r, "rc").ToUpperInvariant();
                    if (sc.Length == 0 || rc.Length == 0) return null;
                    double t = Num(r, "t");
                    DateTime utc = t > 1e9 ? DateTimeOffset.FromUnixTimeSeconds((long)t).UtcDateTime : nowUtc;
                    if (utc > nowUtc.AddMinutes(10)) utc = nowUtc;
                    double rp = Num(r, "rp");
                    MsSpot s = new MsSpot
                    {
                        Source = 3, FreqKHz = f / 1000.0, DxCall = sc, Spotter = rc, Utc = utc, Mode = md.ToUpperInvariant(),
                        LocDx = Loc(Txt(r, "sl")), LocSpotter = Loc(Txt(r, "rl")),
                        Comment = (md + (double.IsNaN(rp) ? "" : " " + rp.ToString("+0;-0", CultureInfo.InvariantCulture) + " dB")).Trim()
                    };
                    s.Line = FormatLine(s);
                    return s;
                }
            }
            catch { return null; }
        }

        public static string FormatLine(MsSpot s)
        {
            return string.Format(CultureInfo.InvariantCulture, "{0:HH:mm:ss}  {1,10:F1}  {2,-10} {3,-6} -> {4,-10} {5,-6}  {6}",
                s.Utc, s.FreqKHz, s.DxCall, s.LocDx, s.Spotter, s.LocSpotter, s.Comment);
        }

        // Stessi campi e stesse regole di ParseJson, letti con Utf8JsonReader direttamente dai byte del messaggio.
        // Solo le proprieta' di primo livello; con chiavi ripetute vale l'ultima, come per l'oggetto letto da JsonDocument.
        public static MsSpot ParseJsonFast(ReadOnlySpan<byte> json, DateTime nowUtc)
        {
            try
            {
                Utf8JsonReader rd = new Utf8JsonReader(json, new JsonReaderOptions { CommentHandling = JsonCommentHandling.Disallow });
                if (!rd.Read() || rd.TokenType != JsonTokenType.StartObject) return null;
                double f = double.NaN, t = double.NaN, rp = double.NaN;
                string md = "", sc = "", rc = "", sl = "", rl = "";
                while (rd.Read())
                {
                    if (rd.TokenType == JsonTokenType.EndObject) break;
                    if (rd.TokenType != JsonTokenType.PropertyName) return null;
                    int key = KeyOf(ref rd);
                    if (!rd.Read()) return null;
                    switch (key)
                    {
                        case 1: f = NumR(ref rd); break;
                        case 2: md = TxtR(ref rd); break;
                        case 3: sc = TxtR(ref rd); break;
                        case 4: rc = TxtR(ref rd); break;
                        case 5: t = NumR(ref rd); break;
                        case 6: rp = NumR(ref rd); break;
                        case 7: sl = TxtR(ref rd); break;
                        case 8: rl = TxtR(ref rd); break;
                        default: rd.Skip(); break;
                    }
                }
                // il resto del documento deve essere valido come per JsonDocument.Parse
                while (rd.Read()) { }
                if (!(f > 0)) return null;
                sc = sc.ToUpperInvariant(); rc = rc.ToUpperInvariant();
                if (sc.Length == 0 || rc.Length == 0) return null;
                DateTime utc = t > 1e9 ? DateTimeOffset.FromUnixTimeSeconds((long)t).UtcDateTime : nowUtc;
                if (utc > nowUtc.AddMinutes(10)) utc = nowUtc;
                MsSpot s = new MsSpot
                {
                    Source = 3, FreqKHz = f / 1000.0, DxCall = sc, Spotter = rc, Utc = utc, Mode = md.ToUpperInvariant(),
                    LocDx = Loc(sl), LocSpotter = Loc(rl),
                    Comment = (md + (double.IsNaN(rp) ? "" : " " + rp.ToString("+0;-0", CultureInfo.InvariantCulture) + " dB")).Trim()
                };
                s.LineFormatter = FormatLine;   // riga della console solo al primo uso
                return s;
            }
            catch { return null; }
        }

        static int KeyOf(ref Utf8JsonReader rd)
        {
            if (rd.ValueTextEquals("f")) return 1;
            if (rd.ValueTextEquals("md")) return 2;
            if (rd.ValueTextEquals("sc")) return 3;
            if (rd.ValueTextEquals("rc")) return 4;
            if (rd.ValueTextEquals("t")) return 5;
            if (rd.ValueTextEquals("rp")) return 6;
            if (rd.ValueTextEquals("sl")) return 7;
            if (rd.ValueTextEquals("rl")) return 8;
            return 0;
        }

        // come Txt: stringa, o testo grezzo se e' un numero, altrimenti ""
        static string TxtR(ref Utf8JsonReader rd)
        {
            if (rd.TokenType == JsonTokenType.String) return rd.GetString() ?? "";
            if (rd.TokenType == JsonTokenType.Number) return Encoding.UTF8.GetString(rd.HasValueSequence ? rd.ValueSequence.ToArray() : rd.ValueSpan.ToArray());
            rd.Skip(); return "";
        }

        // come Num: numero, o stringa che contiene un numero, altrimenti NaN
        static double NumR(ref Utf8JsonReader rd)
        {
            double d;
            if (rd.TokenType == JsonTokenType.Number) return rd.TryGetDouble(out d) ? d : double.NaN;
            if (rd.TokenType == JsonTokenType.String)
                return double.TryParse(rd.GetString(), NumberStyles.Float, CultureInfo.InvariantCulture, out d) ? d : double.NaN;
            rd.Skip(); return double.NaN;
        }

        static string Txt(JsonElement r, string k)
        {
            JsonElement v;
            if (!r.TryGetProperty(k, out v)) return "";
            return v.ValueKind == JsonValueKind.String ? (v.GetString() ?? "") : v.ValueKind == JsonValueKind.Number ? v.GetRawText() : "";
        }

        static double Num(JsonElement r, string k)
        {
            JsonElement v; double d;
            if (!r.TryGetProperty(k, out v)) return double.NaN;
            if (v.ValueKind == JsonValueKind.Number && v.TryGetDouble(out d)) return d;
            if (v.ValueKind == JsonValueKind.String && double.TryParse(v.GetString(), NumberStyles.Float, CultureInfo.InvariantCulture, out d)) return d;
            return double.NaN;
        }

        // locator a 4 o 6 caratteri (PSKReporter a volte ne manda 8 o 10: si tengono i primi 6)
        static string Loc(string l)
        {
            l = (l ?? "").Trim().ToUpperInvariant();
            if (l.Length >= 6) l = l.Substring(0, 6); else if (l.Length >= 4) l = l.Substring(0, 4); else return "";
            LatLon p;
            return Astro.TryLocator(l, out p) ? l : "";
        }
    }
}
