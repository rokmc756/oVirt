#!/bin/bash

SOURCE_LINK="https://mirror.stream.centos.org/SIGs/9-stream/virt/source/ovirt-45/"
RPMS_LINK="https://mirror.stream.centos.org/SIGs/9-stream/virt/x86_64/ovirt-45/"
BASE_DIR="/extra-usb-storage/dnf-repos"


mkdir $BASE_DIR/ovirt45/$i > /dev/null 2>&1

echo "" > $BASE_DIR/ovirt4.log 2>&1
echo "[ Start ] ###########################################   $(date +%Y-%m-%d' '%T)    ##########################################" >> $BASE_DIR/ovirt4.log 2>&1

reposync --repo=SRPMS --repofrompath=SRPMS,$SOURCE_LINK --download-metadata \
--download-path $BASE_DIR/ovirt45/SRPMS --remote-time >> $BASE_DIR/ovirt4.log 2>&1   # --delete

reposync --repo=RPMS --repofrompath=RPMS,$RPMS_LINK --download-metadata \
--download-path $BASE_DIR/ovirt45/RPMS --remote-time >> $BASE_DIR/ovirt4.log 2>&1     # --delete

echo "[ End ] ###########################################   $(date +%Y-%m-%d' '%T)    ##########################################" >> $BASE_DIR/ovirt4.log 2>&1

