#!/usr/bin/env bash
# YA-MS - pacchetto .rpm (Fedora, openSUSE, RHEL e derivate), ricavato dal .deb dello stesso rid:
# stessi file (/opt/ya-ms, lanciatore /usr/bin/ya-ms che al primo avvio copia il programma in ~/YA-MS,
# icona e voce di menu). Serve il comando rpmbuild (pacchetto "rpm" su Ubuntu).
# Uso: installer/make-rpm.sh <rid> <versione> <file .deb> <cartella di uscita>
set -euo pipefail
RID="$1"; VERSION="$2"; DEB="$3"; OUT="$4"
case "$RID" in
  linux-x64)   ARCH=x86_64 ;;
  linux-arm64) ARCH=aarch64 ;;
  linux-arm)   ARCH=armv7hl ;;
  *) echo "rid non gestito: $RID"; exit 1 ;;
esac
TOP="$(mktemp -d)"
TREE="$TOP/albero"
mkdir -p "$TREE" "$TOP/SPECS" "$TOP/RPMS"
dpkg-deb -x "$DEB" "$TREE"
# la versione rpm non accetta il trattino
RV="${VERSION//-/_}"

cat > "$TOP/SPECS/ya-ms.spec" <<EOF
Name:           ya-ms
Version:        ${RV}
Release:        1
Summary:        Efficienza degli sciami meteorici per il meteor scatter
License:        Freeware
URL:            https://github.com/ic8tem/YA-MS
Packager:       Costantino Cerrotta IC8TEM
AutoReqProv:    no
Requires:       fontconfig, libX11, libICE, libSM
%global debug_package %{nil}
%global __strip /bin/true
%global __os_install_post %{nil}
%global _build_id_links none

%description
Previsione e calcolo in diretta dell'efficienza degli sciami meteorici
per i collegamenti radioamatoriali in meteor scatter (50-432 MHz).
Al primo avvio il programma si copia in ~/YA-MS con la sua cartella data.
A cura di Costantino Cerrotta IC8TEM.

%install
mkdir -p %{buildroot}
cp -a ${TREE}/. %{buildroot}/

%post
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database -q || true
command -v gtk-update-icon-cache >/dev/null 2>&1 && gtk-update-icon-cache -q /usr/share/icons/hicolor || true
exit 0

%files
/opt/ya-ms
/usr/bin/ya-ms
/usr/share/applications/ya-ms.desktop
/usr/share/icons/hicolor/256x256/apps/ya-ms.png
%doc /usr/share/doc/ya-ms
EOF

rpmbuild --define "_topdir $TOP" --target "$ARCH" -bb "$TOP/SPECS/ya-ms.spec" >/dev/null
mkdir -p "$OUT"
cp "$TOP"/RPMS/*/ya-ms-*.rpm "$OUT/ya-ms-${VERSION}.${ARCH}.rpm"
rpm -qpi "$OUT/ya-ms-${VERSION}.${ARCH}.rpm" | head -8
