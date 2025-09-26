# v7
# spec file for package calamares-eggs
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license certified by the Open Source Initiative as well as any license
# approved by the FSF as free software.
#

Name:           calamares-eggs
Version:        3.4.0
Release:        1
Summary:        Calamares installer customized for the Penguins' Eggs project
License:        GPL-3.0-or-later
Group:          System/YaST
URL:            https://codeberg.org/Calamares/calamares
Source0:        %{name}-%{version}.tar.gz

# Build dependencies
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig

# KDE Frameworks 6 dependencies
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kwidgetsaddons-devel

# Qt6 dependencies
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-linguist-devel

# Other build dependencies
BuildRequires:  pkgconfig(polkit-qt6-1)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  boost-devel
BuildRequires:  libpwquality-devel

# Additional build tools
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  shared-mime-info

# Runtime dependencies
Requires:       hwinfo
Requires:       python3-jsonschema
Requires:       python3-yaml
Requires:       squashfs
Requires:       parted
Requires:       util-linux
Requires:       dosfstools
Requires:       e2fsprogs

# Conflicts with the standard calamares package
Conflicts:      calamares

%description
Calamares is an installer framework. By mixing and matching C++ and Python
modules, a distribution can create a customized installer with its own branding.
This version is built for the Penguins' Eggs project with specific
customizations and module configurations.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_QT6=ON \
    -DINSTALL_CONFIG=ON \
    -DSKIP_MODULES="dracut dracutlukscfg dummycpp dummyprocess dummypython dummypythonqt initramfs initramfscfg interactiveterminal packagechooser packagechooserq services-openrc" \
    -DBUILD_TESTING=OFF \
    -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake_build

%install
%cmake_install

# Generate language files list (if translations exist)
%find_lang %{name} || touch %{name}.lang

# Validate desktop files (only if they exist)
if [ -f %{buildroot}%{_datadir}/applications/calamares.desktop ]; then
    desktop-file-validate %{buildroot}%{_datadir}/applications/calamares.desktop
fi

%files
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md
%{_bindir}/calamares
%{_libdir}/calamares/
%{_libdir}/libcalamares.so.*
%{_libdir}/libcalamaresui.so.*
%{_datadir}/calamares/
%{_datadir}/applications/calamares.desktop
%{_datadir}/icons/hicolor/scalable/apps/calamares.svg
%{_datadir}/polkit-1/actions/io.calamares.calamares.policy
%{_datadir}/locale/*/LC_MESSAGES/calamares-python.mo
%{_mandir}/man8/calamares.8*

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%changelog
* Fri Sep 26 2025 Your Name <your@email.com> - 3.4.0-1
- Initial release for openSUSE Tumbleweed
- Customized build for Penguins' Eggs project
- Built with Qt6 and KDE Frameworks 6
- Disabled unnecessary modules for eggs usage