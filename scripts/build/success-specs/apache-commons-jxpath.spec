Name:           apache-commons-jxpath
Version:        1.3
Release:        40.2%{?dist}
Summary:        Simple XPath interpreter
License:        ASL 2.0
URL:            http://commons.apache.org/jxpath/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/jxpath/source/commons-jxpath-%{version}-src.tar.gz

Patch0:         commons-jxpath-mockrunner.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)

%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-jxpath-%{version}-src
%patch0 -p1

%pom_remove_dep xerces:
%pom_remove_dep xml-apis:

# Remove dependency on glassfish
%pom_remove_dep :servlet-api
%pom_remove_dep :jsp-api
rm src/java/org/apache/commons/jxpath/servlet/*Context*.java
rm src/java/org/apache/commons/jxpath/servlet/*Handler.java
rm src/test/org/apache/commons/jxpath/servlet/JXPathServletContextTest.java

%mvn_file ":{*}" %{name} @1
%mvn_alias : org.apache.commons:

%pom_xpath_inject 'pom:properties' \
  '<commons.osgi.import>org.apache.commons.beanutils;resolution:="optional",org.jdom*;resolution:="optional",org.w3c.dom;resolution:="optional",javax.servlet*;resolution:="optional",*</commons.osgi.import>'

%build
# we are skipping tests because we don't have com.mockrunner in repos yet
%mvn_build -f -- -Dmaven.compiler.source=1.6 -Dmaven.compiler.target=1.6 -Dcommons.osgi.symbolicName=org.apache.commons.jxpath

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Thu Sep 23 2021 Martin Perina <mperina@redhat.com> - 1.3-40.2
- Non-bootstrap build

* Fri Aug 13 2021 Martin Perina <mperina@redhat.com> - 1.3-40.1
- Bootstrap build

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-39
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.3-36
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3-35
- Set javac -source and -target to 1.8.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-31
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-30
- Mass rebuild for javapackages-tools 201901

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 1.3-32
- Rebuild to fix OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Mat Booth <mat.booth@redhat.com> - 1.3-28
- Make the OSGi dep on servlet APIs optional

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Mat Booth <mat.booth@redhat.com> - 1.3-23
- Fix optional deps in OSGi manifest

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-22
- Cleanup spec file

* Wed Feb 25 2015 Alexander Kurtakov <akurtako@redhat.com> 1.3-21
- Rebuild for jsp api.
- Drop old javadoc pre section.

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-20
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-18
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-16
- Remove unneeded BR: maven-idea-plugin

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-15
- Migrate from Tomcat 6 to Tomcat 7
- Resolves: rhbz#913879

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 1.3-12
- Build with xmvn

* Thu Nov 22 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-11
- Install NOTICE file
- Resolves: rhbz#879556

* Fri Nov  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-10
- Don't build-require maven2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> 1.3-8
- Fix build and update to latest guidelines

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Chris Spike <chris.spike@arcor.de> 1.3-5
- tomcat5 -> tomcat6 BRs/Rs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-4
- Add license to javadoc subpackage

* Thu May 27 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-3
- Add tomcat5 to BR

* Tue May 25 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-2
- Fix ownership of some directories

* Tue May 25 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-1
- Rename package (jakarta-commons-jxpath->apache-commons-jxpath)
- Cleanup spec file
- Build using maven, drop old pom file from sources
- Update to upstream version

* Thu Aug 20 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-9
- Fix random spaces.

* Wed Aug 19 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-8
- BuildRequires java-devel >= 1.6.0.

* Wed Aug 19 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-7
- Initial package for Fedora.

* Sun May 17 2009 Fernando Nasser <fnasser@redhat.com> - 0:1.2-6
- Fix License
- Provide intructions for obtaining source and refresh source tar ball

* Wed Mar 18 2009 Yong Yang <yyang@redhat.com> - 0:1.2-5
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> - 0:1.2-4
- Fix release tag

* Thu Jan 08 2009 Yong Yang <yyang@redhat.com> - 0:1.2-3jpp.1
- Import from dbhole's maven 2.0.8 packages, initial building

* Wed Apr 09 2008 Deepak Bhole <dbhole@redhat.com> - 0:1.2-2jpp.1
- Import from JPackage
- Added pom file

* Wed Jun 07 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.2-2jpp
- First JPP 1.7 build

* Sat Sep 18 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.2-1jpp
- Upgrade to 1.2
- Use jdom-1.0-0.rc1.1jpp
- Relax some versioned dependencies

* Mon Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.1-3jpp
- Rebuild with ant-1.6.2

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.1-2jpp
- Upgrade to Ant 1.6.X

* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.1-1jpp
- First JPackage release
