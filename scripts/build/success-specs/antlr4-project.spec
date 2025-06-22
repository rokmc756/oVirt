# NOTE: A PHP runtime is available as a separate project:
# https://github.com/antlr/antlr-php-runtime/
#
# NOTE: A dart target is available, should dart ever be added to Fedora.
#
# NOTE: A C# target is available.  It can be built into a DLL successfully with
# the dotnet package, but we don't seem to be able to create a nupkg with the
# current tooling, nor is there a well-defined place where a nupkg should be
# installed.


Name:           antlr4-project
Version:        4.9.3
Release:        1.2%{?dist}
Summary:        Parser generator (ANother Tool for Language Recognition)

License:        BSD
URL:            https://www.antlr.org/
Source0:        https://github.com/antlr/antlr4/archive/%{version}/antlr4-%{version}.tar.gz
# Fix some javadoc problems
# https://github.com/antlr/antlr4/pull/2960
Patch0:         antlr4-javadoc.patch

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(com.webguys:string-template-maven-plugin)
BuildRequires:  mvn(org.abego.treelayout:org.abego.treelayout.core)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.glassfish:javax.json)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  utf8cpp-devel

# We can no longer successfully build or install the mono runtime.  See comment
# at the top of this spec file.
# This can be removed when Fedora 37 reaches EOL.
Obsoletes:      mono-antlr4-runtime < 4.9.1

# We can no longer successfully build javadoc documentation.
# See https://github.com/fedora-java/xmvn/issues/58
Obsoletes:      antlr4-javadoc < 4.9.2-2

%global _desc %{expand:
ANTLR (ANother Tool for Language Recognition) is a powerful parser
generator for reading, processing, executing, or translating structured
text or binary files.  It is widely used to build languages, tools, and
frameworks.  From a grammar, ANTLR generates a parser that can build
and walk parse trees.}

%description %_desc

%package     -n antlr4-runtime-test-annotations
Summary:        ANTLR runtime test annotations
BuildArch:      noarch

%description -n antlr4-runtime-test-annotations %_desc

This package provides runtime library test annotations used by Java
ANTLR parsers.

%package     -n antlr4-runtime-test-annotation-processors
Summary:        ANTLR runtime test annotation processors
BuildArch:      noarch
Requires:       antlr4-runtime-test-annotations = %{version}-%{release}

%description -n antlr4-runtime-test-annotation-processors %_desc

This package provides runtime library test annotation processors used by
Java ANTLR parsers.

%package     -n antlr4-runtime
Summary:        ANTLR runtime
BuildArch:      noarch

%description -n antlr4-runtime %_desc

This package provides the runtime library used by Java ANTLR parsers.

%package     -n antlr4
Summary:        Parser generator (ANother Tool for Language Recognition)
BuildArch:      noarch
Requires:       antlr4-runtime = %{version}-%{release}
Requires:       mvn(com.sun:tools)

%description -n antlr4 %_desc

This package provides the ANTLR parser generator.

%package     -n antlr4-maven-plugin
Summary:        ANTLR plugin for Apache Maven
BuildArch:      noarch
Requires:       antlr4 = %{version}-%{release}

%description -n antlr4-maven-plugin %_desc

This package provides a plugin for Apache Maven which can be used to
generate ANTLR parsers during project build.

%package     -n antlr4-doc
Summary:        ANTLR4 documentation
BuildArch:      noarch

%description -n antlr4-doc %_desc

This package contains ANTLR4 documentation.

%package     -n antlr4-cpp-runtime
Summary:        ANTLR runtime for C++

%description -n antlr4-cpp-runtime %_desc

This package provides the runtime library used by C++ ANTLR parsers.

%package     -n antlr4-cpp-runtime-devel
Summary:        Header files for programs that use C++ ANTLR parsers
Requires:       antlr4-cpp-runtime%{?_isa} = %{version}-%{release}

%description -n antlr4-cpp-runtime-devel %_desc

This package provides header files for programs that use C++ ANTLR
parsers.


%package     -n python3-antlr4-runtime
Summary:        ANTLR runtime for Python 3
BuildArch:      noarch

%description -n python3-antlr4-runtime %_desc

This package provides the runtime library used by Python 3 ANTLR parsers.


%prep
%autosetup -n antlr4-%{version} -p1
find -name \*.jar -delete

# Update for recent stringtemplate versions
sed -i 's,\\>,>,g' tool/resources/org/antlr/v4/tool/templates/unicodedata.st

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# Xmvn javadoc mojo is in use
%pom_remove_plugin -r :maven-javadoc-plugin

# Missing test deps: org.seleniumhq.selenium:selenium-java
%pom_disable_module runtime-testsuite
%pom_disable_module tool-testsuite

# Missing test dep:
# io.takari.maven.plugins:takari-plugin-testing
%pom_remove_dep -r :takari-plugin-testing

# Missing plugin
# io.takari.maven.plugins:takari-lifecycle-plugin
%pom_remove_plugin -r :takari-lifecycle-plugin

# Don't bundle dependencies
%pom_remove_plugin :maven-shade-plugin tool

# Need some javax.json classes
%pom_add_dep javax.json:javax.json-api tool

# Replace dep on deprecated maven-project with maven-core
%pom_change_dep org.apache.maven:maven-project:2.2.1 org.apache.maven:maven-core:3.6.1 antlr4-maven-plugin

# Replace dep on maven-jdk-tools-wrapper with dep on tools.jar
%pom_change_dep :maven-jdk-tools-wrapper com.sun:tools runtime-testsuite/processors

%mvn_package :antlr4-master antlr4-runtime


# Build for JDK 1.8
sed -i 's/1\.7/1.8/g' pom.xml

# Use utf8cpp instead of the deprecated wstring_convert
sed -i 's/# \(.*DUSE_UTF8_INSTEAD_OF_CODECVT.*\)/\1/' runtime/Cpp/CMakeLists.txt

# Change library install directory on 64-bit platforms
if [ "%{_lib}" != "lib" ]; then
  sed -i 's/DESTINATION lib/&64/' runtime/Cpp/runtime/CMakeLists.txt
fi

%build
export JAVA_HOME=%{_jvmdir}/java

# Build for Java
# Due to the missing takari packages, we cannot run the tests
%mvn_build -s -f -j -- -Dsource=1.8

# Build the C++ runtime
cd runtime/Cpp
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .
%cmake_build
cd -

# Build the Python 3 runtime
cd runtime/Python3
%py3_build
cd -


%install
# Install for Java; cannot use %%mvn_install as it passes %%name to -n
xmvn-install -R .xmvn-reactor -n antlr4 -d %{buildroot}
jdir=target/site/apidocs
[ -d .xmvn/apidocs ] && jdir=.xmvn/apidocs
mkdir -p %{buildroot}%{_licensedir}
if [ -d "${jdir}" ]; then
   install -dm755 %{buildroot}%{_javadocdir}/antlr4
   cp -pr "${jdir}"/* %{buildroot}%{_javadocdir}/antlr4
   echo '%{_javadocdir}/antlr4' >>.mfiles-javadoc
fi

%jpackage_script org.antlr.v4.Tool "" "" antlr4/antlr4:antlr3-runtime:antlr4/antlr4-runtime:stringtemplate4:treelayout antlr4 true

# Install the C++ runtime
cd runtime/Cpp
%cmake_install
rm -f %{buildroot}%{_libdir}/libantlr4-runtime.a
cd -


# Install the Python 3 runtime
cd runtime/Python3
%py3_install
sed 's,#!python,#!%{python3},' bin/pygrun > %{buildroot}%{_bindir}/pygrun
touch -r bin/pygrun %{buildroot}%{_bindir}/pygrun
chmod 0755 %{buildroot}%{_bindir}/pygrun
cd -


# Create man pages
export PYTHONPATH=%{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_mandir}/man1
cd %{buildroot}%{_bindir}
help2man -N --version-string=%{version} -h '' ./antlr4 > \
  %{buildroot}%{_mandir}/man1/antlr4.1
help2man -N --version-string=%{version} ./pygrun > \
  %{buildroot}%{_mandir}/man1/pygrun.1
cd -

# Clean up bits we do not want
rm -fr %{buildroot}%{_docdir}/libantlr4

%files -n antlr4-runtime-test-annotations -f .mfiles-antlr4-runtime-test-annotations
%license LICENSE.txt

%files -n antlr4-runtime-test-annotation-processors -f .mfiles-antlr4-runtime-test-annotation-processors

%files -n antlr4-runtime -f .mfiles-antlr4-runtime
%doc README.md
%license LICENSE.txt

%files -n antlr4 -f .mfiles-antlr4
%doc CHANGES.txt contributors.txt
%{_bindir}/antlr4
%{_mandir}/man1/antlr4.1*

%files -n antlr4-maven-plugin -f .mfiles-antlr4-maven-plugin

%files -n antlr4-doc
%doc doc
%license LICENSE.txt

%files -n antlr4-cpp-runtime
%doc runtime/Cpp/README.md
%license LICENSE.txt
%{_libdir}/libantlr4-runtime.so.%{version}

%files -n antlr4-cpp-runtime-devel
%doc runtime/Cpp/cmake/Antlr4Package.md runtime/Cpp/cmake/README.md
%{_includedir}/antlr4-runtime/
%{_libdir}/libantlr4-runtime.so



%files -n python3-antlr4-runtime
%doc runtime/Python3/README.txt
%license LICENSE.txt
%{_bindir}/pygrun
%{_mandir}/man1/pygrun.1*
%python3_sitelib/antlr4/
%python3_sitelib/antlr4*.egg-info/


%changelog
* Sun Jan 16 2022 Martin Perina <mperina@redhat.com> - 4.9.3-1.2
- Non-bootstrap build

* Sun Jan 16 2022 Martin Perina <mperina@redhat.com> - 4.9.3-1.1
- Bootstrap build
- Remove swift, go and javascript builds due to dependencies issues and because they are not needed for oVirt

* Sun Nov  7 2021 Jerry James <loganjerry@gmail.com> - 4.9.3-1
- Version 4.9.3
- Drop upstreamed -unicode-properties and -utf8cpp patches

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Jerry James <loganjerry@gmail.com> - 4.9.2-2
- Drop the javadoc subpackage due to xmvn errors
- Fix an invalid RPATH in the swift runtime library

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.9.2-2
- Rebuilt for Python 3.10

* Fri Mar 12 2021 Jerry James <loganjerry@gmail.com> - 4.9.2-1
- Version 4.9.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Jerry James <loganjerry@gmail.com> - 4.9.1-1
- Version 4.9.1
- Remove the mono runtime, which no longer builds on Fedora

* Mon Nov 30 2020 Jerry James <loganjerry@gmail.com> - 4.9-1
- Version 4.9
- Add the JavaScript runtime
- Add -utf8cpp patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 4.8-4
- Fix cmake and javadoc issues

* Tue Jul 21 2020 Mat Booth <mat.booth@redhat.com> - 4.8-3
- Allow building against JDK 11

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.8-2
- Rebuilt for Python 3.9

* Tue Jan 21 2020 Jerry James <loganjerry@gmail.com> - 4.8-1
- Initial RPM, based on old antlr4.spec
