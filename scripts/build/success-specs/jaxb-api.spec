Name:           jaxb-api
Version:        2.3.3
Release:        5%{?dist}
Summary:        Jakarta XML Binding API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-api
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# package renamed from glassfish-jaxb-api in fedora 33
Provides:       glassfish-jaxb-api = %{version}-%{release}
Obsoletes:      glassfish-jaxb-api < 2.3.3-2

# javadoc subpackage is currently not built
Obsoletes:      glassfish-jaxb-api-javadoc < 2.3.3-2

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
%setup -q

# remove unnecessary dependency on parent POM
%pom_remove_parent

# disable unwanted test module
%pom_disable_module jaxb-api-test

# remove unnecessary maven plugins
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# mark dependency on jakarta.activation as optional
%pom_xpath_inject "pom:dependency[pom:groupId='jakarta.activation']" "<optional>true</optional>" jaxb-api

# add compatibility aliases for old artifact coordinates
%mvn_alias jakarta.xml.bind:jakarta.xml.bind-api javax.xml.bind:jaxb-api
%mvn_file :jakarta.xml.bind-api glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api


%build
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -DbuildNumber=unknown -DscmBranch=%{version}


%install
%mvn_install


%files -f .mfiles
%license LICENSE.md NOTICE.md


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.3.3-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.3.3-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.3-2
- Initial package renamed from glassfish-jaxb-api.

