#!/bin/bash

root_pass="changeme"
net_range="192.168.2"

for i in $(seq 171 177)
do

    sshpass -p "$root_pass" ssh -o StrictHostKeyChecking=no root@$net_range.$i reboot

done

