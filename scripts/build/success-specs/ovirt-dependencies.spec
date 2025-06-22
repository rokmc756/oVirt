
%global __jar_repack 0

Summary:    oVirt 3rd party dependencies
Name:       ovirt-dependencies
Version:    4.5.3
Release:    1%{?release_suffix}%{?dist}
License:    ASL 2.0
URL:        http://www.ovirt.org
Source:     ovirt-dependencies-4.5.3-1.tar.gz

BuildArch:  noarch

BuildRequires:  java-11-openjdk-devel
BuildRequires:  javapackages-tools
BuildRequires:  javapackages-local
BuildRequires:  make
BuildRequires:  maven >= 3.5.0
BuildRequires:  maven-local
BuildRequires:  maven-dependency-plugin
BuildRequires:  tar

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

Provides:   bundled(gwt-servlet) = 2.9.0

Provides:   bundled(spring-aop) = 5.3.27
Provides:   bundled(spring-beans) = 5.3.27
Provides:   bundled(spring-context) = 5.3.27
Provides:   bundled(spring-core) = 5.3.27
Provides:   bundled(spring-jcl) = 5.3.27
Provides:   bundled(spring-expression) = 5.3.27
Provides:   bundled(spring-instrument) = 5.3.27
Provides:   bundled(spring-jdbc) = 5.3.27
Provides:   bundled(spring-test) = 5.3.27
Provides:   bundled(spring-tx) = 5.3.27

# Required due to upgrade issues around moving from rhvm-dependencies to ovirt-dependencies
Provides:  rhvm-dependencies
Obsoletes:  rhvm-dependencies < 4.5.0

%description
oVirt 3rd party dependencies

%prep
%setup -q -n %{name}-4.5.3

%build
# Necessary to override the default for xmvn, which is JDK 8
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk"

%mvn_build -j -- -C

%install
%pom_remove_parent dependencies/com/google/gwt/gwt/2.9.0/gwt-2.9.0.pom
%mvn_artifact dependencies/com/google/gwt/gwt/2.9.0/gwt-2.9.0.pom
%mvn_artifact dependencies/com/google/gwt/gwt-servlet/2.9.0/gwt-servlet-2.9.0.pom dependencies/com/google/gwt/gwt-servlet/2.9.0/gwt-servlet-2.9.0.jar

%mvn_artifact dependencies/org/springframework/spring-aop/5.3.27/spring-aop-5.3.27.pom dependencies/org/springframework/spring-aop/5.3.27/spring-aop-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-beans/5.3.27/spring-beans-5.3.27.pom dependencies/org/springframework/spring-beans/5.3.27/spring-beans-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-context/5.3.27/spring-context-5.3.27.pom dependencies/org/springframework/spring-context/5.3.27/spring-context-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-core/5.3.27/spring-core-5.3.27.pom dependencies/org/springframework/spring-core/5.3.27/spring-core-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-jcl/5.3.27/spring-jcl-5.3.27.pom dependencies/org/springframework/spring-jcl/5.3.27/spring-jcl-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-expression/5.3.27/spring-expression-5.3.27.pom dependencies/org/springframework/spring-expression/5.3.27/spring-expression-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-instrument/5.3.27/spring-instrument-5.3.27.pom dependencies/org/springframework/spring-instrument/5.3.27/spring-instrument-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-jdbc/5.3.27/spring-jdbc-5.3.27.pom dependencies/org/springframework/spring-jdbc/5.3.27/spring-jdbc-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-test/5.3.27/spring-test-5.3.27.pom dependencies/org/springframework/spring-test/5.3.27/spring-test-5.3.27.jar
%mvn_artifact dependencies/org/springframework/spring-tx/5.3.27/spring-tx-5.3.27.pom dependencies/org/springframework/spring-tx/5.3.27/spring-tx-5.3.27.jar

%mvn_install

%files -f .mfiles
%dir %{_jnidir}/%{name}
%dir %{_javadir}/%{name}

%doc ChangeLog
%license COPYING
%license COPYING.csv

%changelog
* Fri Jun 02 2023 Martin Perina <mperina@redhat.com> - 4.5.3-1
- Bump SpringFramework to 5.3.27

* Tue May 10 2022 Martin Perina <mperina@redhat.com> - 4.5.2-1
- Bump SpringFramework to 5.3.19

* Mon Jan 03 2022 Martin Perina <mperina@redhat.com> - 4.5.1-1
- Fix issues around moving from rhvm-dependencies package

* Sun Dec 26 2021 Martin Perina <mperina@redhat.com> - 4.5.0-1
- packaging: use maven to download jars
- packaging: drop checksum verification
- packaging: remove artifacts urls from conf.d/*

* Thu Mar 26 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 4.4.2-1
- Initial packaging

