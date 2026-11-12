# Verifica del modello di YA-MS con gli spot reali di meteor scatter.
# Uso: python3 tools/verifica_spot.py <spot.tsv> <eseguibile YA-MS> [MHz_min MHz_max]
#   spot.tsv: formato HamSCI MSQP / PSKReporter ripulito, senza intestazione:
#     tempo unix; frequenza Hz; SNR; modo; nominativo tx; locator tx; nominativo rx; locator rx; programma
# Domanda: le tratte e le ore che il modello da' come favorevoli raccolgono piu' spot?
#   positivi = (tratta, ora) con almeno uno spot; negativi = stessa tratta in un'ora in cui entrambe le stazioni
#   erano attive (tx visto da qualcuno, rx che riceveva qualcuno) ma senza spot tra loro.
#   AUC = probabilita' che un positivo abbia indice piu' alto di un negativo (0,5 = a caso).
#   "AUC nella stessa ora" confronta solo tratte nella stessa ora: toglie l'effetto dell'ora del giorno
#   (attivita' degli operatori, meteore sporadiche) e misura la geometria (quale orientamento e quale distanza).
import sys, csv, math, subprocess, collections, datetime, os

f_spot, exe = sys.argv[1], sys.argv[2]
fmin = float(sys.argv[3]) if len(sys.argv) > 3 else 50.0
fmax = float(sys.argv[4]) if len(sys.argv) > 4 else 54.0

def loc2ll(l):
    l = l.strip().upper()
    if len(l) < 4 or not ('A' <= l[0] <= 'R' and 'A' <= l[1] <= 'R' and l[2].isdigit() and l[3].isdigit()): return None
    lon = (ord(l[0]) - 65) * 20 - 180 + int(l[2]) * 2; lat = (ord(l[1]) - 65) * 10 - 90 + int(l[3])
    if len(l) >= 6 and 'A' <= l[4] <= 'X' and 'A' <= l[5] <= 'X':
        lon += (ord(l[4]) - 65) * 5 / 60 + 2.5 / 60; lat += (ord(l[5]) - 65) * 2.5 / 60 + 1.25 / 60
    else: lon += 1; lat += 0.5
    return lat, lon

def km(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    c = math.sin(p1) * math.sin(p2) + math.cos(p1) * math.cos(p2) * math.cos(dl)
    return 6372.8 * math.acos(max(-1, min(1, c)))

rows = []
for r in csv.reader(open(f_spot, encoding='utf-8', errors='replace'), delimiter='\t'):
    if len(r) < 8: continue
    try: t = int(r[0]); f = int(r[1]) / 1e6
    except ValueError: continue
    if not (fmin <= f <= fmax): continue
    a, b = loc2ll(r[5]), loc2ll(r[7])
    if a is None or b is None: continue
    rows.append((t, r[4].upper(), r[5][:6].upper(), r[6].upper(), r[7][:6].upper(), km(a, b)))
print('spot nella banda %.0f-%.0f MHz: %d' % (fmin, fmax, len(rows)))
t0 = min(x[0] for x in rows); t1 = max(x[0] for x in rows)
h0 = datetime.datetime.utcfromtimestamp(t0).replace(minute=0, second=0)
nh = int((t1 - h0.timestamp()) // 3600) + 1
print('periodo: %s UTC, %d ore' % (h0.strftime('%Y-%m-%d %H:%M'), nh))

hour = lambda t: int((t - h0.timestamp()) // 3600)
txact = collections.defaultdict(set); rxact = collections.defaultdict(set)
minutes = collections.defaultdict(set)   # (tx, rx, h) -> minuti con decodifiche
pairloc = {}
for t, tx, ltx, rx, lrx, d in rows:
    h = hour(t); txact[tx].add(h); rxact[rx].add(h)
    if not (300 <= d <= 2300): continue      # onda di terra sotto 300 km, oltre il singolo salto sopra 2300
    minutes[(tx, rx, h)].add(t // 60)
    pairloc[(tx, rx)] = (ltx, lrx)
print('tratte (tx, rx) tra 300 e 2300 km: %d' % len(pairloc))

locpairs = sorted(set(pairloc.values()))
open('coppie.txt', 'w').write('\n'.join('%s %s' % p for p in locpairs) + '\n')
out = subprocess.run([exe, '--indici-tratte', 'coppie.txt', h0.strftime('%Y-%m-%dT%H'), str(nh)], capture_output=True, text=True)
idx = {}
for line in out.stdout.splitlines()[1:]:
    p = line.split(';')
    if len(p) < 7: continue
    idx[(p[0], p[1], int(p[3]))] = (float(p[4]), float(p[5]), float(p[6]), float(p[2]))
print('indici calcolati da YA-MS: %d righe (%d coppie di locator)' % (len(idx), len(locpairs)))
if out.stderr.strip(): print(out.stderr[-2000:])

MODELS = ['YA-MS beta acceso', 'YA-MS beta spento', 'DH9GCD']
def collect(es_max):
    data = []   # (h, positivo, I_b, I_n, I_d)
    for (tx, rx), (ltx, lrx) in pairloc.items():
        for h in range(nh):
            if h not in txact[tx] or h not in rxact[rx]: continue
            k = (ltx, lrx, h)
            if k not in idx: continue
            m = len(minutes.get((tx, rx, h), ()))
            if es_max and m >= es_max: continue    # decodifiche quasi continue: probabile Es, non meteor scatter
            ib, inn, idh, _ = idx[k]
            data.append((h, 1 if m > 0 else 0, ib, inn, idh))
    return data

def auc(pairs):
    pos = [v for v, y in pairs if y]; neg = [v for v, y in pairs if not y]
    if not pos or not neg: return None, len(pos), len(neg)
    allv = sorted([(v, y) for v, y in pairs])
    # AUC con i ranghi medi (gestisce i valori uguali, per esempio gli zeri)
    ranks = {}; i = 0
    while i < len(allv):
        j = i
        while j < len(allv) and allv[j][0] == allv[i][0]: j += 1
        for k in range(i, j): ranks.setdefault(allv[i][0], (i + j + 1) / 2)
        i = j
    rs = sum(ranks[v] for v in pos)
    return (rs - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)), len(pos), len(neg)

for es_max, title in ((0, 'tutti gli spot'), (20, 'senza le tratte-ora con 20 o piu\' minuti di decodifiche (probabile Es)')):
    data = collect(es_max)
    print('\n=== %s: %d tratte-ora con entrambe le stazioni attive, %d con spot' % (title, len(data), sum(d[1] for d in data)))
    for mi, name in enumerate(MODELS):
        a, npos, nneg = auc([(d[2 + mi], d[1]) for d in data])
        # nella stessa ora: media delle AUC orarie pesata con i positivi
        num = den = 0
        byh = collections.defaultdict(list)
        for d in data: byh[d[0]].append((d[2 + mi], d[1]))
        for h, l in byh.items():
            ah, p, n = auc(l)
            if ah is not None and p >= 3 and n >= 3: num += ah * p; den += p
        print('%-20s AUC %s   AUC nella stessa ora %s' % (name, '%.3f' % a if a is not None else '-', '%.3f' % (num / den) if den else '-'))
    # frazione di tratte-ora con spot per fascia di indice (beta acceso / spento)
    for mi, name in ((0, 'beta acceso'), (1, 'beta spento')):
        vals = sorted(d[2 + mi] for d in data)
        if not vals: continue
        q = [vals[int(len(vals) * k / 5)] for k in range(1, 5)]
        bins = collections.defaultdict(lambda: [0, 0])
        for d in data:
            b = sum(1 for x in q if d[2 + mi] > x); bins[b][0] += d[1]; bins[b][1] += 1
        print('  %s, quinti dell\'indice (dal piu\' basso): ' % name + '  '.join('%.1f%%' % (100.0 * bins[b][0] / bins[b][1]) if bins[b][1] else '-' for b in range(5)))

# ore con piu' spot e indice medio
tot = collections.Counter();
for (tx, rx, h), mm in minutes.items(): tot[h] += 1
print('\nora (UTC)  tratte con spot   indice medio beta acceso / spento delle tratte attive')
for h in range(nh):
    act = [(idx[(pairloc[p][0], pairloc[p][1], h)]) for p in pairloc if h in txact[p[0]] and h in rxact[p[1]] and (pairloc[p][0], pairloc[p][1], h) in idx]
    if not act: continue
    mb = sum(a[0] for a in act) / len(act); mn = sum(a[1] for a in act) / len(act)
    print('%s   %5d   %6.2f / %6.2f' % ((h0 + datetime.timedelta(hours=h)).strftime('%d %H'), tot[h], mb, mn))
