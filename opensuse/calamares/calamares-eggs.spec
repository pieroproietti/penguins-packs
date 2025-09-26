#
# spec file for package calamares-eggs
#

# --- PREAMBOLO: Metadati e Dipendenze ---
# Corrisponde alle variabili pkgname, pkgver, depends, makedepends, etc.

# Il nome del pacchetto (senza versione)
Name:           calamares-eggs
Version:        3.4.0
# Il numero di release, incrementalo per ogni nuova build della stessa versione
Release:        1
# Breve descrizione (da pkgdesc)
Summary:        Calamares installer customized for the Penguins' Eggs project
License:        GPL-3.0-or-later
URL:            https://codeberg.org/Calamares/calamares
# Il sorgente che hai creato prima. %{name} e %{version} sono macro.
Source0:        %{name}-%{version}.tar.gz

# --- DIPENDENZE DI COMPILAZIONE (da makedepends) ---
# I pacchetti necessari solo per costruire il software.
# Su openSUSE, i pacchetti per lo sviluppo terminano spesso in "-devel".
# BuildRequires:  pkgconfig(boost)          # there is not on opensuse leap
# BuildRequires:  pkgconfig(libkpmcore)     # there is not on opensuse leap
# BuildRequires:  pkgconfig(libpwquality)   # there is not on opensuse leap
# BuildRequires:  pkgconfig(solid)          # there is not on opensuse leap
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig(polkit-qt6-1)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-quick-devel
BuildRequires:  qt6-quickwidgets-devel


# --- DIPENDENZE DI ESECUZIONE (da depends) ---
# I pacchetti necessari per far funzionare il software una volta installato.
# Molte di queste verranno rilevate automaticamente da rpmbuild,
# ma è buona norma dichiarare quelle più importanti.
Requires:       hwinfo
Requires:       python3-jsonschema
Requires:       python3-yaml
Requires:       squashfs
Requires:       libboost_program_options1_83_0

# --- DESCRIZIONE LUNGA ---
%description
Calamares is an installer framework. By mixing and matching C++ and Python
modules, a distribution can create a customized installer with its own branding.
This version is built for the Penguins' Eggs project.

# --- %prep: PREPARAZIONE SORGENTI (da prepare()) ---
# Questa sezione scompatta l'archivio.
%prep
# La macro %setup scompatta Source0 in automatico.
# L'opzione -q sta per "quiet".
%setup -q

# --- %build: COMPILAZIONE (da build()) ---
# Qui inseriamo i comandi cmake.
# --- %build: COMPILAZIONE (da build()) ---
%build
# Define the modules to skip as a simple, space-separated string.
# This is safe and avoids shell syntax errors.
%define skip_modules dracut dracutlukscfg dummycpp dummyprocess dummypython dummypythonqt initramfs initramfscfg interactiveterminal packagechooser packagechooserq services-openrc

# Use the standard openSUSE macros for configuration.
%cmake -G Ninja \
    -DWITH_QT6=ON \
    -DINSTALL_CONFIG=ON \
    -DSKIP_MODULES="%{skip_modules}" \
    -DBUILD_TESTING=OFF

# Use the standard macro to run the build (e.g., ninja).
%cmake_build

# --- %install: INSTALLAZIONE (da package()) ---
# Installa i file nella build root.
%install
# La macro %cmake_install esegue 'ninja install' o 'make install'
# usando DESTDIR=%{buildroot}
%cmake_install

# --- %files: ELENCO FILE ---
# La parte più importante e diversa da Arch.
# Devi elencare tutti i file e le directory che il pacchetto deve contenere.
%files
# Aggiungi qui i file di licenza e documentazione
%license COPYING
# File eseguibile
%{_bindir}/calamares
# Librerie e moduli
%{_libdir}/calamares/
# Dati, icone, configurazioni, etc.
%{_datadir}/calamares/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/calamares.svg

# --- %changelog: CRONOLOGIA ---
%changelog
* Fri Sep 26 2025 Tuo Nome <tua@email.com> - 3.4.0-1
- Initial release for openSUSE.