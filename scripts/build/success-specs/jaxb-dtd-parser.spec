Name:           jaxb-dtd-parser
Version:        1.4.3
Release:        6%{?dist}
Summary:        SAX-like API for parsing XML DTDs
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

Obsoletes:      glassfish-dtd-parser < 1.4.3-1
Provides:       glassfish-dtd-parser = %{version}-%{release}

%description
SAX-like API for parsing XML DTDs.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q

pushd dtd-parser
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent

# remove unnecessary plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin

popd


%build
pushd dtd-parser
%mvn_build
popd


%install
pushd dtd-parser
%mvn_install
popd


%files -f dtd-parser/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f dtd-parser/.mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.3-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.3-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Mat Booth <mat.booth@redhat.com> - 1.4.3-3
- Restore JDK 9+ bits for Jaxb

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Initial package renamed from glassfish-dtd-parser.

