%bcond_with bootstrap

Name:           maven-parent
Version:        34
Release:        10%{?dist}
Summary:        Apache Maven parent POM
License:        ASL 2.0
URL:            https://maven.apache.org
Source0:        https://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
%endif

%description
Apache Maven parent POM file used by other Maven projects.

%prep
%setup -q
%pom_disable_module apache-resource-bundles
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin

%pom_xpath_remove "pom:execution[pom:id='generate-helpmojo']" maven-plugins

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 34-10
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 09 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-9
- Rebuild to workaround DistroBaker issue

* Tue Jun 08 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-8
- Bootstrap Maven for CentOS Stream 9

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-7
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 34-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 22 2020 Marian Koncek <mkoncek@redhat.com> - 34-1
- Update to upstream version 34

* Fri Mar 27 2020 Severin Gehwolf <sgehwolf@redhat.com> - 34-3
- Remove javadoc taglet configuration which is not longer available

* Wed Mar 25 2020 Severin Gehwolf <sgehwolf@redhat.com> - 34-2
- Remove explicit requirement on maven-plugin-tools-javadoc

* Mon Mar 02 2020 Fabio Valentini <decathorpe@gmail.com> - 34-1
- Update to version 34.
- Switch to HTTPS URL for source downloads.
- Remove upstream patch that's part of this release.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-3
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-2
- Mass rebuild for javapackages-tools 201901

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 33-1
- Update to upstream version 33
- Obsolete maven-shared and maven-plugins-pom.

* Tue May 14 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-1
- Update to upstream version 33

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 27-1
- Update to upstream version 27

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-1
- Update to upstream version 26

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 25-1
- Update to upstream version 25

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 24-2
- Rebuild to regenerate Maven auto-requires

* Wed Apr  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 24-1
- Update to upstream version 24

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 23-1
- Update to upstream version 23

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20-6
- Rebuild to regenerate Maven provides

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20-4
- Build with xmvn

* Fri Nov  2 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 20-4
- Add missing BR/R: apache-parent
- Update to current packaging guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 20-1
- Initial version of the package
