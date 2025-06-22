%global		upstream_name    scram
%global		upstream_version 2.1

Name:		ongres-%upstream_name
Version:	%(echo %upstream_version | sed 's/-/~/g')
Release:	3.1%{?dist}
Summary:	Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:	BSD
URL:           https://github.com/ongres/%upstream_name
Source0:       https://github.com/ongres/%upstream_name/archive/%upstream_version/%upstream_name-%upstream_version.tar.gz
BuildRequires:	maven-local
BuildRequires:  ongres-stringprep
BuildRequires:  junit
BuildArch:	noarch

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


%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Summary:	Client for %{name}

%description client
This package contains the client for %{name}

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%package parent
Summary:	Parent POM of %{name}

%description parent
This package contains the %{name} parent POM.

%prep
%autosetup -p1 -n "%upstream_name-%upstream_version"
find \( -name '*.jar' -o -name '*.class' \) -delete
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin client
%pom_remove_plugin -r :maven-javadoc-plugin

# Retired in Fedora; not required for build
%pom_remove_dep com.google.code.findbugs:annotations
sed -i 's/.*SuppressFBWarnings.*//' common/src/main/java/com/ongres/scram/common/message/ServerFinalMessage.java

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-common
%license LICENSE

%files client -f .mfiles-client
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files parent -f .mfiles-parent
%license LICENSE

%changelog
* Thu Jan 12 2023 Martin Perina <mperina@redhat.com> - 2.1-3.1
- Rebuild with added conflict to maven 3.8 modules to pass the build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Richard Fearn <richardfearn@gmail.com> - 2.1-2
- Remove unnecessary findbugs dependency (#1966792)

* Fri Feb 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 2.1-1
- Rebase to version 2.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.0~beta.2-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0~beta.2-5
- Remove explicit invocation of maven-javadoc-plugin

* Tue May 22 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0.0~beta.2-4
- BR javadoc maven plugin explicitly
- use nicer Source0 format

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Pavel Raiskup <praiskup@redhat.com> - 1.0.0~beta.2-2
- drop potential pre-compiled files from release tarball

* Fri Nov 24 2017 Augusto Caringi <acaringi@redhat.com> 1.0.0~beta.2-1
- initial rpm
