Name:           mojo-parent
Version:        60
Release:        3.2%{?dist}
Summary:        Codehaus MOJO parent project pom file
License:        ASL 2.0
URL:            https://www.mojohaus.org/mojo-parent/
BuildArch:      noarch

Source0:        https://github.com/mojohaus/mojo-parent/archive/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local

%description
Codehaus MOJO parent project pom file

%prep
%setup -q -n %{name}-%{name}-%{version}
# Not needed in Fedora.
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-checkstyle-plugin

cp %SOURCE1 .

%build
%mvn_alias : org.codehaus.mojo:mojo
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Wed Sep 29 2021 Martin Perina <mperina@redhat.com> - 60-3.2
- Non-bootstrap build

* Tue Aug 17 2021 Martin Perina <mperina@redhat.com> - 60-3.1
- Bootstrap build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 60-2
- Bootstrap build
- Non-bootstrap build

* Mon Feb 01 2021 Fabio Valentini <decathorpe@gmail.com> - 60-1
- Update to version 60.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 26 2021 Marian Koncek <mkoncek@redhat.com> - 60-1
- Update to upstream version 60

* Wed Jul 29 2020 Marian Koncek <mkoncek@redhat.com> - 50-1
- Update to upstream version 50

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 50-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu May 14 2020 Fabio Valentini <decathorpe@gmail.com> - 50-1
- Update to version 50.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 40-8
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 40-7
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Michael Simacek <msimacek@redhat.com> - 40-3
- Remove dependency on site-plugin and checkstyle-plugin

* Thu Aug 11 2016 Michael Simacek <msimacek@redhat.com> - 40-2
- Update upstream URLs

* Thu Aug 11 2016 Michael Simacek <msimacek@redhat.com> - 40-1
- Update to upstream version 40

* Mon Apr 11 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 39-1
- Update to upstream version 39

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 38-1
- Update to upstream version 38

* Fri Aug  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-2
- Remove maven-enforcer-plugin from POM

* Wed Aug  5 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 37-1
- Update to upstream version 37

* Thu Jul 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 36-1
- Update to upstream version 36

* Tue Jul 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 35-1
- Update to upstream version 35

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Michael Simacek <msimacek@redhat.com> - 34-2
- Add BR maven-site-plugin

* Mon Oct 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 34-1
- Update to upstream version 34

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-3
- Rebuild to regenerate Maven auto-requires

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-2
- Regenerate requires

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 33-1
- Update to upstream version 33

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 32-3
- Add ASL 2.0 license text to rpms

* Mon Apr 22 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 32-2
- Update to latest upstream (#948704)

* Fri Feb  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 31-1
- Update to upstream version 31

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 30-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 30-4
- Build with xmvn

* Fri Jan  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-3
- Disable maven-plugin-cobertura

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-2
- Install additional depmap
- Resolves: rhbz#880619

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-1
- Update to upstream version 30

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 29-1
- Update to latest upstream.

* Tue Mar  8 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 28-2
- Remove parent from pom.xml (no codehaus-parent in Fedora now)

* Mon Mar  7 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 28-1
- Update to latest upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-5
- Add component-javadoc to R

* Thu Sep 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-4
- Add forgotten jpackage-utils BR

* Tue Sep 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-3
- Change to license used by upstream (ASL 2.0)

* Mon Sep  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-2
- Removed %%build section and BRs (not really needed)

* Mon Sep  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 24-1
- Initial version of the package
