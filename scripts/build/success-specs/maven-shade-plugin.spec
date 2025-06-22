Name:           maven-shade-plugin
Version:        3.2.4
Release:        6%{?dist}
Summary:        Maven plugin for packaging artifacts in an uber-jar
License:        ASL 2.0

URL:            https://maven.apache.org/plugins/%{name}
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.vafer:jdependency)
BuildRequires:  mvn(xmlunit:xmlunit)

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.


%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q

rm src/test/jars/plexus-utils-1.4.1.jar
ln -s $(build-classpath plexus/utils) src/test/jars/plexus-utils-1.4.1.jar

%pom_remove_dep 'com.google.guava:guava:'
%pom_add_dep 'com.google.guava:guava'

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.2.4-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.2.4-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.4-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 08 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.4-1
- Update to version 3.2.4.

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.3-1
- Update to version 3.2.3.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.1-2
- Drop workaround for maven-artifact-transfer 0.11.0.

* Sun Aug 18 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.1-1
- Update to version 3.2.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Michael Simacek <msimacek@redhat.com> - 3.1.1-1
- Update to upstream version 3.1.1

* Wed Apr 11 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-3
- Switch BR to guava20

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-1
- Update to upstream version 3.1.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Michael Simacek <msimacek@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Mon May 02 2016 Michael Simacek <msimacek@redhat.com> - 2.4.3-1
- Update to upstream version 2.4.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-1
- Update to upstream version 2.4.2

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-3
- Fix Maven 3 patch

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-2
- Port to maven-dependency-tree 3.0

* Thu Jul 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-1
- Update to upstream version 2.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-1
- Update to upstream version 2.4

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-5
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-4
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-2
- Add patch for MSHADE-168
- Resolves: rhbz#1096583

* Fri May  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Dec  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-1
- Update to upstream version 2.2

* Tue May 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-1
- Update to upstream version 2.1

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec 13 2012 Tomas Radej <tradej@redhat.com> - 2.0-1
- Update to upstream 2.0

* Wed Nov 14 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.1-3
- Install NOTICE file with javadoc package

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.7.1-1
- Update to upstream 1.7.1.

* Wed Jun 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-1
- Update to upstream 1.7

* Fri Apr 6 2012 Alexander Kurtakov <akurtako@redhat.com> 1.6-1
- Update to latest upstream release.

* Mon Mar 05 2012 Jaromir Capik <jcapik@redhat.com> - 1.5-4
- Migration to plexus-containers-component-metadata

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-2
- Fix depmap macro call

* Tue Nov 1 2011 Alexander Kurtakov <akurtako@redhat.com> 1.5-1
- Update to upstream 1.5 release.

* Thu Jun 9 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-4
- Build with maven 3.x.
- Use upstream source.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-2
- Add jdependency also to Requires

* Thu Oct 14 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 1.4-1
- Update to 1.4
- Add BR on jdependency >= 0.6
- Add patch to add dependency on maven-artifact-manager

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.3-2
- Replace plexus utils jar with symlink
- Create MAVEN_REPO_LOCAL dir before calling maven

* Tue Jun 22 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.3-1
- Initial package
