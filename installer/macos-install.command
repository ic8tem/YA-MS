#!/bin/sh
# YA-MS - installazione per Mac nella cartella personale ~/YA-MS (YA-MS.app e cartella data insieme)
SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/YA-MS"
echo "Installo YA-MS in $DEST"
mkdir -p "$DEST"
rm -rf "$DEST/YA-MS.app"
cp -R "$SRC/YA-MS.app" "$DEST/"
[ -f "$SRC/LEGGIMI.txt" ] && cp "$SRC/LEGGIMI.txt" "$DEST/"
# il programma non e' firmato da Apple: tolgo il blocco di "scaricato da Internet"
xattr -dr com.apple.quarantine "$DEST/YA-MS.app" 2>/dev/null || true
echo "Fatto. Apro YA-MS..."
open "$DEST/YA-MS.app"
