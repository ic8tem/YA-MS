#!/usr/bin/env bash
# YA-MS - AppImage (un solo file, gira su quasi tutte le distribuzioni Linux con glibc).
# L'AppImage e' in sola lettura: al primo avvio (e a ogni nuova versione) copia il programma in ~/YA-MS
# e lo avvia da li', cosi' la cartella data resta accanto al programma, come negli altri pacchetti.
# Uso: installer/make-appimage.sh <rid> <versione> <cartella pubblicata> <cartella di uscita>
set -euo pipefail
RID="$1"; VERSION="$2"; SRC="$3"; OUT="$4"
case "$RID" in
  linux-x64)   ARCH=x86_64 ;;
  linux-arm64) ARCH=aarch64 ;;
  *) echo "rid non gestito: $RID"; exit 1 ;;
esac
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
A="$(mktemp -d)/YA-MS.AppDir"
mkdir -p "$A/opt/ya-ms" "$A/usr/share/icons/hicolor/256x256/apps"
cp -R "$SRC/." "$A/opt/ya-ms/"
chmod 755 "$A/opt/ya-ms/YA-MS"
echo "$VERSION" > "$A/opt/ya-ms/VERSIONE_PACCHETTO"
cp "$ROOT/src/Assets/ya-ms-256.png" "$A/ya-ms.png"
cp "$ROOT/src/Assets/ya-ms-256.png" "$A/usr/share/icons/hicolor/256x256/apps/ya-ms.png"
cat > "$A/ya-ms.desktop" <<'EOF'
[Desktop Entry]
Type=Application
Name=YA-MS
Comment=Efficienza degli sciami meteorici per il meteor scatter
Exec=AppRun
Icon=ya-ms
Terminal=false
Categories=HamRadio;Science;Utility;
EOF
cat > "$A/AppRun" <<'EOF'
#!/bin/sh
# YA-MS: copia il programma in ~/YA-MS (solo la prima volta o con una versione nuova) e lo avvia.
HERE="$(dirname "$(readlink -f "$0")")"
DEST="$HOME/YA-MS"
NEW="$(cat "$HERE/opt/ya-ms/VERSIONE_PACCHETTO" 2>/dev/null)"
OLD="$(cat "$DEST/VERSIONE_PACCHETTO" 2>/dev/null)"
if [ ! -x "$DEST/YA-MS" ] || [ "$NEW" != "$OLD" ]; then
  mkdir -p "$DEST"
  cp -R "$HERE/opt/ya-ms/." "$DEST/"
  chmod +x "$DEST/YA-MS"
fi
cd "$DEST" && exec "$DEST/YA-MS" "$@"
EOF
chmod 755 "$A/AppRun"
T="$(mktemp -d)"
curl -fsSL -o "$T/appimagetool" "https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-$(uname -m).AppImage"
chmod +x "$T/appimagetool"
mkdir -p "$OUT"
ARCH=$ARCH "$T/appimagetool" --appimage-extract-and-run "$A" "$OUT/YA-MS-${VERSION}-${ARCH}.AppImage"
ls -la "$OUT/YA-MS-${VERSION}-${ARCH}.AppImage"
