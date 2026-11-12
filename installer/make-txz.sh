#!/usr/bin/env bash
# YA-MS - pacchetto Slackware (.txz), ricavato dal .deb dello stesso rid: stessi file del .deb
# (/opt/ya-ms, lanciatore /usr/bin/ya-ms che al primo avvio copia il programma in ~/YA-MS).
# Si installa da root con: installpkg ya-ms-<versione>-<arch>-1_ic8tem.txz
# Uso: installer/make-txz.sh <rid> <versione> <file .deb> <cartella di uscita>
set -euo pipefail
RID="$1"; VERSION="$2"; DEB="$3"; OUT="$4"
case "$RID" in
  linux-x64)   ARCH=x86_64 ;;
  linux-arm64) ARCH=aarch64 ;;
  linux-arm)   ARCH=arm ;;
  *) echo "rid non gestito: $RID"; exit 1 ;;
esac
T="$(mktemp -d)"
dpkg-deb -x "$DEB" "$T"
mkdir -p "$T/install"
# slack-desc: 11 righe che iniziano con il nome del pacchetto
cat > "$T/install/slack-desc" <<'EOF'
     |-----handy-ruler------------------------------------------------------|
ya-ms: ya-ms (efficienza degli sciami meteorici per il meteor scatter)
ya-ms:
ya-ms: Previsione e calcolo in diretta dell'efficienza degli sciami meteorici
ya-ms: per i collegamenti radioamatoriali in meteor scatter (50-432 MHz).
ya-ms: Al primo avvio il programma si copia in ~/YA-MS con la sua cartella
ya-ms: data. A cura di Costantino Cerrotta IC8TEM.
ya-ms:
ya-ms: https://github.com/ic8tem/YA-MS
ya-ms:
ya-ms:
ya-ms:
EOF
cat > "$T/install/doinst.sh" <<'EOF'
if [ -x /usr/bin/update-desktop-database ]; then /usr/bin/update-desktop-database -q usr/share/applications >/dev/null 2>&1; fi
if [ -x /usr/bin/gtk-update-icon-cache ]; then /usr/bin/gtk-update-icon-cache -q usr/share/icons/hicolor >/dev/null 2>&1; fi
EOF
SV="${VERSION//-/_}"
mkdir -p "$OUT"
tar -C "$T" --owner=0 --group=0 -cJf "$OUT/ya-ms-${SV}-${ARCH}-1_ic8tem.txz" install opt usr
ls -la "$OUT/ya-ms-${SV}-${ARCH}-1_ic8tem.txz"
