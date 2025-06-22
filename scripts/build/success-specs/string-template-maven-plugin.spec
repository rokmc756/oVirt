Name:           string-template-maven-plugin
Version:        1.1
Release:        4%{?dist}
Summary:        Execute StringTemplate files during a maven build

License:        MIT
URL:            http://kevinbirch.github.io/%{name}/
BuildArch:      noarch
Source0:        https://github.com/kevinbirch/%{name}/archive/%{name}-%{version}.tar.gz
# The license file was added to git after the last release
Source1:        https://raw.githubusercontent.com/kevinbirch/%{name}/master/LICENSE
# Update org.sonatype.aether to org.eclipse.aether
# https://github.com/kevinbirch/string-template-maven-plugin/pull/12
Patch0:         %{name}-aether.patch
# Tell javadoc about maven mojo tags
# https://github.com/kevinbirch/string-template-maven-plugin/pull/13
Patch1:         %{name}-javadoc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.twdata.maven:mojo-executor-maven-plugin)

%description
This plugin allows you to execute StringTemplate template files during
your build.  The values for templates can come from static declarations
or from a Java class specified to be executed.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1
cp -p %{SOURCE1} .

# Updated name
%pom_change_dep :stringtemplate :ST4

# We do not need the versions reports
%pom_remove_plugin :versions-maven-plugin

# We do not have the secret key for signing jars
%pom_remove_plugin :maven-gpg-plugin

# We do not create any soure JARs
%pom_remove_plugin :maven-source-plugin

# We use xmvn-javadoc instead of maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 1.1-1
- Initial RPM
