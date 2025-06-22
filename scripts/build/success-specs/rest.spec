Name:          rest
Version:       0.8.1
Release:       11%{?dist}
Summary:       A library for access to RESTful web services

License:       LGPLv2
URL:           http://www.gnome.org
Source0:       http://download.gnome.org/sources/%{name}/0.8/%{name}-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=1445700
Patch0:        rest-0.8.0-fix-the-XML-test.patch

BuildRequires: make
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: gtk-doc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent 
remote objects, which methods can then be called on. The majority of services 
don't actually adhere to this strict definition. Instead, their RESTful end 
point usually has an API that is just simpler to use compared to other types 
of APIs they may support (XML-RPC, for instance). It is this kind of API that 
this library is attempting to support.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -vif
%configure --disable-static --enable-gtk-doc --enable-introspection=yes

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/librest-0.7.so.0
%{_libdir}/librest-0.7.so.0.0.0
%{_libdir}/librest-extras-0.7.so.0
%{_libdir}/librest-extras-0.7.so.0.0.0
%{_libdir}/girepository-1.0/Rest-0.7.typelib
%{_libdir}/girepository-1.0/RestExtras-0.7.typelib

%files devel
%{_includedir}/rest-0.7
%{_libdir}/pkgconfig/rest*
%{_libdir}/librest-0.7.so
%{_libdir}/librest-extras-0.7.so
%{_datadir}/gtk-doc/html/%{name}*0.7
%{_datadir}/gir-1.0/Rest-0.7.gir
%{_datadir}/gir-1.0/RestExtras-0.7.gir

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.8.1-11
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.8.1-10
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Debarshi Ray <rishi@fedoraproject.org> - 0.8.1-3
- Fix the XML test

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 17 2017 Debarshi Ray <rishi@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 18 2016 Christophe Fergeau <cfergeau@redhat.com> 0.8.0-1
- Update to 0.8.0 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.93-1
- Update to 0.7.93
- Tighten deps with the _isa macro
- Don't manually require pkgconfig; rpmbuild generates this automatically
- Use license macro for the COPYING file

* Fri Jan  9 2015 Debarshi Ray <rishi@fedoraproject.org> 0.7.92-6
- Backport upstream patch to fix a memory error (GNOME #742644)

* Wed Sep  3 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.92-5
- Update to 0.7.92

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug  6 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.91-4
- Drop old patch that doesn't appear to be needed any more and causes build issues

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.7.91-3
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Richard Hughes <rhughes@redhat.com> - 0.7.91-1
- Update to 0.7.91

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Matthias Clasen <mclasen@redhat.com> 0.7.90-4
- Rebuild with newer gtk-doc to fix multilib issue

* Sat Apr 13 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.90-3
- Run autoreconf for aarch64 (RHBZ 926440)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.90-1
- Release 0.7.90

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.12-1
- Release 0.7.12. Fixes CVE-2011-4129 RHBZ 752022

* Fri Oct 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.11-1
- Release 0.7.11

* Sun Apr 24 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.10-1
- Update to 0.7.10

* Sun Apr  3 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.9-1
- Update to 0.7.9

* Wed Mar 23 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.8-1
- Update to 0.7.8

* Tue Feb 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.6-1
- Update to 0.7.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.5-1
- Update to 0.7.5
- Now its on gnome we have official tar file releases

* Wed Sep 29 2010 jkeating - 0.7.3-2
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.3-1
- Update to 0.7.3

* Mon Aug 30 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.2-1
- Update to 0.7.2

* Thu Aug  5 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.0-1
- Update to 0.7.0

* Sun Jul 11 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.4-1
- Update to 0.6.4

* Wed May 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.3-2
- some cleanups and fixes

* Wed May 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.3-1
- Update to 0.6.3, update url and source details, enable introspection

* Mon Feb 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-4
- Add patch to fix DSO linking. Fixes bug 564764

* Mon Jan 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-3
- Bump build

* Mon Jan 25 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-2
- Move to official tarball release of 0.6.1

* Sat Oct 10 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-1
- New upstream 0.6.1 release

* Wed Aug 19 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.6-1
- New upstream 0.6 release

* Fri Aug  7 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.5-3
- A few minor spec file cleanups

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.5-1
- Update to 0.5

* Mon Jun 22 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.4-1
- Update to 0.4

* Wed Jun 17 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-1
- Initial packaging
