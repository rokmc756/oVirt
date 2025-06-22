#!/bin/bash


dnf -y install centos-release-ovirt45 epel-release

# dnf config-manager --enable devel
# dnf config-manager --enable crb


dnf remove -y openjdk-1.8.0*

# https://stackoverflow.com/questions/69915828/shebang-changed-to-usr-libexec-platform-python-when-building-python-rpm-package


# dnf install -y maven-* junit-* yum-utils dnf-utils maven-local nodejs rpmlint \
dnf install -y junit-* yum-utils dnf-utils maven-local nodejs rpmlint \
gobject-introspection-devel gtk-doc meson opus-devel spice-protocol maven-parent \
usbredir-devel vala mvn*antlr* gcc-c++ binutils-devel doxygen elfutils-devel \
elfutils-libelf-devel gdb gperf json-c-devel python3-sphinx rpm-devel chrpath cmake \
help2man pkgconfig python3-devel utf8cpp-devel doxygen graphviz \
maven-shared-utils plexus-classworlds plexus-interpolation plexus-utils \
ant-junit aqute-bnd jakarta-activation javamail openssl-devel python3-devel \
python3-parameterized python3-pytest swig asciidoc ansible-core ansible-macros \
selinux-policy-devel ovirt-engine-build-dependencies jackson-annotations \
jackson-core jackson-databind ovirt-engine-wildfly git ovirt-engine-nodejs-modules \
python3-mock python3-testscenarios python3-testtools python3-nose python3.11-devel \
python3.11-setuptools libxml2-devel python3-construct libcurl-devel vsftpd \
gtest-devel libvirt-devel perl-generators java-1.8.0-openjdk-devel jflex \
nss-devel nss-tools opensc pcsc-lite-devel softhsm intltool rest-devel \
check-devel jackson-jaxrs-json-provider gettext-devel intltool \
libsoup-devel maven-shared-utils maven-source-plugin mockito \
plexus-classworlds plexus-interpolation plexus-utils slf4j-jdk14 \
xorg-x11-server-Xvfb cyrus-sasl-devel gstreamer1-devel \
gstreamer1-plugins-base-devel gtk3-devel intltool json-glib-devel \
libacl-devel libcacard-devel libcap-ng-devel libjpeg-turbo-devel \
lz4-devel pixman-devel polkit-devel usbutils \
classloader-leak-test-framework maven-plugin-bundle \
postgresql-contrib postgresql-test-rpm-macros gettext-devel \
PEGTL-static audit-libs-devel catch1-devel dbus-glib-devel execstack \
libgcrypt-devel libnotify-devel libqb-devel librsvg2-devel protobuf-compiler \
protobuf-devel yajl-devel exec-maven-plugin junit5 \
maven-plugin-build-helper ongres-stringprep string-template-maven-plugin libuuid-devel \
jackson-* maven-plugin-* maven-antrun-plugin maven-clean-plugin sisu-* \
modello-* maven-shade-plugin apache-commons-logging java-javadoc \
maven-shared-utils plexus-classworlds plexus-interpolation plexus-utils \
apache-commons-* jdom-* ansible-test maven-dependency-plugin *resteasy* \
*govirt* *gtk-vnc* *libvirt-glib* *spice-client-gtk-3* spec-version-maven-plugin \
jaxb-runtime mojo-parent plexus-components-pom xmlunit* maven-invoker-javadoc \
plexus-component-factories-pom modello maven-reporting-api plexus-i18n \
plexus-velocity xml-* xalan* wayland-* virt-viewer maven-surefire-* \
jakarta-* ws-commons-util ovirt-engine-extensions-api unboundid-ldapsdk \
maven-local-openjdk8 mojo-executor-maven-plugin ongres-scram* \
maven-doxia* python3-xeddsa bouncycastle-pkix bouncycastle-pg cryptopp* \
ed25519-java xorg-x11-proto-devel-2024* testng* replacer maven-invoker \
ncompress


# maven-shared-utils < 3.3.4-3 is needed by ws-commons-util-1.0.2-1.1.el9.noarch
# plexus-classworlds < 2.6.0-11 is needed by ws-commons-util-1.0.2-1.1.el9.noarch
# plexus-interpolation < 1.26-11 is needed by ws-commons-util-1.0.2-1.1.el9.noarch
# plexus-utils < 3.3.0-10 is needed by ws-commons-util-1.0.2-1.1.el9.noarch

# python3dist
# libcacard-devel
# spice-gtk-*
# mvn-*



