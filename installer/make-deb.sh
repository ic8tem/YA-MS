#!/usr/bin/env bash
# YA-MS - pacchetto .deb (Debian, Ubuntu, Mint, Raspberry Pi OS).
# Il pacchetto mette il programma in /opt/ya-ms; al primo avvio (e a ogni nuova versione) il lanciatore
# /usr/bin/ya-ms lo copia nella cartella personale ~/YA-MS e lo avvia da li': cosi' la cartella data resta
# accanto al programma, scrivibile dall'utente, e non si scrive nulla altrove.
# Uso: installer/make-deb.sh <rid> <versione> <cartella pubblicata> <cartella di uscita>
set -euo pipefail
RID="$1"; VERSION="$2"; SRC="$3"; OUT="$4"
case "$RID" in
  linux-x64)   ARCH=amd64 ;;
  linux-arm64) ARCH=arm64 ;;
  linux-arm)   ARCH=armhf ;;
  *) echo "rid non gestito: $RID"; exit 1 ;;
esac
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PKG="$(mktemp -d)/ya-ms_${VERSION}_${ARCH}"

install -d "$PKG/DEBIAN" "$PKG/opt/ya-ms" "$PKG/usr/bin" "$PKG/usr/share/applications" \
           "$PKG/usr/share/icons/hicolor/256x256/apps" "$PKG/usr/share/doc/ya-ms"
cp -R "$SRC/." "$PKG/opt/ya-ms/"
chmod 755 "$PKG/opt/ya-ms/YA-MS"
echo "$VERSION" > "$PKG/opt/ya-ms/VERSIONE_PACCHETTO"
install -m 644 "$ROOT/src/Assets/ya-ms-256.png" "$PKG/usr/share/icons/hicolor/256x256/apps/ya-ms.png"
install -m 644 "$ROOT/README.md" "$PKG/usr/share/doc/ya-ms/README.md"
printf "YA-MS - a cura di Costantino Cerrotta IC8TEM\nhttps://github.com/ic8tem/YA-MS\n" > "$PKG/usr/share/doc/ya-ms/copyright"
chmod 644 "$PKG/usr/share/doc/ya-ms/copyright"

cat > "$PKG/usr/bin/ya-ms" <<'EOF'
#!/bin/sh
# YA-MS: copia il programma in ~/YA-MS (solo la prima volta o con una versione nuova) e lo avvia.
# I file creati dal programma (data/config.ini, archivi, mappa) non vengono toccati.
DEST="$HOME/YA-MS"
NEW="$(cat /opt/ya-ms/VERSIONE_PACCHETTO 2>/dev/null)"
OLD="$(cat "$DEST/VERSIONE_PACCHETTO" 2>/dev/null)"
if [ ! -x "$DEST/YA-MS" ] || [ "$NEW" != "$OLD" ]; then
  mkdir -p "$DEST"
  cp -R /opt/ya-ms/. "$DEST/"
  chmod +x "$DEST/YA-MS"
fi
cd "$DEST" && exec "$DEST/YA-MS" "$@"
EOF
chmod 755 "$PKG/usr/bin/ya-ms"

cat > "$PKG/usr/share/applications/ya-ms.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=YA-MS
Comment=Efficienza degli sciami meteorici per il meteor scatter
Exec=/usr/bin/ya-ms
Icon=ya-ms
Terminal=false
Categories=HamRadio;Science;Utility;
EOF

SIZE=$(du -sk "$PKG" | cut -f1)
cat > "$PKG/DEBIAN/control" <<EOF
Package: ya-ms
Version: ${VERSION}
Section: hamradio
Priority: optional
Architecture: ${ARCH}
Installed-Size: ${SIZE}
Depends: libfontconfig1, libx11-6, libice6, libsm6
Maintainer: Costantino Cerrotta IC8TEM <ic8tem@users.noreply.github.com>
Homepage: https://github.com/ic8tem/YA-MS
Description: efficienza degli sciami meteorici per il meteor scatter
 Previsione e calcolo in diretta dell'efficienza degli sciami meteorici
 per i collegamenti radioamatoriali in meteor scatter (50-432 MHz).
 Al primo avvio il programma si copia in ~/YA-MS con la sua cartella data.
EOF

cat > "$PKG/DEBIAN/postinst" <<'EOF'
#!/bin/sh
set -e
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database -q || true
command -v gtk-update-icon-cache >/dev/null 2>&1 && gtk-update-icon-cache -q /usr/share/icons/hicolor || true
exit 0
EOF
chmod 755 "$PKG/DEBIAN/postinst"

mkdir -p "$OUT"
dpkg-deb --root-owner-group --build "$PKG" "$OUT/ya-ms_${VERSION}_${ARCH}.deb"
dpkg-deb --info "$OUT/ya-ms_${VERSION}_${ARCH}.deb" | head -12
