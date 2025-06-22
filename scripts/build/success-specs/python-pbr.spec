%global pypi_name pbr
%global commitId 5150198c294802f82ddc7ed5765546653bc19adf

%if "%{?rhel}" == "8"
%global with_python38 1
%undefine __brp_mangle_shebangs
%else
%global with_python38 0
%endif

Name:           python-%{pypi_name}
Version:        5.5.1
Release:        7.2%{?dist}
Summary:        Python Build Reasonableness

License:        ASL 2.0
URL:            https://opendev.org/openstack/pbr.git
Source0:        python-pbr-5150198c294802f82ddc7ed5765546653bc19adf.tar.gz

BuildArch:      noarch

%description
PBR is a library that injects some useful and sensible default behaviors into
your setuptools run. It started off life as the chunks of code that were copied
between all of the OpenStack projects. Around the time that OpenStack hit 18
different projects each with at least 3 active branches, it seems like a good
time to make that code into a proper re-usable library.

%package -n python3-%{pypi_name}
Summary:        Python Build Reasonableness
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sed
Requires:       git-core

# /usr/bin/pbr moved from:
Conflicts:      python2-%{pypi_name} < 5.4.3-2

%description -n python3-%{pypi_name}
Manage dynamic plugins for Python applications

%if %{with_python38}
%package -n python38-%{pypi_name}
Summary:        Python Build Reasonableness
BuildRequires:  python38-devel
BuildRequires:  python38-setuptools
Requires:       git-core

# /usr/bin/pbr moved from:
Conflicts:      python2-%{pypi_name} < 5.4.3-2

%description -n python38-%{pypi_name}
Manage dynamic plugins for Python applications
%endif

%prep
%autosetup -n python-%{pypi_name}-%{commitId}

rm -rf {test-,}requirements.txt pbr.egg-info/requires.txt

cat > PKG-INFO<<EOF
Metadata-Version: 1.0
Name: pbr
Version: 5.5.1
Summary: %{summary}
License: UNKNOWN
Platform: UNKNOWN
EOF

%build
export SKIP_PIP_INSTALL=1
%if %{with_python38}
%define python3_pkgversion 38
%define __python3 /usr/bin/python3.8
%py3_build
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%endif

%py3_build

%install
%if %{with_python38}
%define python3_pkgversion 38
%define __python3 /usr/bin/python3.8
%py3_install
mv %{buildroot}%{_bindir}/pbr %{buildroot}%{_bindir}/pbr-3.8
rm -rf %{buildroot}%{python3_sitelib}/pbr/tests
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%endif

%py3_install

mv %{buildroot}%{_bindir}/pbr %{buildroot}%{_bindir}/pbr-3
rm -rf %{buildroot}%{python3_sitelib}/pbr/tests

%files -n python3-pbr
%license LICENSE
%doc README.rst
%attr(755, root, root) %{_bindir}/pbr-3
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%if %{with_python38}
%files -n python38-pbr
%define python3_pkgversion 38
%define __python3 /usr/bin/python3.8
%license LICENSE
%doc README.rst
%{_bindir}/pbr-3.8
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{pypi_name}/
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%endif

%changelog
* Mon Apr 04 2022 Martin Perina <mperina@redhat.com> - 5.5.1-7.2
- Improve Python 3.8 support

* Fri Mar 25 2022 Martin Perina <mperina@redhat.com> - 5.5.1-7.1
- Add support for both Python 3 and Python 3.8

* Wed Mar 31 2021 Yanis Guenane <yguenane@redhat.com> - 5.5.1-2
- Update to python3.8

* Thu Oct 29 2020 Joel Capitao <jcapitao@redhat.com> - 5.5.1-1
- Update to 5.5.1 (rhbz#1684239)

* Mon Sep 14 2020 Joel Capitao <jcapitao@redhat.com> - 5.5.0-1
- Update to 5.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-5
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-4
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-2
- Subpackage python2-pbr has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 10 2019 Yatin Karel <ykarel@redhat.com> - 5.4.3-1
- Update to 5.4.3

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-7
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-6
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Yatin Karel <ykarel@redhat.com> - 5.1.2-3
- Fix FTBFS: No more python2-openstackdocstheme

* Thu Feb 07 2019 Javier Peña <jpena@redhat.com> - 5.1.2-2
- Fix doc requirements

* Thu Feb 07 2019 Javier Peña <jpena@redhat.com> - 5.1.2-1
- Update to 5.1.2 (rhbz#1671081)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Matthias Runge <mrunge@redhat.com> - 4.2.0-1
- update to 4.2.0 (rhbz#1605192)

* Wed Aug  8 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 4.1.1-2
- Add runtime requirement to git-core

* Fri Jul 20 2018 Matthias Runge <mrunge@redhat.com> - 4.1.1-1
- rebase to 4.1.1 (rhbz#1605192)

* Wed Jul 18 2018 Haïkel Guémar  <hguemar@fedoraproject.org> - 4.1.0-2
- Add dependency to setuptools (RHBZ#1601767)

* Tue Jul 17 2018 Matthias Runge <mrunge@redhat.com> - 4.1.0-1
- update to 4.1.0 (rhbz#1561252)
- modernize spec

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-8
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 15 2018 Tomas Orsava <torsava@redhat.com> - 3.1.1-6
- Switch %%python macro to %%python2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 3.1.1-4
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jan Beran <jberan@redhat.com> 3.1.1-2
- Fix of missing Python 3 version of executables in python3-pbr subpackage

* Wed Jun 28 2017 Alan Pevec <alan.pevec@redhat.com> 3.1.1-1
- Update to 3.1.1

* Fri Mar  3 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.0-1
- Upstream 2.0.0
- Drop upstreamed patch

* Sat Feb 18 2017 Alan Pevec <apevec AT redhat.com> - 1.10.0-4
- Fix newer Sphinx and Python 3.5 support LP#1379998

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-2
- Rebuild for Python 3.6

* Wed Oct 12 2016 Alan Pevec <apevec AT redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Paul Belanger <pabelanger@redhat.com> 1.8.1-3
- Provide python2-pbr (rhbz#1282126)
- minor spec cleanup

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 12 2015 Alan Pevec <alan.pevec@redhat.com> 1.8.1-1
- Update to 1.8.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 14 2015 Alan Pevec <alan.pevec@redhat.com> 1.8.0-1
- Update to upstream 1.8.0

* Tue Sep 08 2015 Alan Pevec <alan.pevec@redhat.com> 1.7.0-1
- Update to upstream 1.7.0

* Mon Aug 31 2015 Matthias Runge <mrunge@redhat.com> - 1.6.0-1
- update to upstream 1.6.0 (rhbz#1249840)

* Sat Aug 15 2015 Alan Pevec <alan.pevec@redhat.com> 1.5.0-1
- Update to upstream 1.5.0

* Wed Jul 15 2015 Alan Pevec <alan.pevec@redhat.com> 1.3.0-1
- Update to upstream 1.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Alan Pevec <apevec@redhat.com> - 0.11.0-1
- update to 0.11.0

* Fri Mar 20 2015 Alan Pevec <apevec@redhat.com> - 0.10.8-1
- update to 0.10.8

* Mon Dec 29 2014 Alan Pevec <apevec@redhat.com> - 0.10.7-1
- update to 0.10.7

* Tue Nov 25 2014 Matthias Runge <mrunge@redhat.com> - 0.10.0-1
- update to 0.10.0 (rhbz#1191232)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 30 2014 Matthias Runge <mrunge@redhat.com> - 0.8.0-1
- update to 0.8.0 (rhbz#1078761)

* Tue Apr 08 2014 Matthias Runge <mrunge@redhat.com> - 0.7.0-2
- Added python3 subpackage.
- slight modification of Ralph Beans proposal

* Mon Mar 24 2014 Matthias Runge <mrunge@redhat.com> - 0.7.0-1
- update to 0.7.0 (rhbz#1078761)

* Tue Feb 11 2014 Matthias Runge <mrunge@redhat.com> - 0.6.0-1
- update to 0.6.0 (rhbz#1061124)

* Fri Nov 01 2013 Matthias Runge <mrunge@redhat.com> - 0.5.23-1
- update to 0.5.23 (rhbz#1023926)

* Tue Aug 13 2013 Matthias Runge <mrunge@redhat.com> - 0.5.21-2
- add requirement python-pip (rhbz#996192)
- remove requirements.txt

* Thu Aug 08 2013 Matthias Runge <mrunge@redhat.com> - 0.5.21-1
- update to 0.5.21 (rhbz#990008)

* Fri Jul 26 2013 Matthias Runge <mrunge@redhat.com> - 0.5.19-2
- remove one buildrequires: python-sphinx

* Mon Jul 22 2013 Matthias Runge <mrunge@redhat.com> - 0.5.19-1
- update to python-pbr-0.5.19 (rhbz#983008)

* Mon Jun 24 2013 Matthias Runge <mrunge@redhat.com> - 0.5.17-1
- update to python-pbr-0.5.17 (rhbz#976026)

* Wed Jun 12 2013 Matthias Runge <mrunge@redhat.com> - 0.5.16-1
- update to 0.5.16 (rhbz#973553)

* Tue Jun 11 2013 Matthias Runge <mrunge@redhat.com> - 0.5.14-1
- update to 0.5.14 (rhbz#971736)

* Fri May 31 2013 Matthias Runge <mrunge@redhat.com> - 0.5.11-2
- remove requirement setuptools_git
- fix docs build under rhel

* Fri May 17 2013 Matthias Runge <mrunge@redhat.com> - 0.5.11-1
- update to 0.5.11 (rhbz#962132)
- disable tests, as requirements can not be fulfilled right now

* Thu Apr 25 2013 Matthias Runge <mrunge@redhat.com> - 0.5.8-1
- Initial package.
