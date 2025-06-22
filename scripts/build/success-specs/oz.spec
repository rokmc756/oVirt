Name:    oz
Version: 0.18.0
Release: 3%{?dist}
Summary: Library and utilities for automated guest OS installs
License: LGPLv2
URL:     http://github.com/clalancette/oz

Source0: https://github.com/clalancette/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3
Requires: python3-lxml
Requires: python3-libguestfs >= 1.18
Requires: python3-libvirt
Requires: python3-m2crypto
Requires: python3-monotonic
Requires: python3-requests
# in theory, oz doesn't really require libvirtd to be local to operate
# properly.  However, because of the libguestfs manipulations, in practice
# it really does.  Make it depend on libvirt (so we get libvirtd) for now,
# unless/until we are able to make it really be remote.
Requires: libvirt-daemon-kvm
Requires: libvirt-daemon-driver-qemu
Requires: libvirt-daemon-config-network
%if 0%{?rhel} >= 9
# genisoimage has been dropped from RHEL 9
Requires: xorriso
%else
Requires: genisoimage
%endif
Requires: mtools
Requires: openssh-clients

%description
Oz is a set of libraries and utilities for doing automated guest OS
installations, with minimal input from the user.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/isocontent/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/isos/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/floppycontent/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/floppies/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/icicletmp/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/jeos/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/kernels/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/oz/screenshots/

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/oz
cp oz.cfg $RPM_BUILD_ROOT%{_sysconfdir}/oz

%post
if [ ! -f %{_sysconfdir}/oz/id_rsa-icicle-gen ]; then
   ssh-keygen -t rsa -b 2048 -N "" -f %{_sysconfdir}/oz/id_rsa-icicle-gen >& /dev/null
fi

%files
%license COPYING
%doc README examples
%dir %attr(0755, root, root) %{_sysconfdir}/oz/
%config(noreplace) %{_sysconfdir}/oz/oz.cfg
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/isocontent/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/isos/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/floppycontent/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/floppies/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/icicletmp/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/jeos/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/kernels/
%dir %attr(0755, root, root) %{_localstatedir}/lib/oz/screenshots/
%{_bindir}/oz-install
%{_bindir}/oz-generate-icicle
%{_bindir}/oz-customize
%{_bindir}/oz-cleanup-cache
%{_mandir}/man1/*
%{python3_sitelib}/oz
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Feb 16 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 0.18.0-3
- Fix deps on el8 and el9

* Wed Feb 16 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 0.18.0-2
- Rebuilt for CentOS Virtualization SIG

* Sat Feb 05 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.18.0-1
- Update to 0.18.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Adam Williamson <awilliam@redhat.com> - 0.17.0-20
- Try again to do what -19 probably failed to do (#2015490)

* Tue Oct 26 2021 Adam Williamson <awilliam@redhat.com> - 0.17.0-19
- Don't write kickstart so initial-setup won't think root pw is set (#2015490)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.17.0-17
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-16
- Fixes for anaconda changes

* Tue Feb 09 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-15
- fix patch for newer Fedora releases

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-13
- Add upstream PR for libvirt fixes

* Mon Oct 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-12
- Futher arm fixes, drop EOL conditionals

* Sun Oct 04 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-11
- Add missing fixes patch

* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.17.0-10
- Fix screenshots on armv7/aarch64, ARMv7 fixes, drop old release conditionals

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Dan Horák <dan[at]danny.cz> - 0.17.0-8
- fix compatibility with new qemu/libvirt on s390x

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-7
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.17.0-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.0-2
- Fix m2crypto python2 naming

* Tue Mar 26 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.0-1
- Conditionalise py3 support
- 0.17.0 is releases, minor cleanups

* Sat Mar 16 2019 Chris Lalancette <clalancette@gmail.com> - 0.17.0-0.3
- Update to latest upstream changes for Python 3

* Wed Mar 13 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.0-0.2
- Rebase to latest PR for ARMv7/aarch64 UEFI

* Thu Feb 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17.0-0.1
- Upstream git 0.17 snapshot
- ARMv7 fixes and support for UEFI
- UEFI fixes for x86_64 and aarch64

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Kevin Fenzi <kevin@scrye.com> - 0.16.0-7
- Drop unneeded sed fix.

* Mon Dec 10 2018 Kevin Fenzi <kevin@scrye.com> - 0.16.0-6
- Add patch to add rnd device to provide faster random on boot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.16.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Feb 18 2018 Chris Lalancette <clalancette@gmail.com> - 0.16.0-3
- Add s390x support patches

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Chris Lalancette <clalancette@gmail.com> - 0.16.0-1
- Release 0.16.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Chris Lalancette <clalancette@gmail.com> - 0.15.0-5
- Remove rawhide dependency on python-uuid

* Wed Aug 10 2016 Ian McLeod <imcleod@redhat.com> - 0.15.0-4
- Version bump to simplify upgrade for Fedora rel-eng

* Tue Aug 9 2016 Ian McLeod <imcleod@redhat.com> - 0.15.0-3
- Backport patches for ppc and aarch64 builds
- Backport patch related to configurable timeouts

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 28 2016 Chris Lalancette <clalancette@gmail.com> - 0.15.0-1
- Release 0.15.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 26 2015 Chris Lalancette <clalancette@gmail.com> - 0.14.0-1
- Release 0.14.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 07 2015 Chris Lalancette <clalancette@gmail.com> - 0.13.0-1
- Update to release 0.13.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Chris Lalancette <clalancette@gmail.com> - 0.12.0-2
- Add patch to first qcow2 image type

* Fri Jan  3 2014 Chris Lalancette <clalancette@gmail.com> - 0.12.0-1
- Update to release 0.12.0

* Thu Aug  8 2013 Chris Lalancette <clalancette@gmail.com> - 0.11.0-2
- Add in the upstream patch that fixes ICICLE generation with extra elements

* Sun Jul 28 2013 Chris Lalancette <clalancette@gmail.com> - 0.11.0-1
- Update to release 0.11.0

* Sat Mar 09 2013 Chris Lalancette <clalancette@gmail.com> - 0.10.0-1
- Update to release 0.10.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 18 2012 Chris Lalancette <clalancette@gmail.com> - 0.9.0-1
- Update to release 0.9.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Pádraig Brady <P@draigBrady.com> - 0.8.0-1
- Update to release 0.8.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Chris Lalancette <clalance@redhat.com> - 0.7.0-1
- Update to release 0.7.0

* Fri Aug 12 2011 Chris Lalancette <clalance@redhat.com> - 0.5.0-4
- Make oz require openssh-clients to get the ssh binary

* Wed Jul 27 2011 Chris Lalancette <clalance@redhat.com> - 0.5.0-3
- Minor cleanups to the spec file

* Tue Jul 05 2011 Pádraig Brady <P@draigBrady.com> - 0.5.0-2
- Adjust package as per updated Fedora standards

* Wed Jun 29 2011 Chris Lalancette <clalance@redhat.com> - 0.5.0-1
- Release 0.5.0

* Mon Jun 20 2011 Pádraig Brady <P@draigBrady.com> - 0.4.0-4
- Include examples/.

* Wed Jun 15 2011 Pádraig Brady <P@draigBrady.com> - 0.4.0-3
- Address rpmlint issues.

* Fri Jun 10 2011 Pádraig Brady <P@draigBrady.com> - 0.4.0-2
- Change to noarch.

* Tue May 24 2011 Chris Lalancette <clalance@redhat.com> - 0.4.0-1
- Release 0.4.0.

* Wed Mar 30 2011 Chris Lalancette <clalance@redhat.com> - 0.3.0-1
- Release 0.3.0.

* Wed Mar 16 2011 Chris Lalancette <clalance@redhat.com> - 0.2.0-1
- Release 0.2.0.

* Thu Feb  3 2011 Chris Lalancette <clalance@redhat.com> - 0.1.0-1
- Initial public release of Oz.

* Wed Nov  3 2010 Chris Lalancette <clalance@redhat.com> - 0.0.4-1
- Initial build.
