Name:           stringtemplate4
Version:        4.3.1
Release:        6%{?dist}
Summary:        A Java template engine
License:        BSD
URL:            http://www.stringtemplate.org/
BuildArch:      noarch

Source0:        https://github.com/antlr/stringtemplate4/archive/%{version}/%{name}-%{version}.tar.gz
# Adapt to JDK 11
Patch0:         %{name}-java11.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime) >= 3.5.2
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin) >= 3.5.2
BuildRequires:  xorg-x11-fonts-Type1
BuildRequires:  xorg-x11-server-Xvfb

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -p1

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# The revapi plugin is an API checker.  That is a great thing for upstream to
# use, but not for Fedora builds.  Plus Fedora doesn't currently have it.
%pom_remove_plugin :revapi-maven-plugin

%build
xvfb-run -d %mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt contributors.txt README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Jerry James <loganjerry@gmail.com> - 4.3.1-4
- Remove dependency on deprecated sonatype-oss-parent

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 4.3.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jun 23 2020 Jerry James <loganjerry@gmail.com> - 4.3.1-1
- Version 4.3.1
- Add -java11 patch to adapt to JDK 11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jerry James <loganjerry@gmail.com> - 4.3-1
- Version 4.3

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 4.2-1
- Version 4.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.8-1
- Update to upstream version 4.0.8

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.4-8
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.4-7
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.4-4
- Fix file permissions

* Thu Jul 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.4-3
- Fix build. stringtemplate4 now needs itself to build so add it to
  classpath

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.4-1
- Initial version of the package

