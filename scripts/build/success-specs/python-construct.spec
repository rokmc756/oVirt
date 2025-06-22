Summary:        A powerful declarative parser/builder for binary data
Name:           python-construct
Version:        2.10.67
Release:        1%{?dist}
License:        MIT
URL:            http://construct.readthedocs.org
Source0:        https://pypi.python.org/packages/source/c/construct/construct-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-setuptools
#BuildRequires:  python3-pytest

%global _description\
Construct is a powerful declarative parser (and builder) for binary\
data.\
\
Instead of writing imperative code to parse a piece of data, you\
declaratively define a data structure that describes your data. As\
this data structure is not code, you can use it in one direction to\
parse data into Pythonic objects, and in the other direction, convert\
(build) objects into binary data.

%description %_description
%package     -n python3-construct
Summary:        %summary
Requires:       python3-six
%description -n python3-construct %_description

%prep
%setup -q -n construct-%{version}

%build
%{py3_build}

%install
%{py3_install}

%check
# tests are not part of release tarball
#{__python3} -m pytest --benchmark-disable --showlocals

%files -n python3-construct
%license LICENSE
%doc README.rst
%{python3_sitelib}/construct
%{python3_sitelib}/construct-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 23 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.10.67-1
- 2.10.67

* Mon Apr 05 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.10.66-1
- 2.10.66

* Thu Mar 25 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.10.63-1
- 2.10.63

* Sun Mar 14 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.10.61-1
- 2.10.61

* Sat Feb 20 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.10.60-1
- 2.10.60

* Sun Feb 07 2021 Terje Rosten <terje.rosten@ntnu.no> - 2.10.59-1
- 2.10.59

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.10.56-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.10.56-1
- 2.10.56

* Tue Jan 28 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.10.55-1
- 2.10.55
- Python < 3.6 is not supported any longer

* Thu Jan 23 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.10.53-1
- 2.10.53

* Sun Jan 19 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.9.51-1
- 2.9.51

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.45-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.45-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.9.45-2
- Add python2 build deps to conditional
- Re-enable python2 builds on rawhide as it's still a build requirement

* Mon May 13 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.9.45-1
- 2.9.45
- Remove Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-17
- Rebuilt for Python 3.7

* Mon May 21 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.5.1-16
- Add patch to fix Python 3 import issue (rhbz#1560199)

* Mon Feb 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.5.1-15
- Clean up

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.5.1-12
- Python 2 binary package renamed to python2-construct
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 08 2013 Terje Rosten <terje.rosten@ntnu.no> - 2.5.1-1
- initial package
