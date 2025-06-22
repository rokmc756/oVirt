# Copyright (c) 2000-2012, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           jdom
Version:        1.1.3
Release:        26.2%{?dist}
Summary:        Java alternative to DOM and SAX
License:        Saxpath
URL:            http://www.jdom.org/
Source0:        http://jdom.org/dist/binary/archive/jdom-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/org/jdom/jdom/%{version}/jdom-%{version}.pom
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-1.1-OSGiManifest.patch

BuildRequires:  javapackages-local
BuildRequires:  ant

BuildArch:      noarch

%description
JDOM is, quite simply, a Java representation of an XML document. JDOM
provides a way to represent that document for easy and efficient
reading, manipulation, and writing. It has a straightforward API, is a
lightweight and fast, and is optimized for the Java programmer. It's an
alternative to DOM and SAX, although it integrates well with both DOM
and SAX.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demos for %{name}
Requires:       %{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%build
%ant -Dcompile.source=1.6 -Dcompile.target=1.6 -Dj2se.apidoc=%{_javadocdir}/java package javadoc-link

%install
%mvn_file : %{name}
%mvn_alias : jdom:jdom
%mvn_artifact %{SOURCE1} build/%{name}-*-snap.jar
%mvn_install -J build/apidocs

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc CHANGES.txt COMMITTERS.txt README.txt TODO.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%files demo
%{_datadir}/%{name}
%license LICENSE.txt

%changelog
* Wed Sep 29 2021 Martin Perina <mperina@redhat.com> - 1.1.3-26.2
- Non-bootstrap build

* Mon Aug 16 2021 Martin Perina <mperina@redhat.com> - 1.1.3-26.1
- Bootstrap build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-25
- Bump release

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-20
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0:1.1.3-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.3-21
- Fix compilation with Java 11.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-19
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.3-18
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Michael Simacek <msimacek@redhat.com> - 0:1.1.3-17
- Correct license to Saxpath

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 0:1.1.3-13
- fix JAR installation

* Wed Mar 22 2017 Michael Simacek <msimacek@redhat.com> - 0:1.1.3-12
- Install with XMvn

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-9
- Add build-requires on javapackages-local

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.3-6
- Use .mfiles generated during build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.3-3
- Add jaxen on build classpath to compile full support

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.3-1
- Update to upstream 1.1.3 release.

* Fri Apr 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 0:1.1.2-3
- Update OSGI Manifest.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 2 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.2-1
- New upstream version. 
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.1-4
- Add compatibility depmap jdom:jdom
- Versionless jars & javadocs

* Wed Nov 3 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.1-3
- Really fix license tag.

* Mon Nov 1 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.1-2
- Drop gcj support.
- Fix license tag.
- Fix requires and build requires.

* Fri Feb 5 2010 Mary Ellen Foster <mefoster at gmail.com> 0:1.1.1-1
- Update to 1.1.1 bug#316380
- Add maven dependency information
- Make javadoc and demo subpackages noarch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-7.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 21 2008 Andrew Overholt <overholt@redhat.com> 1.0-5.5
- Add OSGi manifest information

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0-5.4
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0-5jpp.3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0-5jpp.2
- Autorebuild for GCC 4.3

* Thu Sep 20 2007 Deepak Bhole <dbhole@redhat.com> - 0:1.0-4jpp.2
- Add %%{?dist} as per policy

* Fri Aug 04 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-4jpp.1
- Added missing requirements.
- Remove jaxen requirement, since we don't have it in fc yet.
- Merge with fc spec.

* Tue Apr 11 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-3jpp
- First JPP-1.7 release
- Drop false xalan dependency

* Tue Oct 11 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-2jpp
- Add jaxen to Requires and classpath

* Sat Sep 18 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- Upgrade to 1.0 final

* Tue Sep 07 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.rc1.1jpp
- Upgrade to 1.0-rc1

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0-0.b9.4jpp
- Rebuild with ant-1.6.2

* Mon Jul 19 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.b9.3jpp
- Add non-versioned javadoc dir symlink.
- Crosslink with local J2SE javadocs.

* Thu Jan 22 2004 David Walluck <david@anti-microsoft.org> 0:1.0-0.b9.2jpp
- fix URL

* Wed Jan 21 2004 David Walluck <david@anti-microsoft.org> 0:1.0-0.b9.1jpp
- b9
- don't use classic compiler

* Thu Mar 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.b8.2jpp
- Adapted to JPackage 1.5.
- Use sed instead of bash 2 extension when symlinking jars during build.

* Wed May 08 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b8.1jpp
- vendor, distribution, group tags

* Sat Jan 19 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b7.6jpp
- versioned dir for javadoc
- requires xalan-j2 >= 2.2.0
- no dependencies for javadoc package
- stricter dependency for demo package
- section macro

* Wed Dec 5 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b7.5jpp
- javadoc into javadoc package

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.0-0.b7.4jpp
- removed packager tag
- new jpp extension
- added xalan 2.2.D13 support

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b7.3jpp
- used original tarball

* Sun Sep 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b7.2jpp
- first unified release
- s/jPackage/JPackage

* Mon Sep 17 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-0.b7.1mdk
- Requires and BuildRequires xalan-j2
- vendor tag
- packager tag
- s/Copyright/License/
- truncated description to 72 columns in spec
- spec cleanup
- used versioned jar
- added demo package

*  Sat Feb 17 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0b6-1mdk
- first Mandrake release
