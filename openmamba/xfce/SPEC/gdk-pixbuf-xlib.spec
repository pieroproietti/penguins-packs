%define majversion %(echo %version | cut -d. -f 1-2)

Name:          gdk-pixbuf-xlib
Epoch:         1
Version:       2.40.2
Release:       1mamba
Summary:       An image loading library (xlib deprecated API for integrating GdkPixbuf with Xlib data types)
Group:         System/Tools
Vendor:        openmamba
Distribution:  openmamba
Packager:      Silvan Calarco <silvan.calarco@mambasoft.it>
URL:           http://slackpacks.tchelinux.com.br/gdk-pixbuf
Source:        https://download.gnome.org/sources/gdk-pixbuf-xlib/%{majversion}/gdk-pixbuf-xlib-%{version}.tar.xz
License:       GPL
## AUTOBUILDREQ-BEGIN
BuildRequires: glibc-devel
BuildRequires: ldconfig
BuildRequires: libX11-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libglib-devel
## AUTOBUILDREQ-END
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
%{name} is an image loading library that can be extended by loadable modules for new image formats. It is used by toolkits such as GTK+ or clutter.

%package -n lib%{name}
Summary:       Shared libraries provided by %{name}
Group:         System/Libraries
Requires:      libgdk-pixbuf >= 2.42

%description -n lib%{name}
%{name} is an image loading library that can be extended by loadable modules for new image formats. It is used by toolkits such as GTK+ or clutter.
This package contains the %{name} shared libraries.


%package -n lib%{name}-devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      lib%{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n lib%{name}-devel
%{name} is an image loading library that can be extended by loadable modules for new image formats. It is used by toolkits such as GTK+ or clutter.
This package contains libraries and header files need for development.

%package apidocs
Summary:       %{name} API documentation
Group:         Documentation

%description apidocs
This package contains %{name} API documentation.

%debug_package

%prep
%setup -q

%build
%meson \
   -Ddocs=true

%meson_build

%install
[ "%{buildroot}" != / ] && rm -rf %{buildroot}
%meson_install

%clean
[ "%{buildroot}" != / ] && rm -rf %{buildroot}

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files -n lib%{name}
%defattr(-,root,root)
%{_libdir}/libgdk_pixbuf_xlib-2.0.so.*
%doc COPYING

%files -n lib%{name}-devel
%defattr(-,root,root)
%dir %{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf-xlib
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf-xlib/*.h
%{_libdir}/libgdk_pixbuf_xlib-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc

%changelog
* Tue Dec 01 2020 Silvan Calarco <silvan.calarco@mambasoft.it> 2.40.2-1mamba
- update to 2.40.2 (forked from libgdk-pixbuf)

* Sun May 10 2020 Silvan Calarco <silvan.calarco@mambasoft.it> 2.40.0-1mamba
- update to 2.40.0

* Fri Feb 09 2018 Silvan Calarco <silvan.calarco@mambasoft.it> 2.36.9-2mamba
- rebuilt to try to fix warning on libpng linking

* Sun Nov 19 2017 Automatic Build System <autodist@mambasoft.it> 2.36.9-1mamba
- automatic update by autodist

* Fri Aug 11 2017 Silvan Calarco <silvan.calarco@mambasoft.it> 2.36.8-1mamba
- update to 2.36.8

* Sat Apr 30 2016 Silvan Calarco <silvan.calarco@mambasoft.it> 2.34.0-1mamba
- update to 2.34.0

* Mon Jun 01 2015 Silvan Calarco <silvan.calarco@mambasoft.it> 2.30.8-6mamba
- run gtk-pixbuf-query-loaders with default directory

* Thu May 28 2015 Silvan Calarco <silvan.calarco@mambasoft.it> 2.30.8-5mamba
- multiarch cohexistence of gdk-pixbuf.loaders

* Fri Apr 03 2015 Silvan Calarco <silvan.calarco@mambasoft.it> 2.30.8-4mamba
- fix posttrans creation of gtk-pixbuf-{csource,pixdata} links

* Tue Mar 31 2015 Silvan Calarco <silvan.calarco@mambasoft.it> 2.30.8-3mamba
- use -32 or -64 suffix as more widely used

* Thu Mar 26 2015 Silvan Calarco <silvan.calarco@mambasoft.it> 2.30.8-2mamba
- provide gdk-pixbuf-query-loaders with arch suffix to support biarch environment

* Tue May 27 2014 Automatic Build System <autodist@mambasoft.it> 2.30.8-1mamba
- automatic version update by autodist

* Tue Mar 25 2014 Automatic Build System <autodist@mambasoft.it> 2.30.7-1mamba
- automatic version update by autodist

* Tue Mar 04 2014 Automatic Build System <autodist@mambasoft.it> 2.30.6-1mamba
- automatic version update by autodist

* Tue Feb 18 2014 Automatic Build System <autodist@mambasoft.it> 2.30.5-1mamba
- automatic version update by autodist

* Tue Feb 04 2014 Automatic Build System <autodist@mambasoft.it> 2.30.4-1mamba
- automatic version update by autodist

* Tue Jan 14 2014 Automatic Build System <autodist@mambasoft.it> 2.30.3-1mamba
- automatic version update by autodist

* Tue Dec 17 2013 Automatic Build System <autodist@mambasoft.it> 2.30.2-1mamba
- automatic version update by autodist

* Mon Nov 11 2013 Automatic Build System <autodist@mambasoft.it> 2.30.1-1mamba
- automatic version update by autodist

* Mon Oct 28 2013 Automatic Build System <autodist@mambasoft.it> 2.30.0-1mamba
- automatic version update by autodist

* Tue Oct 22 2013 Automatic Build System <autodist@mambasoft.it> 2.29.3-1mamba
- automatic update by autodist

* Thu May 02 2013 Automatic Build System <autodist@mambasoft.it> 2.29.0-1mamba
- automatic version update by autodist

* Mon Apr 15 2013 Automatic Build System <autodist@mambasoft.it> 2.28.1-1mamba
- automatic version update by autodist

* Tue Mar 26 2013 Automatic Build System <autodist@mambasoft.it> 2.28.0-1mamba
- automatic version update by autodist

* Tue Mar 19 2013 Automatic Build System <autodist@mambasoft.it> 2.27.3-1mamba
- automatic version update by autodist

* Fri Mar 08 2013 Automatic Build System <autodist@mambasoft.it> 2.27.2-1mamba
- automatic version update by autodist

* Mon Feb 11 2013 Automatic Build System <autodist@mambasoft.it> 2.27.1-1mamba
- automatic version update by autodist

* Mon Feb 11 2013 Silvan Calarco <silvan.calarco@mambasoft.it> 2.26.5-1mamba
- update to 2.26.5
- downgrade to stable release to fix
- don't build png as included loader

* Sat Feb 02 2013 Automatic Build System <autodist@mambasoft.it> 2.27.1-1mamba
- automatic version update by autodist

* Sun Jan 20 2013 Automatic Build System <autodist@mambasoft.it> 2.27.0-1mamba
- automatic version update by autodist

* Sat Nov 10 2012 Automatic Build System <autodist@mambasoft.it> 2.26.5-1mamba
- automatic version update by autodist

* Tue Sep 18 2012 Automatic Build System <autodist@mambasoft.it> 2.26.4-1mamba
- automatic version update by autodist

* Tue Aug 21 2012 Automatic Build System <autodist@mambasoft.it> 2.26.3-1mamba
- automatic version update by autodist

* Mon Aug 06 2012 Automatic Build System <autodist@mambasoft.it> 2.26.2-1mamba
- automatic version update by autodist

* Sat Apr 14 2012 Automatic Build System <autodist@mambasoft.it> 2.26.1-1mamba
- automatic version update by autodist

* Mon Apr 02 2012 Automatic Build System <autodist@mambasoft.it> 2.26.0-1mamba
- automatic version update by autodist

* Wed Mar 14 2012 Silvan Calarco <silvan.calarco@mambasoft.it> 2.24.1-2mamba
- rebuilt with --with-x11

* Mon Mar 12 2012 Automatic Build System <autodist@mambasoft.it> 2.24.1-1mamba
- update to 2.24.1

* Mon Dec 12 2011 Silvan Calarco <silvan.calarco@mambasoft.it> 2.24.0-2mamba
- move gir file from devel to main package

* Sat Aug 27 2011 Automatic Build System <autodist@mambasoft.it> 2.24.0-1mamba
- automatic version update by autodist

* Tue Jun 28 2011 Automatic Build System <autodist@mambasoft.it> 2.23.5-1mamba
- automatic update by autodist

* Tue Jun 14 2011 Automatic Build System <autodist@mambasoft.it> 2.23.4-1mamba
- automatic update by autodist

* Tue Apr 05 2011 Automatic Build System <autodist@mambasoft.it> 2.23.3-1mamba
- automatic update by autodist

* Sat Nov 06 2010 Automatic Build System <autodist@mambasoft.it> 2.22.1-1mamba
- automatic update to 2.22.1 by autodist

* Wed Oct 06 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 2.22.0-3mamba
- remove static package containing libtool *.la files that are needed in devel

* Mon Oct 04 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 2.22.0-2mamba
-  imported in openmamba devel

* Wed Sep 29 2010 gil <puntogil@libero.it> 2.22.0-1mamba
- update to 2.22.0
- renamed libgdk-pixbuf2

* Fri Jul 02 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 0.22.0-8mamba
- rebuilt with libpng 1.4

* Mon Jun 08 2009 Automatic Build System <autodist@mambasoft.it> 0.22.0-7mamba
- automatic rebuild by autodist

* Sun Jun 22 2008 Fabio Giani <fabio.giani@gmail.com> 0.22.0-6mamba
- update Vendor, Distribution, Packager, buildrequirements list

* Thu Apr 27 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.22.0-5qilnx
- p4

* Tue Apr 12 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.22.0-4qilnx
- fixed security issue QSA-2005-040 (CAN-2005-0891)

* Thu Nov 25 2004 Silvan Calarco <silvan.calarco@mambasoft.it> 0.22.0-3qilnx
- rebuilt removing wrong buildconflict libgnome1-devel (??) 

* Tue Oct 19 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.22.0-2qilnx
- security fixes: QSA-2004-048 (CAN-2004-0753, CAN-2004-[0782,0783,0788])
- add post/postun
- own /usr/lib/gdk-pixbuf, /usr/lib/gdk-pixbuf/loaders
- fixed underquoted m4 definition
- HTML documentation moved to devel package

* Tue Oct 07 2003 Silvan Calarco <silvan.calarco@mambasoft.it> 0.22.0-1qilnx
- first build
