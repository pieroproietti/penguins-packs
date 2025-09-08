# el9
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

%global app_name penguins-eggs
%global nodejs_prefix %{_prefix}/lib/%{app_name}

# Non generare il pacchetto di debug, che causa problemi con i binari pre-compilati
%global debug_package %{nil}

%_bootloadersver 25.9.0

Name:           %{app_name}
Version:        25.9.8
Release:        1%{?dist}
Summary:        A console tool to remaster your system and create live images
# rimuove scoperta dipendenze
AutoReqProv: no

License:        GPL-3.0-or-later
URL:            https://penguins-eggs.net/
Source0:        https://github.com/pieroproietti/penguins-eggs/archive/v%{version}/%{app_name}-%{version}.tar.gz
#Source1:        https://github.com/pieroproietti/penguins-eggs/releases/download/v%{version}/bootloaders.tar.gz
Source1:        https://github.com/pieroproietti/penguins-bootloaders/releases/download/v%%{_bootloadersver}/bootloaders.tar.gz"


# Provides a virtual dependency for the bundled nodejs modules
# This is a good practice followed by Fedora and applicable here too.
Provides:       bundled(nodejs-module)

# BuildRequires for Rocky Linux / RHEL systems
# Use nodejs-devel which includes npm. pnpm is not in the default repos.
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs

# Dependencies artd
Requires:       bash-completion 
Requires:       cryptsetup 
Requires:       curl 
Requires:       device-mapper 
Requires:       dosfstools 
Requires:       dracut 
Requires:       dracut-live 
Requires:       fuse 
Requires:       git 
Requires:       jq 
Requires:       lvm2 
Requires:       nodejs
Requires:       nvme-cli 
Requires:       parted
Requires:       rsync 
Requires:       sshfs 
Requires:       squashfs-tools 
Requires:       wget 
Requires:       xdg-user-dirs 
Requires:       xorriso 
Requires:       zstd

%description
A console tool that allows you to remaster your system and redistribute it as live images on USB sticks or via PXE.

%prep
%setup -q -n %{app_name}-%{version}

# >> ESTRAI BOOTLOADERS DA SOURCE1
tar -xzf %{SOURCE1} -C ../

%build
# Use npm which is standard on Rocky/RHEL systems
sudo npm install -g pnpm
pnpm i
pnpm run build

%install
# Install main application files
install -d -m 755 %{buildroot}%{nodejs_prefix}
install -m 644 .oclif.manifest.json package.json -t %{buildroot}%{nodejs_prefix}

# Copy necessary directories
cp -r \
    addons \
    assets \
    bin \
    conf \
    dracut \
    dist \
    eui \
    node_modules \
    scripts \
    %{buildroot}%{nodejs_prefix}/

# >> SOVRASCRIVI CON I BOOTLOADERS CORRETTI
cp -r ../bootloaders %{buildroot}%{nodejs_prefix}/


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
#%license LICENSE
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
* Sat Jul 19 2025 Rocky Packager <packager@rockylinux.org> - 25.7.14-2
- Initial package for Rocky Linux, adapted from Fedora spec.
- Switched from pnpm to npm for build process.
