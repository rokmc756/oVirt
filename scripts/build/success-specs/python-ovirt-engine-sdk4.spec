Name: python-ovirt-engine-sdk4
Summary: Python SDK for version 4 of the oVirt Engine API
Version: 4.6.2
Release: 1%{?release_suffix}%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://ovirt.org
Source: ovirt-engine-sdk-python-4.6.2.tar.gz

BuildRequires: gcc
BuildRequires: libxml2-devel
Requires: libxml2

%description
This package contains the Python SDK for version 4 of the oVirt Engine
API.

%package -n python3-ovirt-engine-sdk4
Summary: oVirt Engine Software Development Kit (Python)
BuildRequires: python3-devel
Requires: libxml2
Requires: python3
Requires: python3-pycurl >= 7.43.0-6
Requires: python3-six

%description -n python3-ovirt-engine-sdk4
This package contains the Python 3 SDK for version 4 of the oVirt Engine
API.

%if 0%{?rhel} >= 9
%package -n python3.11-ovirt-engine-sdk4
Summary: oVirt Engine Software Development Kit (Python)
BuildRequires: python3.11-devel
BuildRequires: python3.11-setuptools
Requires: libxml2
Requires: python3.11
Requires: python3.11-pycurl >= 7.43.0-6
Requires: python3.11-six

%description -n python3.11-ovirt-engine-sdk4
This package contains the Python 3.11 SDK for version 4 of the oVirt Engine
API.
%endif

%if 0%{?rhel} < 9
%package -n python3.11-ovirt-engine-sdk4
Summary: oVirt Engine Software Development Kit (Python)
BuildRequires: python3.11-devel
BuildRequires: python3.11-setuptools
Requires: libxml2
Requires: python3.11
Requires: python3.11-pycurl >= 7.43.0-6
Requires: python3.11-six

%description -n python3.11-ovirt-engine-sdk4
This package contains the Python 3.11 SDK for version 4 of the oVirt Engine
API.
%endif

%prep
%setup -c -q -n ovirt-engine-sdk-python-4.6.2

%build
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%py3_build
%if 0%{?rhel} < 9
%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%py3_build
%endif
%if 0%{?rhel} >= 9
%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%py3_build
%endif

%install
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%py3_install
%if 0%{?rhel} < 9
%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%py3_install
%endif
%if 0%{?rhel} >= 9
%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%py3_install
%endif

%files -n python3-ovirt-engine-sdk4
%doc README.adoc
%doc examples
%license LICENSE.txt
%define python3_pkgversion 3
%define __python3 /usr/bin/python3
%{python3_sitearch}/*

%if 0%{?rhel} < 9
%files -n python3.11-ovirt-engine-sdk4
%doc README.adoc
%doc examples
%license LICENSE.txt
%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%{python3_sitearch}/*
%endif

%if 0%{?rhel} >= 9
%files -n python3.11-ovirt-engine-sdk4
%doc README.adoc
%doc examples
%license LICENSE.txt
%define python3_pkgversion 3.11
%define __python3 /usr/bin/python3.11
%{python3_sitearch}/*
%endif

%changelog
* Thu Mar 23 2023 Martin Necas <mnecas@redhat.com> - 4.6.2-1
- Add Python 3.11 subpackage to be usable in ansible-core 2.14 for el8

* Wed Mar 1 2023 Martin Necas <mnecas@redhat.com> - 4.6.1-1
- Add Python 3.11 subpackage to be usable in ansible-core-2.14

* Fri Nov 25 2022 Martin Perina <mperina@redhat.com> - 4.6.0-1
- Update to model 4.6.0
- Switch from Python 3.8 to 3.9 on EL8 to support ansible-core >= 2.13

* Thu Aug 4 2022 Ori Liel <oliel@redhat.com> - 4.5.2
- Update to model 4.5.11

* Tue Mar 29 2022 Ori Liel <oliel@redhat.com> - 4.5.1
- Update to model 4.5.7

* Wed Oct 27 2021 Martin Necas <mnecas@redhat.com> - 4.5.0-1
- Update to model 4.5.0

* Thu Aug 5 2021 Martin Necas <mnecas@redhat.com> - 4.4.15-1
- Update to model 4.4.34
- Improve examples upload_disk, download_disk, backup_vm

* Thu Jul 2 2020 Martin Perina <mperina@redhat.com> - 4.4.4-1
- Update to model 4.4.17
- Improve examples code around image transfer features

* Thu Jun 06 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 4.3.1-1
- 4.3.1
- Adhere to Fedora packaging guidelines naming schema

* Wed Jun 14 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 4.2.0-1
- 4.2.0
