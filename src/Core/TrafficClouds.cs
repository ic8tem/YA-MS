// YA-MS - nuvole della concentrazione di scie per una tratta A-B a un'ora data (linguetta "Traffico in diretta").
// Per ogni lato della tratta: media e dispersione pesata dei punti di riflessione, pesi = somma su tutti gli sciami
// attivi di ZHR x contributo speculare. Senza sciami utili restano gli hot spot classici (sporadiche).
//
// Versione veloce (dalla 1.8.29): le nuvole dipendono solo dai rapporti tra i contributi, quindi non serve la tabella
// dell'efficienza per direzione della tratta (la parte piu' pesante del modello). La sola soglia "c'e' un contributo"
// (somma > 1e-6 in %) dipende dalla scala: si decide con il limite superiore esatto WeightSum >= massimo della tabella,
// e solo se il limite non basta si calcola la tabella come prima. Il risultato e' lo stesso del calcolo completo.
using System;
using System.Collections.Generic;

namespace YAMS
{
    public static class TrafficClouds
    {
        public static List<TrafficCloud> Compute(DateTime utc, LatLon a, LatLon b, double layerKm, bool fast)
        {
            List<TrafficCloud> res = new List<TrafficCloud>();
            PathModel pm = PathModel.Build(a, 0.05, b, 0.05, layerKm, 0, !fast);
            if (pm == null || !pm.Valid || pm.SamplePoints <= 0) return res;
            double jd = Astro.JulianDay(utc), lam = Astro.SolarLongitude(jd);
            double[] acc = new double[pm.SamplePoints];
            double tot = 0;
            foreach (Shower sh in Catalog.Showers)
            {
                if (!sh.IsActive(utc)) continue;
                double zhr = sh.ZhrAt(lam, utc);
                if (zhr < 0.1) continue;
                double ra, dec; sh.RadiantAt(lam, utc, out ra, out dec);
                Vec3 v = Astro.RaDecToEcef(ra, dec, jd);
                double[] c = fast ? pm.ContributionsRaw(v) : pm.Contributions(v);
                for (int i = 0; i < c.Length && i < acc.Length; i++) { acc[i] += zhr * c[i]; tot += zhr * c[i]; }
            }
            bool useful;
            if (!fast) useful = tot > 1e-6;
            else if (pm.WeightSum > 0 && tot / pm.WeightSum > 1e-6) useful = true;   // tot/fieldMax >= tot/WeightSum > 1e-6
            else useful = tot / pm.FieldMax > 1e-6;                                  // caso di confine: tabella calcolata come prima
            if (useful)
            {
                foreach (bool left in new[] { true, false })
                {
                    double sw = 0, la = 0, lo = 0;
                    for (int i = 0; i < acc.Length; i++)
                    {
                        if (pm.SampleLeft(i) != left || acc[i] <= 0) continue;
                        LatLon q = pm.SampleLatLon(i);
                        sw += acc[i]; la += acc[i] * q.Lat; lo += acc[i] * q.Lon;
                    }
                    if (sw < 0.15 * tot) continue;
                    la /= sw; lo /= sw;
                    double k = Math.Cos(la * Math.PI / 180) * 111.2, sxx = 0, syy = 0, sxy = 0;
                    for (int i = 0; i < acc.Length; i++)
                    {
                        if (pm.SampleLeft(i) != left || acc[i] <= 0) continue;
                        LatLon q = pm.SampleLatLon(i);
                        double e = (q.Lon - lo) * k, n = (q.Lat - la) * 111.2;
                        sxx += acc[i] * e * e; syy += acc[i] * n * n; sxy += acc[i] * e * n;
                    }
                    sxx /= sw; syy /= sw; sxy /= sw;
                    double tr = sxx + syy, det = sxx * syy - sxy * sxy, disc = Math.Sqrt(Math.Max(0, tr * tr / 4 - det));
                    double l1 = tr / 2 + disc, l2 = Math.Max(0, tr / 2 - disc);
                    // direzione dell'asse maggiore (x = est, y = nord) e suo azimut
                    double ang = 0.5 * Math.Atan2(2 * sxy, sxx - syy);
                    double az = Astro.Norm360(90 - ang * 180 / Math.PI);
                    res.Add(new TrafficCloud
                    {
                        Centre = new LatLon(la, lo), MajorKm = Math.Max(30, 1.5 * Math.Sqrt(l1)), MinorKm = Math.Max(20, 1.5 * Math.Sqrt(l2)),
                        AngleDeg = az, Share = sw / tot
                    });
                }
            }
            else
                foreach (HotPoint h in new[] { pm.HotA, pm.HotB })
                    if (h != null) res.Add(new TrafficCloud { Centre = h.Pos, MajorKm = 70, MinorKm = 70, Share = 0.5, Sporadic = true });
            return res;
        }
    }
}
