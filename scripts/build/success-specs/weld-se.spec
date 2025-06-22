# It's extremely hard (lots of dependencies) to package weld, so just including binaries here
%global pkg_version 2.3.5
%global weld_version %{pkg_version}.Final

%global _maven_metadata_dir /usr/share/maven-metadata

Name:		weld-se
Version:	%{pkg_version}
Release:	0.1%{?dist}
Summary:	Weld SE (Uber Jar)
License:	ASL 2.0
URL:		https://weld.cdi-spec.org
SOURCE0:	https://repo1.maven.org/maven2/org/jboss/weld/se/weld-se/%{weld_version}/weld-se-%{weld_version}.pom
SOURCE1:	https://repo1.maven.org/maven2/org/jboss/weld/se/weld-se/%{weld_version}/weld-se-%{weld_version}.jar
SOURCE2:	weld-se.xml
SOURCE3:	https://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:	noarch

BuildRequires:	java-11-openjdk-devel

Provides:	mvn(org.jboss.weld.se:weld-se) = %{weld_version}
Provides:	mvn(org.jboss.weld.se:weld-se:pom:) = %{weld_version}

Requires:	(java-headless or java-11-headless)
Requires:	javapackages-filesystem

%description
%{name} bundles all the bits of Weld and CDI required for Java SE.


%install
mkdir -p %{buildroot}%{_mavenpomdir}/%{name}
cp -p %{SOURCE0} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p %{SOURCE1} %{buildroot}%{_javadir}/%{name}/%{name}.jar
mkdir -p %{buildroot}%{_maven_metadata_dir}
cp -p %{SOURCE2} %{buildroot}%{_maven_metadata_dir}/%{name}.xml

cp %{SOURCE3} LICENSE

%files
%license LICENSE
%{_mavenpomdir}/%{name}/%{name}.pom
%{_javadir}/%{name}/%{name}.jar
%{_maven_metadata_dir}/%{name}.xml


%changelog
* Mon Mar 21 2022 Martin Perina <mperina@redhat.com> - 2.3.5-0.1
- Initial RPM release
- Just bundled JAR due to high number of build dependencies

