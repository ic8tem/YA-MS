#!/bin/sh
# YA-MS - installazione per Linux nella cartella personale ~/YA-MS (programma e cartella data insieme)
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/YA-MS"
echo "Installo YA-MS in $DEST"
mkdir -p "$DEST"
# copia tutto; i file creati dal programma (config.ini, archivi, mappa) restano
cp -R "$SRC/." "$DEST/"
rm -f "$DEST/installa.sh"
chmod +x "$DEST/YA-MS"
mkdir -p "$HOME/.local/share/applications" "$HOME/.local/share/icons/hicolor/256x256/apps"
cp "$DEST/ya-ms.png" "$HOME/.local/share/icons/hicolor/256x256/apps/ya-ms.png"
cat > "$HOME/.local/share/applications/ya-ms.desktop" <<DESK
[Desktop Entry]
Type=Application
Name=YA-MS
Comment=Efficienza degli sciami meteorici per il meteor scatter
Exec="$DEST/YA-MS"
Path=$DEST
Icon=ya-ms
Terminal=false
Categories=HamRadio;Science;Utility;
DESK
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$HOME/.local/share/applications" || true
echo "Fatto. Avvia YA-MS dal menu delle applicazioni oppure con: $DEST/YA-MS"
