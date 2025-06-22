%global base_name       lang
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        2.6
Release:        35%{?dist}
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0

URL:            https://commons.apache.org/%{base_name}
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         0000-Fix-FastDateFormat-for-Java-7-behaviour.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  junit

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1

sed -i 's/\r//' *.txt *.html

%mvn_file  : %{name} %{short_name}
%mvn_alias : org.apache.commons: %{base_name}:%{base_name}

# remove org.apache.commons.lang.enum package
# "enum" is a keyword since Java 4 and cannot be used as an identifier
rm -r src/main/java/org/apache/commons/lang/enum/
rm -r src/test/java/org/apache/commons/lang/enum/
rm src/test/java/org/apache/commons/lang/enums/EnumTest.java

# convert some stray ISO-8859-1 characters to UTF-8
iconv -f ISO-8859-1 -t UTF-8 \
    src/main/java/org/apache/commons/lang/Entities.java > \
    src/main/java/org/apache/commons/lang/Entities.java.utf-8
mv src/main/java/org/apache/commons/lang/Entities.java.utf-8 \
    src/main/java/org/apache/commons/lang/Entities.java

%build
%mvn_build -- \
    -Dcommons.osgi.symbolicName=org.apache.commons.lang \
    -Dmaven.compiler.source=1.8 \
    -Dmaven.compiler.target=1.8 \
    -Dsource=1.8

%install
%mvn_install

%files -f .mfiles
%doc PROPOSAL.html RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Wed Dec 15 2021 Sandro Bonazzola <sbonazzo@redhat.com> - 2.6-35
- add missing dependency on junit

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 2.6-34
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.6-32
- Remove unused org.apache.commons.lang.enum package.
- Compile with Java 11, target Java 8 (instead of Java 8 targeting Java 3).
- Remove stray encoding issues, convert to UTF-8.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.6-30
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jul 09 2020 Mat Booth <mat.booth@redhat.com> - 2.6-29
- Pass javadoc source parameter as a property so it can be used by the xmvn
  javadoc mojo

* Thu Jun 25 2020 Roland Grunberg <rgrunber@redhat.com> - 2.6-28
- Force Java 8 as we cannot build for Java 11 without breaking API.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6-26
- Use override for maven compiler source and target that works with xmvn 3.1.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Mat Booth <mat.booth@redhat.com> - 2.6-24
- Rebuild to regenerate OSGi metadata

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Alexander Kurtakov <akurtako@redhat.com> 2.6-15
- Drop old jakarta provides/obsoletes.

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-14
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 2.6-12
- Rebuild

* Tue Apr 09 2013 Michal Srb <msrb@redhat.com> - 2.6-11
- Properly specify XMvn's compilerSource option

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8
- Build with xmvn

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-6
- Add backported fix for JDK 1.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-4
- Use new add_maven_depmap macro
- Fix maven3 build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-2
- Fix commons-lang symlink

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6-1
- Update to 2.6
- Versionless jars & javadocs
- Use maven 3 to build

* Wed Nov 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-7
- Use apache-commons-parent instead of maven-*

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-6
- Add license to javadoc subpackage

* Wed May 26 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-5
- Add another old depmap to prevent groupId dependency problems

* Fri May 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-4
- Correct depmap filename for backward compatibility

* Mon May 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-3
- Fix maven depmap JPP name to short_name

* Mon May 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-2
- Added export for MAVEN_LOCAL_REPO and mkdir
- Added more add_to_maven_depmap to assure backward compatibility
- Add symlink to short_name.jar

* Mon May 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5-1
- Rename and rebase of jakarta-commons-lang
- Re-did whole spec file to use maven, dropped gcj support
