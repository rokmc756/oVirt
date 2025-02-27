#!/bin/bash

build_host="192.168.2.170"
web_ui_build_dir="/root/rpmbuild/BUILD/ovirt-web-ui-1.9.3"

img_files="
/src/components/VmConsole/images/disconnect_icon.png
/src/components/VmConsole/images/download_icon.png
/doc/screenshots/v1.1.0_2017_Nov/01_vmsList.png
/doc/screenshots/v1.3.2_2017-Nov/03_editVm.png
/doc/screenshots/v1.3.2_2017-Nov/02_vmDetail.png
/doc/screenshots/v1.3.2_2017-Nov/01_vmsList.png
/doc/screenshots/v1.0.0_2017-Jun/03_editVm.png
/doc/screenshots/v1.0.0_2017-Jun/02_vmDetail.png
/doc/screenshots/v1.0.0_2017-Jun/04_createVm.png
/doc/screenshots/v1.0.0_2017-Jun/01_vmsList.png
/doc/screenshots/v0.1.2_2017-Feb/02_vmDetail.png
/doc/screenshots/v0.1.2_2017-Feb/01_vmsList.png
/doc/screenshots/v1.5.0_2019-Feb/01_vm_dashboard.png
/doc/screenshots/v1.1.0_2017_Jun/03_consoleOptionsVmDisks.png
/doc/screenshots/v1.1.0_2017_Jun/04_vmEdit.png
/doc/screenshots/v1.1.0_2017_Jun/02_vmDetail.png
/doc/screenshots/v1.1.0_2017_Jun/01_vmsList.png
/doc/screenshots/v0.1.3_2017-Feb/03_aboutDialog.png
/doc/screenshots/v0.1.3_2017-Feb/02_vmDetail.png
/doc/screenshots/v0.1.3_2017-Feb/01_vmsList.png
/doc/screenshots/v1.3.9_2018-May/02_createVM.png
/doc/screenshots/v1.3.9_2018-May/05_vmDetailExpanded.png
/doc/screenshots/v1.3.9_2018-May/06_about.png
/doc/screenshots/v1.3.9_2018-May/04_addNIC.png
/doc/screenshots/v1.3.9_2018-May/01_vmList.png
/doc/screenshots/v1.3.9_2018-May/03_addDisk.png
/branding/images/ovirt_lost_map.png
/branding/images/ovirt_logo.png
/branding/images/ovirt_about_bg.png
/branding/images/ovirt_masthead_bg.png
/branding/images/dialog/error.png
/branding/images/ovirt_landing_bg_top_right.png
/branding/images/ovirt_middle_logo.png
/branding/images/ovirt_landing_bg_bottom_left.png
/branding/images/favicon-16x16.png
/branding/images/favicon-32x32.png
/branding/images/ovirt_masthead_logo.png
"

for img in $img_files
do

    mkdir -p ./${img%/*.png} > /dev/null 2>&1

    rsync -ratlzv --rsh='/usr/bin/sshpass -p changeme ssh -o StrictHostKeyChecking=no -l root' $build_host:$web_ui_build_dir$img .$web_uil_build_dir${img%/*.png}/

done

find ./ -name "*.png"

