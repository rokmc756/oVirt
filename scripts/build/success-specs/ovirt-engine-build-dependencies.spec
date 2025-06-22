Name:		ovirt-engine-build-dependencies
Version:	4.5.5
Release:	1%{?dist}
Summary:	oVirt Engine Build Dependencies
Group:		%{ovirt_product_group}
License:	ASL 2.0
URL:		http://www.ovirt.org
Source0:	%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	tar

Requires:	javapackages-filesystem


%description
%{name} provides build dependencies for oVirt Engine, so it is possible to build it without internet access.



%prep
%setup -c -q -T


%install
install -d -m 755  %{buildroot}%{_datadir}/%{name}/repository
tar -xf %{SOURCE0} -C %{buildroot}%{_datadir}/%{name}


%files
%{_datadir}/%{name}


%changelog
* Thu Nov 30 2022 Martin Perina <mperina@redhat.com> - 4.5.5-1
- Package dependencies for ovirt-engine 4.5.5

* Thu Nov 24 2022 Martin Perina <mperina@redhat.com> - 4.5.4-1
- Package dependencies for ovirt-engine 4.5.4

* Thu Sep 08 2022 Martin Perina <mperina@redhat.com> - 4.5.3-1
- Initial packaging of build dependencies for oVirt Engine 4.5.3
