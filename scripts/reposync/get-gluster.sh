#!/bin/bash

BASE_DIR="/extra-usb-storage/dnf-repos"

mkdir $BASE_DIR/gluster/$i > /dev/null 2>&1

echo "" > $BASE_DIR/gluster.log 2>&1
echo "[ Start ] ###########################################   $(date +%Y-%m-%d' '%T)    ##########################################" >> $BASE_DIR/gluster.log 2>&1

for i in `seq 9 11`
do


    SOURCE_LINK="https://mirror.stream.centos.org/SIGs/9-stream/storage/source/gluster-$i/"
    RPMS_LINK="https://mirror.stream.centos.org/SIGs/9-stream/storage/x86_64/gluster-$i/"

    reposync --repo=SRPMS --repofrompath=SRPMS,$SOURCE_LINK --download-metadata --download-path $BASE_DIR/gluster/$i --remote-time >> $BASE_DIR/gluster.log 2>&1 # --delete
    reposync --repo=RPMS --repofrompath=RPMS,$RPMS_LINK --download-metadata --download-path $BASE_DIR/gluster/$i --remote-time >> $BASE_DIR/gluster.log 2>&1    # --delete

done

echo "[ End ] ###########################################   $(date +%Y-%m-%d' '%T)    ##########################################" >> $BASE_DIR/gluster.log 2>&1

