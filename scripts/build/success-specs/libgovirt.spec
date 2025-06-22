# -*- rpm-spec -*-

%global with_gir 0

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%global with_gir 1
%endif

Summary: A GObject library for interacting with oVirt REST API
Name: libgovirt
Version: 0.3.8
Release: 5%{dist}
License: LGPLv2+
Source0: http://download.gnome.org/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
Source1: http://download.gnome.org/sources/libgovirt/0.3/%{name}-%{version}.tar.xz.sig
Source2: etrunko-57E1C130.keyring
URL: https://gitlab.gnome.org/GNOME/libgovirt

ExclusiveArch:  x86_64

BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: rest-devel >= 0.7.92
%if %{with_gir}
BuildRequires: gobject-introspection-devel
%endif
#needed for make check
BuildRequires: glib-networking
BuildRequires: dconf
#needed for GPG signature check
BuildRequires: gnupg2
BuildRequires: make

%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package devel
Summary: Libraries, includes, etc. to compile with the libgovirt library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel

%description devel
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

Libraries, includes, etc. to compile with the libgovirt library

%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%if %{with_gir}
%global gir_arg --enable-introspection=yes
%else
%global gir_arg --enable-introspection=no
%endif

%configure %{gir_arg}
%__make %{?_smp_mflags} V=1

%install
%__make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name} --with-gnome

%check
make check

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING MAINTAINERS README
%{_libdir}/%{name}.so.2*
%if %{with_gir}
%{_libdir}/girepository-1.0/GoVirt-1.0.typelib
%endif

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/govirt-1.0/
%dir %{_includedir}/govirt-1.0/govirt/
%{_includedir}/govirt-1.0/govirt/*.h
%{_libdir}/pkgconfig/govirt-1.0.pc
%if %{with_gir}
%{_datadir}/gir-1.0/GoVirt-1.0.gir
%endif

%changelog
* Tue Dec 14 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 0.3.8-5.el9
- Rebuilt for CentOS Virt SIG
- Source: http://ftp.redhat.com/pub/redhat/linux/enterprise/9Base/en/RHEV/SRPMS/libgovirt-0.3.8-4.el9ev.src.rpm

* Mon Aug 16 2021 Uri Lublin <uril@redhat.com> - 0.3.8-4.el9ev
- Rebuilt following glibc 2.34 rebase
  Related: rhbz#1991688

* Wed Jun 30 2021 Uri Lublin <uril@redhat.com> - 0.3.8-3.el9ev
- Rebuilt for RHV
  Related: rhbz#1949046

* Wed Feb 24 2021 Eduardo Lima (etrunko) <etrunko@redhat.com> - 0.3.8-1
- Update to 0.3.8 release

