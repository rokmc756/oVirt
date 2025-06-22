Name:           mockito-junit-jupiter
Version:        3.12.4
Release:        0.1%{?dist}
Summary:        Mockito extension for JUnit5
License:        MIT
URL:            https://site.mockito.org/
BuildArch:      noarch

# Source tarball and the script to generate it
Source0:        mockito-%{version}.tar.gz

# A custom build script to allow building with maven instead of gradle
Source1:        mockito-junit-jupiter.pom

BuildRequires:  maven-local
BuildRequires:  maven
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)

%description
Mockito extension for JUnit5 testing framework, which eases mocks
initialization and handles strict stubbings.

%package javadoc
Summary: Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n mockito-%{version}/subprojects/junit-jupiter

# Use our custom build script
sed -e 's/@VERSION@/%{version}/' %{SOURCE1} > pom.xml

# Copy license from root directory of the whole mockito project
cp ../../LICENSE .


%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Oct 15 2021 Martin Perina <mperina@redhat.com> - 3.12.4-0.1
- Update to version 3.12.4

* Wed Jul 28 2021 Martin Perina <mperina@redhat.com> - 3.11.2-0.1
- Initial package
