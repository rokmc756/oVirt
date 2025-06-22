Name:          ebay-cors-filter
Version:       1.0.1
Release:       4.1%{?dist}
Summary:       eBay CORS filter
License:       ASL 2.0
URL:           https://github.com/eBay/cors-filter
Source0:       https://github.com/eBay/cors-filter/archive/cors-filter-%{version}.tar.gz
Patch0:        %{name}-1.0.1-servlet.patch

BuildRequires: maven-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)

# Block packages from maven:3.8 to pass the build
BuildRequires: maven < 1:3.8.0
BuildRequires: maven-lib < 1:3.8.0
BuildRequires: maven-resolver < 1:1.7.0
BuildRequires: maven-shared-utils < 3.3.4-6
BuildRequires: maven-wagon < 3.5.0
BuildRequires: plexus-cipher < 1.8
BuildRequires: plexus-classworlds < 2.6.0-13
BuildRequires: plexus-containers-component-annotations < 2.1.1
BuildRequires: plexus-interpolation < 1.26-14
BuildRequires: plexus-sec-dispatcher < 1.5
BuildRequires: plexus-utils < 3.3.0-12
BuildRequires: sisu < 1:0.3.5

BuildArch:     noarch

%description
CORS (Cross Origin Resource Sharing) is a mechanism supported by W3C to
enable cross origin requests in web-browsers. CORS requires support from
both browser and server to work. This is a Java servlet filter
implementation of server-side CORS for web containers such as Apache
Tomcat.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n cors-filter-cors-filter-%{version}
%patch0 -p1

%build

%pom_remove_parent

sed -i 's/\r//' LICENSE NOTICE README.md
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md cors-flowchart.png
%dir %{_javadir}/%{name}
%dir %{_mavenpomdir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Thu Sep 22 2022 Martin Perina <mperina@redhat.com> - 1.0.1-4.1
- Block all packages from maven:3.8 module to pass the build on CS9

* Tue Feb 04 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-4
- Initial import on el8 from Fedora

* Thu Apr  9 2015 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-3
- Initial packaging based on Fedora spec file.
