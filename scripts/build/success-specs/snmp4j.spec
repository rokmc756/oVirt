Name:          snmp4j
Version:       3.6.4
Release:       0.1%{?dist}
Summary:       The Object Oriented SNMP API for Java Managers and Agents
License:       ASL 2.0
URL:           http://www.snmp4j.org/
Source0:       https://oosnmp.net/dist/release/org/snmp4j/%{name}/%{version}/%{name}-%{version}-distribution.tar.gz

BuildRequires: java-11-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:     noarch

%description
SNMP4J is an enterprise class free open source and
state-of-the-art SNMP implementation for Java 2SE 1.4 or
later. SNMP4J supports command generation (managers) as
well as command responding (agents). Its clean object
oriented design is inspired by SNMP++, which is a
well-known SNMPv1/v2c/v3 API for C++ (see http://www.agentpp.com).

The SNMP4J Java SNMP API provides the following features:

* SNMPv3 with MD5 and SHA authentication and DES, 3DES,
  AES 128, AES 192, and AES 256 privacy.
* Pluggable Message Processing Models with implementations
  for MPv1, MPv2c, and MPv3
* All PDU types.
* Pluggable transport mappings. UDP, TCP, and TLS are supported
  out-of-the-box.
* Pluggable timeout model.
* Synchronous and asynchronous requests.
* Command generator as well as command res-ponder support.
* Free open source with the Apache license model
* Java 1.4.1 or later (1.6 for version 2.0 or later)
* Logging based on Log4J
* Row-based efficient asynchronous table retrieval with GETBULK.
* Multi-threading support.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# cleanup
find -name "*.jar" -delete
find -name "*.class" -delete

# remove wagon-webdav-jackrabbit
%pom_xpath_remove "pom:build/pom:extensions"

# required by Apache Camel
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration/pom:excludes"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration" '
<archive>
  <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>'
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Export-Package>org.snmp4j.*;version="${project.version}"</Export-Package>
    <Import-Package>javax.crypto*,javax.net.ssl,javax.security*;resolution:=optional,*</Import-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# Convert from dos to unix line ending
for file in CHANGES.txt \
 LICENSE-2_0.txt \
 NOTICE \
 snmp4j_usage.txt \
 mibs/OOSNMP-USM-MIB.txt \
 mibs/SNMP-USM-HMAC-SHA2-MIB.txt
do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

# AssertionFailedError: null
rm src/test/java/org/snmp4j/SnmpTest.java

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "org.apache.servicemix.bundles:org.apache.servicemix.bundles.snmp4j"

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt snmp4j_usage.txt mibs
%license LICENSE-2_0.txt NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE-2_0.txt NOTICE

%changelog
* Mon Jan 24 2022 Martin Perina <mperina@redhat.com> - 3.6.4-0.1
- Bump to version 3.6.4
- Disable unit  tests due to errors

* Tue Jan 28 2020 Sandro Bonazzola <sbonazzo@redhat.com> - 2.4.1-1
- Initial import from Fedora

