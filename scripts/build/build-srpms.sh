#!/bin/bash

NORMAL=`echo -e '\033[0m'`
RED=`echo -e '\033[31m'`
GREEN=`echo -e '\033[0;32m'`
LGREEN=`echo -e '\033[1;32m'`
BLUE=`echo -e '\033[0;34m'`
LBLUE=`echo -e '\033[1;34m'`
YELLOW=`echo -e '\033[0;33m'`
NC=`echo -e '\033[0m'` # No Color

BASE_DIR=/root/ovirt45
BUILD_DIR=/root/rpmbuild

mkdir $BASE_DIR/logs > /dev/null 2>&1
start_date=$(date +%Y-%m-%d-%H-%M)


for spec in `find /root/rpmbuild/SPECS -name '*.spec'`
do

	pkg_name=`echo $spec | cut -d '/' -f 5 | cut -d . -f 1`

	echo "$spec Start Date : $(date +%Y-%m-%d' '%H:%M:%S)" >> $BASE_DIR/logs/build-ovirt-$start_date.log
	rpmbuild -ba $spec > $BASE_DIR/logs/$pkg_name-build-$(date +%Y-%m-%d-%H-%M).log 2>&1

	if [ $? == 0 ]; then
		echo "${GREEN}Success ${NC}: $spec - $(date +%Y-%m-%d' '%H:%M:%S)"
		echo "$spec : Success - $(date +%Y-%m-%d' '%H:%M:%S)" >> $BASE_DIR/logs/build-ovirt-$start_date.log
	        mv -fv $spec $BASE_DIR/success-specs/
	        rm -f $BASE_DIR/logs/$pkg_name-build-*.log
	else
		echo "${RED}Failure ${NC}: $spec - $(date +%Y-%m-%d' '%H:%M:%S)"
		echo "$spec : Failure - $(date +%Y-%m-%d' '%H:%M:%S)" >> $BASE_DIR/logs/build-ovirt-$start_date.log
	fi

	echo "$spec End Date : $(date +%Y-%m-%d' '%H:%M:%S)" >> $BASE_DIR/logs/build-ovirt-$start_date.log

done

echo $NC"Done"

