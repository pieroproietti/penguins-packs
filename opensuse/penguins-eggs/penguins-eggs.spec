# Disattiva la firma del pacchetto
%define _signature gpg
%define _gpg_name none

#
# spec file for package penguins-eggs
#
# Copyright (c) 2025 Piero Proietti
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Global variables
%global app_name penguins-eggs
%global nodejs_prefix %{_prefix}/lib/%{app_name}

# Non generare il pacchetto di debug
%global debug_package %{nil}

Name:           %{app_name}
Version:        25.7.14
# La convenzione di openSUSE per la release è iniziare da 0
Release:        1%{?dist}
Summary:        A console tool to remaster your system and create live images
# Manteniamo la disattivazione delle dipendenze automatiche a causa dei moduli nodejs inclusi (bundled)
AutoReqProv:    no

License:        GPL-3.0-or-later
URL:            https://penguins-eggs.net/
Source0:        https://github.com/pieroproietti/penguins-eggs/archive/v%{version}/%{app_name}-%{version}.tar.gz

# NOTA: La direttiva "Provides: bundled(nodejs-module)" è una convenzione di Fedora
# e viene omessa su openSUSE. La gestione dei moduli nodejs è affidata a pnpm.

# Dipendenze di build per openSUSE
BuildRequires:  gcc-c++
BuildRequires:  make
# openSUSE richiede versioni specifiche di nodejs e pnpm
BuildRequires:  nodejs
BuildRequires:  pnpm

# Dipendenze di runtime per openSUSE
Requires:       bash
Requires:       bash-completion
Requires:       cryptsetup
Requires:       curl
Requires:       device-mapper
Requires:       dosfstools
Requires:       dracut
Requires:       dracut-extra
Requires:       dracut-tools
Requires:       efibootmgr
Requires:       fuse
Requires:       git
Requires:       grub2-x86_64-efi
Requires:       jq
Requires:       lvm2
Requires:       nodejs
Requires:       nvme-cli
Requires:       rsync
Requires:       shadow
Requires:       squashfs
Requires:       sshfs
Requires:       wget
Requires:       xdg-user-dirs
Requires:       xorriso
Requires:       zstd

%description
A console tool that allows you to remaster your system and redistribute it as live images on USB sticks or via PXE.

%prep
%setup -q -n %{app_name}-%{version}

%build
# I comandi di build rimangono identici
pnpm install --frozen-lockfile
pnpm build

%install
# La sezione di installazione non richiede modifiche, usa macro standard
install -d -m 755 %{buildroot}%{nodejs_prefix}
install -m 644 .oclif.manifest.json package.json -t %{buildroot}%{nodejs_prefix}

# Copy necessary directories
cp -r \
    addons \
    assets \
    bin \
    bootloaders \
    conf \
    dracut \
    dist \
    eui \
    node_modules \
    scripts \
    %{buildroot}%{nodejs_prefix}/

# Install executable symlink
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{nodejs_prefix}/bin/run.js %{buildroot}%{_bindir}/eggs

# Install shell completions
install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions
ln -s %{nodejs_prefix}/scripts/eggs.bash %{buildroot}%{_datadir}/bash-completion/completions/eggs

install -d -m 755 %{buildroot}%{_datadir}/zsh/site-functions
ln -s %{nodejs_prefix}/scripts/_eggs %{buildroot}%{_datadir}/zsh/site-functions/_eggs

# Install man page
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 manpages/doc/man/eggs.1.gz %{buildroot}%{_mandir}/man1/eggs.1.gz

# Install desktop file and icon
install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 assets/%{app_name}.desktop %{buildroot}%{_datadir}/applications/%{app_name}.desktop
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 assets/eggs.png %{buildroot}%{_datadir}/pixmaps/eggs.png

%files
%doc README.md
%{_bindir}/eggs
%dir %{nodejs_prefix}
%{nodejs_prefix}/.oclif.manifest.json
%{nodejs_prefix}/package.json
%{nodejs_prefix}/addons/
%{nodejs_prefix}/assets/
%{nodejs_prefix}/bin/
%{nodejs_prefix}/bootloaders/
%{nodejs_prefix}/conf/
%{nodejs_prefix}/dist/
%{nodejs_prefix}/dracut/
%{nodejs_prefix}/eui/
%{nodejs_prefix}/node_modules/
%{nodejs_prefix}/scripts/
%{_datadir}/applications/%{app_name}.desktop
%{_datadir}/bash-completion/completions/eggs
%{_datadir}/zsh/site-functions/_eggs
%{_datadir}/pixmaps/eggs.png
%{_mandir}/man1/eggs.1.gz

%changelog
* Sat Jul 19 2025 Piero Proietti <piero.proietti@gmail.com> - 25.7.14-0
- Initial openSUSE package