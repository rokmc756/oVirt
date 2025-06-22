Summary: A Java template engine
Name: stringtemplate
Version: 3.2.1
Release: 26%{?dist}
URL: http://www.stringtemplate.org/
Source0: http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0: stringtemplate-3.1-build-junit.patch
License: BSD

BuildRequires: ant
BuildRequires: ant-antlr
BuildRequires: ant-junit
BuildRequires: javapackages-local

BuildArch: noarch

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Summary:        API documentation for %{name}
Requires:       java-javadoc

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0
sed -i -e 's/source="1.4"/source="1.8"/g' build.xml
sed -i -e 's/target="1.4"/target="1.8"/g' build.xml

%build
rm -rf lib target
ant jar
ant javadocs -Dpackages= -Djavadocs.additionalparam="-Xdoclint:none"

%install
%mvn_artifact pom.xml build/%{name}.jar
%mvn_file : %{name}
%mvn_install -J docs/api/

%files -f .mfiles
%license LICENSE.txt
%doc README.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.1-23
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Jeff Johnston <jjohnstn@redhat.com> - 3.2.1-22
- Update to build under Java 11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Mat Booth <mat.booth@redhat.com> - 3.2.1-16
- Modernise spec

* Mon Oct  2 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-15
- Workaround strict javadoc doclint
- Resolves: rhbz#1495145

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 05 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.1-10
- Fix for F21 XMvn changes (#1107380)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.2.1-8
- Use Requires: java-headless rebuild (#1067528)

* Wed Aug 14 2013 Mat Booth <fedora@matbooth.co.uk> - 3.2.1-7
- Fix FTBFS #993386

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 1 2013 Conrad Meyer <konrad@tylerc.org> - 3.2.1-5
- Add missing dep on antlr-tool (#904979)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 29 2010 Miloš Jakubíček <xjakub@fi.muni.cz> - 3.2.1-1
- Update to 3.2.1
- Supply maven POM files
- Drop stringtemplate-3.1-disable-broken-test.patch (merged upstream)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Apr 05 2008 Colin Walters <walters@redhat.com> - 3.1-1
- First version
