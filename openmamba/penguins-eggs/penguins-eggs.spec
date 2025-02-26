Name:          penguins-eggs
Version:       10.0.59
Release:       1mamba
Summary:       A console tool that allows you to remaster your system and redistribute it as live images on USB sticks or via PXE
Group:         System/Tools
Vendor:        openmamba
Distribution:  openmamba
Packager:      Piero Proietti <piero.proietti@gmail.com>
URL:           https://penguins-eggs.net/
Source:        https://github.com/pieroproietti/penguins-eggs.git/v%{version}/penguins-eggs-%{version}.tar.gz
License:       GPL
## AUTOBUILDREQ-BEGIN
## AUTOBUILDREQ-END
BuildRequires: nodejs pnpm
Requires:   bash-completion cryptsetup curl device-mapper dmraid dosfstools dracut efibootmgr fuse git jq lvm2 nodejs nvme-cli parted rsync sshfs wget xdg-user-dirs xorriso zstd

%description
A console tool that allows you to remaster your system and redistribute it as live images on USB sticks or via PXE.

#% debug_package
%global debug_package %{nil}  # no debug package

%prep
%setup -q

%build
# Based on Arch Linux pkgbuild
pnpm install
pnpm build  

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

install -Dm644 .oclif.manifest.json package.json -t %{buildroot}%{_prefix}/lib/%{name}
cp -r \
   addons \
   assets \
   bin \
   conf \
   ipxe \
   dracut \
   dist \
   eui \
   mkinitcpio \
   mkinitfs \
   node_modules \
   scripts \
   syslinux \
   %{buildroot}%{_prefix}/lib/%{name}

# Install bash-completion files
install -d %{buildroot}%{_datadir}/bash-completion/completions
ln -s /usr/lib/%{name}/scripts/eggs.bash \
   %{buildroot}%{_datadir}/bash-completion/completions/

# Install zsh-completion files
install -d %{buildroot}%{_datadir}/zsh/functions/Completion/Zsh/
ln -s ../lib/%{name}/scripts/_eggs \
   %{buildroot}%{_datadir}/zsh/functions/Completion/Zsh/

# Install man page
install -D -m0644 manpages/doc/man/eggs.1.gz -t %{buildroot}%{_mandir}/man1/

# Install desktop file
install -D -m0644 assets/%{name}.desktop -t %{buildroot}%{_datadir}/applications/

# Install icon
install -D -m0644 assets/eggs.png -t %{buildroot}%{_datadir}/pixmaps/

# Symlink executable
install -d %{buildroot}%{_bindir}
ln -s ../lib/%{name}/bin/run.js %{buildroot}%{_bindir}/eggs

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%{_bindir}/eggs
%{_datadir}/applications/penguins-eggs.desktop
%dir %{_prefix}/lib/penguins-eggs
%{_prefix}/lib/penguins-eggs/.oclif.manifest.json
%{_prefix}/lib/penguins-eggs/*
%{_datadir}/bash-completion/completions/eggs.bash
%{_datadir}/zsh/functions/Completion/Zsh/_eggs
%{_datadir}/pixmaps/eggs.png
%{_mandir}/man1/eggs.1*
%doc README.md

%%changelog
* Sat Dec 28 2024 Piero Proietti <piero.proietti@gmail.com> - 10.0.57-1mamba
* Wed Dec 18 2024 Piero Proietti <piero.proietti@gmail.com> - 10.0.56-1mamba
* Fri Dec 13 2024 Piero Proietti <piero.proietti@gmail.com> - 10.0.55-1mamba
* Sun Dec 01 2024 Silvan Calarco, Piero Proietti <piero.proietti@gmail.com> - 10.0.54-1mamba
