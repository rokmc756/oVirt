Name:           jackson-databind
Version:        2.11.4
Release:        6%{?dist}
Summary:        General data-binding package for Jackson (2.x)
License:        ASL 2.0 and LGPLv2+

URL:            https://github.com/FasterXML/jackson-databind
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:      noarch

%description
The general-purpose data-binding functionality and tree-model for Jackson Data
Processor. It builds on core streaming parser/generator package, and uses
Jackson Annotations for configuration.

%package -n pki-%{name}
Summary: General data-binding package for Jackson (2.x)
Obsoletes: %{name} < %{version}-%{release}
Conflicts: %{name} < %{version}-%{release}
Provides: %{name} = %{version}-%{release}

%description -n pki-%{name}
The general-purpose data-binding functionality and tree-model for Jackson Data
Processor. It builds on core streaming parser/generator package, and uses
Jackson Annotations for configuration.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin "org.jacoco:jacoco-maven-plugin"
%pom_remove_plugin "org.moditect:moditect-maven-plugin"

cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

# unavailable test deps
%pom_remove_dep javax.measure:jsr-275
rm src/test/java/com/fasterxml/jackson/databind/introspect/NoClassDefFoundWorkaroundTest.java
%pom_xpath_remove pom:classpathDependencyExcludes

# TestTypeFactoryWithClassLoader fails to compile
# - it's the only test that uses powermock, so drop the powermock dependencies
# - mockito is only transitively pulled in by powermock, so add it back
%pom_remove_dep org.powermock:
%pom_add_dep org.mockito:mockito-core::test
rm src/test/java/com/fasterxml/jackson/databind/type/TestTypeFactoryWithClassLoader.java

# Off test that require connection with the web
rm src/test/java/com/fasterxml/jackson/databind/ser/jdk/JDKTypeSerializationTest.java \
 src/test/java/com/fasterxml/jackson/databind/deser/jdk/JDKStringLikeTypesTest.java \
 src/test/java/com/fasterxml/jackson/databind/TestJDKSerialization.java

%mvn_file : %{name}

%build
%mvn_build -f -j -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -n pki-%{name} -f .mfiles
%doc README.md release-notes/*
%license LICENSE NOTICE

%changelog
* Mon Aug 16 2021 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.11.4-6
- Disable tests
- Drop javadoc subpackage

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.11.4-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Apr 28 2021 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.11.4-4
- Rename subpackages to pki-jackson

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.11.4-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Fabio Valentini <decathorpe@gmail.com> - 2.11.4-1
- Update to version 2.11.4.

* Wed Oct 14 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.3-1
- Update to version 2.11.3.

* Sun Aug 09 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.2-2
- Drop useless powermock build dependency.

* Sat Aug 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.2-1
- Update to version 2.11.2.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.11.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jul 06 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.1-1
- Update to version 2.11.1.

* Mon May 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.11.0-1
- Update to version 2.11.0.

* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.4-1
- Update to version 2.10.4.

* Tue Mar 03 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.3-1
- Update to version 2.10.3.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Fabio Valentini <decathorpe@gmail.com> - 2.10.2-1
- Update to version 2.10.2.

* Wed Nov 13 2019 Fabio Valentini <decathorpe@gmail.com> - 2.10.1-1
- Update to version 2.10.1.

* Thu Oct 3 2019 Alexander Scheel <ascheel@redhat.com> - 2.10.0-1
- Update to latest upstream release
- Fixes: CVE-2019-14540
- Fixes: CVE-2019-16335
- Fixes: CVE-2019-16942
- Fixes: CVE-2019-16943
- Resolves: rhbz#1758168
- Resolves: rhbz#1758172
- Resolves: rhbz#1758183

* Thu Sep 12 2019 Alexander Scheel <ascheel@redhat.com> - 2.9.9.3-1
- Update to latest upstream release; fixes CVE-2019-12384

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Mat Booth <mat.booth@redhat.com> - 2.9.8-1
- Update to latest upstream release, fixes CVE-2018-14718 CVE-2018-147189
  CVE-2018-19360 CVE-2018-19361 CVE-2018-19362 CVE-2018-12022 CVE-2018-12023
  CVE-2018-14720 CVE-2018-14721

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-3
- Add patch to fix CVE-2018-7489

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-1
- Update to latest upstream release
- Drop upstreamed CVE patches

* Mon Jan 22 2018 Mat Booth <mat.booth@redhat.com> - 2.9.3-1
- Update to latest upstream release

* Mon Jan 15 2018 Mat Booth <mat.booth@redhat.com> - 2.7.6-7
- Better patch for CVE-2017-17485

* Thu Jan 11 2018 Mat Booth <mat.booth@redhat.com> - 2.7.6-6
- Backport a patch to fix CVE-2017-17485

* Fri Nov 03 2017 Mat Booth <mat.booth@redhat.com> - 2.7.6-5
- Backport a patch to fix CVE-2017-15095

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Mat Booth <mat.booth@redhat.com> - 2.7.6-3
- Backport a patch to fix CVE-2017-7525

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 gil cattaneo <puntogil@libero.it> 2.7.6-1
- update to 2.7.6

* Fri Jun 24 2016 gil cattaneo <puntogil@libero.it> 2.6.7-1
- update to 2.6.7

* Thu May 26 2016 gil cattaneo <puntogil@libero.it> 2.6.6-1
- update to 2.6.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 gil cattaneo <puntogil@libero.it> 2.6.3-1
- update to 2.6.3

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 2.6.2-1
- update to 2.6.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 2.5.0-1
- update to 2.5.0

* Sat Sep 20 2014 gil cattaneo <puntogil@libero.it> 2.4.2-1
- update to 2.4.2

* Wed Jul 23 2014 gil cattaneo <puntogil@libero.it> 2.4.1.3-1
- update to 2.4.1.3

* Thu Jul 03 2014 gil cattaneo <puntogil@libero.it> 2.4.1.1-1
- update to 2.4.1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 gil cattaneo <puntogil@libero.it> 2.2.2-2
- review fixes

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 2.2.2-1
- 2.2.2
- renamed jackson-databind

* Tue May 07 2013 gil cattaneo <puntogil@libero.it> 2.2.1-1
- 2.2.1

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 2.1.0-1
- update to 2.1.0
- renamed jackson2-databind

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 2.0.6-1
- initial rpm
