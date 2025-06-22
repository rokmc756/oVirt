%global pypi_name jmespath

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        11.5%{?dist}
Summary:        JSON Matching Expressions

License:        MIT
URL:            https://github.com/jmespath/jmespath.py
Source0:        https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.

%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%package -n     python3-%{pypi_name}
Summary:        JSON Matching Expressions
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
# BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools

Supplements:    ansible

%description -n python3-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.

%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%package -n python3.11-%{pypi_name}
Summary:        JSON Matching Expressions
BuildRequires:  python3.11-devel
BuildRequires:  python3.11-setuptools

%description -n python3.11-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements from
a JSON document.
%define python3_pkgversion 3
%define __python3 /usr/bin/python3

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%py3_build

%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%py3_build "--executable=%{quote:/usr/bin/python3 -s}"
%define python3_pkgversion 3
%define __python3 /usr/bin/python3


%install
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%py3_install

%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%py3_install


%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%py3_install
mv %{buildroot}/%{_bindir}/jp.py %{buildroot}/%{_bindir}/jp.py-%{python3_version}
ln -sf %{_bindir}/jp.py-%{python3_version} %{buildroot}/%{_bindir}/jp.py-3
ln -sf %{_bindir}/jp.py-%{python3_version} %{buildroot}/%{_bindir}/jp.py


%check
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
nosetests-%{python3_version}


%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{_bindir}/jp.py
%{_bindir}/jp.py-3
%{_bindir}/jp.py-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%files -n python3.11-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.??.egg-info

%define python3_pkgversion 3
%define __python3 /usr/bin/python3

%changelog
* Tue Apr 04 2023 Martin Perina <mperina@redhat.com> - 0.9.0-11.5
- Fix incorrect Python 3.11 requirements for python3-jmespath package on EL8
- Simplify spec file

* Thu Mar 23 2023 Martin Necas <mnecas@redhat.com> - 0.9.0-11.4
- Add Python 3.11 subpackage to be usable in ansible-core-2.14 for cs8

* Wed Mar 01 2023 Martin Necas <mnecas@redhat.com> - 0.9.0-11.3
- Add Python 3.11 subpackage to be usable in ansible-core-2.14

* Fri Nov 18 2022 Martin Perina <mperina@redhat.com> - 0.9.0-11.2
- Replace Python 3.8 with 3.9 on EL8 to support ansible-core-2.13

* Wed Mar 23 2022 Martin Necas <mnecas@redhat.com> - 0.9.0-11.1
- Add Python 3.8 subpackage to be usable in ansible-core-2.12

* Mon Jan 14 2019 Pavel Cahyna <pcahyna@redhat.com> - 0.9.0-11
- Supplement: ansible, as we enable the json_query Jinja2 filter. RHBZ#1660559

* Fri Jun 15 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.9.0-10
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 27 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.0-4
- Fix python2 subpackage requiring python3 (RHBZ#1342501)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9.0-2
- Improve to set the Provides tag for EL6 too

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.9.0-1
- Upgrade to upstream current version
- Improve the spec file
- Make possible to build in EL6

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.5.0-1
- New version

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-2
- Add Python 3 support

* Fri Jul 25 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.4.1-1
- Initial packaging
