%global     upstream_name   stringprep

Name:       ongres-%upstream_name
Version:    1.1
Release:    2.1%{?dist}
Summary:    RFC 3454 Preparation of Internationalized Strings in pure Java
License:    BSD
URL:            https://github.com/ongres/%upstream_name
Source0:        https://github.com/ongres/%upstream_name/archive/%{version}/%upstream_name-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  junit5
BuildRequires:  velocity
BuildRequires:  maven-plugin-build-helper
BuildRequires:  exec-maven-plugin
BuildRequires:  maven-enforcer-plugin

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

BuildArch:  noarch

%description
The stringprep protocol does not stand on its own;
it has to be used by other protocols at precisely-defined
places in those other protocols.

%package javadoc
Summary:    Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -p1 -n "%upstream_name-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep :velocity-tools codegenerator

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Thu Jan 12 2023 Martin Perina <mperina@redhat.com> - 1.1-2.1
- Rebuild with added conflict to maven 3.8 modules to pass the build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 1.1-1
- initial rpm
