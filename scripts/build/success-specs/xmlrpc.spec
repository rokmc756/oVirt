Name:           xmlrpc
Version:        3.1.3
Release:        1.1%{?dist}
Summary:        Java XML-RPC implementation
License:        ASL 2.0
URL:            http://ws.apache.org/xmlrpc/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/ws/xmlrpc/sources/apache-xmlrpc-%{version}-src.tar.bz2
Patch0:         %{name}-client-addosgimanifest.patch
Patch1:         %{name}-common-addosgimanifest.patch
Patch2:         %{name}-javax-methods.patch
Patch3:         %{name}-server-addosgimanifest.patch
Patch4:         %{name}-disallow-deserialization-of-ex-serializable-tags.patch
Patch5:         %{name}-disallow-loading-external-dtd.patch

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.ws.commons.util:ws-commons-util)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)

# Block packages from maven:3.8 to pass the build
BuildRequires: maven < 1:3.8.0
BuildRequires: maven-lib < 1:3.8.0
BuildRequires: maven-resolver < 1:1.7.0
BuildRequires: maven-shared-utils < 3.3.4-6
BuildRequires: maven-wagon < 3.5.0
BuildRequires: plexus-cipher < 1.8
BuildRequires: plexus-classworlds < 2.6.0-13
BuildRequires: plexus-containers-component-annotations < 2.1.1
BuildRequires: plexus-interpolation < 1.26-14
BuildRequires: plexus-sec-dispatcher < 1.5
BuildRequires: plexus-utils < 3.3.0-12
BuildRequires: sisu < 1:0.3.5

%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.
Apache XML-RPC was previously known as Helma XML-RPC. If you have code
using the Helma library, all you should have to do is change the import
statements in your code from helma.xmlrpc.* to org.apache.xmlrpc.*.

%package javadoc
Summary:    Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%package common
Summary:    Common classes for XML-RPC client and server implementations
# Provide xmlrpc is not here because it would be useless due to different jar names
Obsoletes:  %{name} < 3.1.3
Obsoletes:  %{name}3-common < 3.1.3-13
Provides:   %{name}3-common = 3.1.3-13

%description common
%{summary}.

%package client
Summary:    XML-RPC client implementation
Obsoletes:  %{name}3-client < 3.1.3-13
Provides:   %{name}3-client = 3.1.3-13

%description client
%{summary}.

%package server
Summary:    XML-RPC server implementation
Obsoletes:  %{name}3-server < 3.1.3-13
Provides:   %{name}3-server = 3.1.3-13

%description server
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}-src
%patch2 -p1
pushd client
%patch0 -b .sav
popd
pushd common
%patch1 -b .sav
popd
pushd server
%patch3 -b .sav
popd
%patch4 -p1
%patch5 -p1

sed -i 's/\r//' LICENSE.txt

%pom_disable_module dist
%pom_remove_dep jaxme:jaxmeapi common
# This dep is no longer supplied by ws-commons-util
%pom_add_dep junit:junit:3.8.1:test
%pom_add_dep jakarta.xml.bind:jakarta.xml.bind-api:2.3.3
%mvn_file :{*} @1
%mvn_package :*-common %{name}

%build
# FIXME: ignore test failure because server part needs network
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files common -f .mfiles-%{name}
%license LICENSE.txt NOTICE.txt

%files client -f .mfiles-%{name}-client

%files server -f .mfiles-%{name}-server

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
* Thu Sep 22 2022 Martin Perina <mperina@redhat.com> - 3.1.3-1.1
- Block all packages from maven:3.8 module to pass the build on CS9

* Thu Feb 06 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 3.1.3-1
- Initial import on el8 from Fedora
- Dropped epoch

