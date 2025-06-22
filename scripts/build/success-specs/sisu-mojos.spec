Name:           sisu-mojos
Version:        0.3.4
Release:        8.2%{?dist}
Summary:        Sisu plugin for Apache Maven
License:        EPL-1.0
URL:            http://www.eclipse.org/sisu
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/sisu/org.eclipse.sisu.mojos.git/snapshot/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.slf4j:slf4j-nop)


%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -c
mv releases/%{version}/* .

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Animal Sniffer is not useful in Fedora
%pom_remove_plugin :animal-sniffer-maven-plugin

%mvn_alias : org.sonatype.plugins:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Sep 30 2021 Martin Perina <mperina@redhat.com> - 0.3.4-8.2
- Non-bootstrap build

* Thu Sep 23 2021 Martin Perina <mperina@redhat.com> - 0.3.4-8.1
- Bootstrap build

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.4-7
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.3.4-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.4-2
- Remove unnecessary dependency on parent POM.

* Sat Nov 09 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.4-1
- Update to version 0.3.4.

* Wed Nov 06 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.4-1
- Update to upstream version 0.3.4

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.3-2
- Mass rebuild for javapackages-tools 201902

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.3-1
- Update to version 0.3.3.

* Thu Jun 06 2019 Marian Koncek <mkoncek@redhat.com> - 0.3.3-1
- Update to upstream version 0.3.3

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.1-9
- Mass rebuild for javapackages-tools 201901

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  2 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.1-7
- Update license tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.3.1-1
- Update to upstream version 0.3.1

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 0.1.0-4
- Fix parent POM BR

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.0-2
- Obsolete sisu-maven-plugin

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.0-1
- Update to upstream version 0.1.0

* Mon Sep 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.0.0-0.1.M5
- Initial packaging.
- Fix unowned directory
