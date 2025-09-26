
sudo zypper install rpm-build

# Crea la struttura
mkdir -p ~/rpmbuild/{SOURCES,SPECS,BUILD,RPMS,SRPMS}

# Copia i file al posto giusto
cp calamares-eggs-3.4.0.tar.gz ~/rpmbuild/SOURCES/
cp calamares-eggs.spec ~/rpmbuild/SPECS/

