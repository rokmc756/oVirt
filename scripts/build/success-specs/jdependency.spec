Name:           jdependency
Version:        1.2
Release:        13%{?dist}
Summary:        This project provides an API to analyse class dependencies
License:        ASL 2.0
URL:            http://github.com/tcurdt/%{name}
BuildArch:      noarch

Source0:        http://github.com/tcurdt/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)

%description
%{name} is small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_file : %{name}
# work-around for: https://bugzilla.redhat.com/show_bug.cgi?id=1981486
%pom_add_dep org.apache.commons:commons-lang3:3.12.0:test

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

# remove a test case that is harmlessly broken on Java 11
rm src/test/java/org/vafer/jdependency/DependencyUtilsTestCase.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.2-13
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jul 12 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1.2-12
- Add commons-lang3 dependency for tests.
- Resolves: RHBZ#1981024

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2-11
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2-8
- Set javac source and target to 1.8 to fix Java 11 builds.
- Remove one test case that is harmlessly broken with Java 11.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 Michael Simacek <msimacek@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Michal Srb <msrb@redhat.com> - 0.9-1
- Update to upstream version 0.9

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7-10
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-8
- Update to current packaging guidelines
- Fix test failures

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-7
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7-3
- Fix date ordering in changelog
- Guidelines fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7-1
- Update to 0.7
- Fix BR to not require maven2
- Fix BR for new package name
- Adjust spec to new guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-3
- Add license to javadoc subpackage
- Change jakarta-commons-io for apache-commons-io
- Add BR to maven

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-2
- Rename from vafer-jdependency to jdependency alone

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6-1
- Initial package
