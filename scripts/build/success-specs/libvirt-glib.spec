# -*- rpm-spec -*-

Name: libvirt-glib
Version: 4.0.0
Release: 3%{?dist}
Summary: libvirt glib integration for events
License: LGPLv2+
URL: https://libvirt.org/
Source0: https://libvirt.org/sources/glib/%{name}-%{version}.tar.xz
Patch1: %{name}-%{version}-cast-align.patch

BuildRequires: meson
BuildRequires: glib2-devel
BuildRequires: libvirt-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libxml2-devel
BuildRequires: vala-tools
BuildRequires: gettext
BuildRequires: gtk-doc

%package devel
Summary: libvirt glib integration for events development files
Requires: %{name} = %{version}-%{release}

%package -n libvirt-gconfig
Summary: libvirt object APIs for processing object configuration

%package -n libvirt-gobject
Summary: libvirt object APIs for managing virtualization hosts

%package -n libvirt-gconfig-devel
Summary: libvirt object APIs for processing object configuration development files
Requires: libvirt-gconfig = %{version}-%{release}

%package -n libvirt-gobject-devel
Summary: libvirt object APIs for managing virtualization hosts development files
Requires: %{name}-devel = %{version}-%{release}
Requires: libvirt-gconfig-devel = %{version}-%{release}
Requires: libvirt-gobject = %{version}-%{release}
Requires: libvirt-devel

%description
This package provides integration between libvirt and the glib
event loop.

%description devel
This package provides development header files and libraries for
integration between libvirt and the glib event loop.

%description -n libvirt-gconfig
This package provides APIs for processing the object configuration
data

%description -n libvirt-gconfig-devel
This package provides development header files and libraries for
the object configuration APIs.

%description -n libvirt-gobject
This package provides APIs for managing virtualization host
objects

%description -n libvirt-gobject-devel
This package provides development header files and libraries for
managing virtualization host objects

%prep
%setup -q
%patch1 -p1

%build
%meson -Drpath=disabled
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%ldconfig_scriptlets

%ldconfig_scriptlets -n libvirt-gconfig

%ldconfig_scriptlets -n libvirt-gobject

%files -f %{name}.lang
%doc README COPYING AUTHORS NEWS
%{_libdir}/libvirt-glib-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtGLib-1.0.typelib

%files -n libvirt-gconfig
%{_libdir}/libvirt-gconfig-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtGConfig-1.0.typelib

%files -n libvirt-gobject
%{_libdir}/libvirt-gobject-1.0.so.*
%{_libdir}/girepository-1.0/LibvirtGObject-1.0.typelib

%files devel
%doc examples/event-test.c
%{_libdir}/libvirt-glib-1.0.so
%{_libdir}/pkgconfig/libvirt-glib-1.0.pc
%dir %{_includedir}/libvirt-glib-1.0
%dir %{_includedir}/libvirt-glib-1.0/libvirt-glib
%{_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib.h
%{_includedir}/libvirt-glib-1.0/libvirt-glib/libvirt-glib-*.h
%{_datadir}/gir-1.0/LibvirtGLib-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-glib
%{_datadir}/vala/vapi/libvirt-glib-1.0.deps
%{_datadir}/vala/vapi/libvirt-glib-1.0.vapi

%files -n libvirt-gconfig-devel
%doc examples/event-test.c
%{_libdir}/libvirt-gconfig-1.0.so
%{_libdir}/pkgconfig/libvirt-gconfig-1.0.pc
%dir %{_includedir}/libvirt-gconfig-1.0
%dir %{_includedir}/libvirt-gconfig-1.0/libvirt-gconfig
%{_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig.h
%{_includedir}/libvirt-gconfig-1.0/libvirt-gconfig/libvirt-gconfig-*.h
%{_datadir}/gir-1.0/LibvirtGConfig-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-gconfig
%{_datadir}/vala/vapi/libvirt-gconfig-1.0.deps
%{_datadir}/vala/vapi/libvirt-gconfig-1.0.vapi

%files -n libvirt-gobject-devel
%doc examples/event-test.c
%{_libdir}/libvirt-gobject-1.0.so
%{_libdir}/pkgconfig/libvirt-gobject-1.0.pc
%dir %{_includedir}/libvirt-gobject-1.0
%dir %{_includedir}/libvirt-gobject-1.0/libvirt-gobject
%{_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject.h
%{_includedir}/libvirt-gobject-1.0/libvirt-gobject/libvirt-gobject-*.h
%{_datadir}/gir-1.0/LibvirtGObject-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-gobject
%{_datadir}/vala/vapi/libvirt-gobject-1.0.deps
%{_datadir}/vala/vapi/libvirt-gobject-1.0.vapi

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 4.0.0-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 4.0.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 15 2021 Daniel P. Berrangé <berrange@redhat.com> - 4.0.0-1
- Rebased to 4.0.0 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
