#!/usr/bin/env bash
# YA-MS: rigenera il manuale dei calcoli e la spiegazione dell'efficienza in tutte le lingue
# (italiano dal sorgente, le altre da tools/traduzioni_doc/<documento>/<codice>.json).
set -euo pipefail
cd "$(dirname "$0")/.."
node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx
python3 tools/build_spiegazione.py data
mkdir -p doc/manuali
for f in tools/traduzioni_doc/manuale/*.json; do
  c=$(basename "$f" .json); [ "$c" = chiavi ] && continue
  node tools/build_manuale.js "doc/manuali/YA-MS_manuale_calcoli_$c.docx" "$c"
done
for f in tools/traduzioni_doc/spiegazione/*.json; do
  c=$(basename "$f" .json); [ "$c" = chiavi ] && continue
  python3 tools/build_spiegazione.py data "$c"
done
