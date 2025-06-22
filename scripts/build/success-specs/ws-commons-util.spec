Name:           ws-commons-util
Version:        1.0.2
Release:        1.1%{?dist}
Summary:        Common utilities from the Apache Web Services Project

License:        ASL 2.0
URL:            http://ws.apache.org/commons/util

# svn checkout http://svn.apache.org/repos/asf/webservices/commons/tags/util/1.0.2/ ws-commons-util-1.0.2
# tar cJf ws-commons-util-1.0.2.tar.xz ws-commons-util-1.0.2
Source0:        ws-commons-util-1.0.2.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

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
This is version 1.0.2 of the common utilities from the Apache Web
Services Project.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%mvn_file : %{name}
%mvn_alias org.apache.ws.commons:ws-commons-util org.apache.ws.commons.util:ws-commons-util
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.apache.ws.commons.util</Bundle-SymbolicName>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Localization>plugin</Bundle-Localization>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

# This dep is supplied by the JRE
%pom_remove_dep "xml-apis:xml-apis"

# Avoid unnecessary runtime dependency on junit, used for tests only
%pom_xpath_inject 'pom:dependency[pom:artifactId="junit"]' "<scope>test</scope>"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Thu Sep 22 2022 Martin Perina <mperina@redhat.com> - 1.0.2-1.1
- Block all packages from maven:3.8 module to pass the build on CS9
- Use JDK 1.6 source code compatibility for the build

* Thu Feb 06 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.2-1
- Initial import on el8 from Fedora

