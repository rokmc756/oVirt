## What is this Ansible Playbook for oVirt
It is Ansible Playbook to deploy oVirt for CentOS 9.x. The purpose of this is only for development environment not production.

## What is oVirt?
oVirt is an open-source distributed virtualization solution, designed to manage your entire enterprise infrastructure. oVirt uses the trusted KVM hypervisor and is built upon several other community projects, including libvirt, Gluster, PatternFly, and Ansible.

## oVirt Architecture
![alt text](https://raw.githubusercontent.com/rokmc756/ovirt/main/roles/ovirt/images/ovirt-architecture.png)


## Supported Platform and OS
Virtual Machines\
Baremetal\
CentOS Stream 9.x

## Prerequisite for Ansible Host
MacOS or Windows Linux Subsysetm or Many kind of Linux Distributions should have ansible as ansible host.\
Supported OS for ansible target host should be prepared with package repository configured such as yum, dnf and apt

## Prepare Ansible Host to run this Ansible Playbook
* MacOS
```
$ xcode-select --install
$ brew install ansible
$ brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```

* Fedora/CentOS/RHEL
```
$ yum install ansible
```

### Setup NFS Server / iSCSI Target / Postgres Database for oVirt Engine
#### 1) Configure Inventory
```
$ vi ansible-hosts=co9

[all:vars]
ssh_key_filename="id_rsa"
remote_machine_username="jomoon"
remote_machine_password="changeme"
ansible_python_interpreter=/usr/bin/python3

[engine]
co9-node01      ansible_ssh_host=192.168.2.171

[workers]
co9-node02      ansible_ssh_host=192.168.2.172
co9-node03      ansible_ssh_host=192.168.2.173
co9-node04      ansible_ssh_host=192.168.2.174

[db]
co9-node05      ansible_ssh_host=192.168.2.175

[iscsi]
co9-node06      ansible_ssh_host=192.168.2.176

[nfs]
co9-node07      ansible_ssh_host=192.168.2.177
```

#### 2) Initialize Hosts to create user and ssh keys for exchaning them among all hosts
```
$ make hosts r=init s=all
```
#### 3) Configure oVirt Ansible Collection
```
$ ansible-galaxy collection install ovirt.ovirt
$ ansible-galaxy collection list | grep ovirt
ovirt.ovirt                              3.2.0

$ vi roles/ovirt/meta/main.yml
---
collections:
  - ovirt.ovirt

$ dnf install -y libxml2-devel
$ pip3 install ovirt-engine-sdk-python

```

### Setup Postgres Database / iSCSI Target / NFS Server
#### 1) Install/Uninstall Postgres Database for oVirt Engine/DW Remote Database
```
$ make postgres r=install s=all

or
$ make postgres r=uninstall s=all
```


#### 2) Setup/Remove iSCSI Target for oVirt iSCSI Storage Domain
```
$ make storage r=setup s=iscsi c=target

or
$ make storage r=remove s=iscsi c=target
```

#### 3) Setup/Remove NFS Server for oVirt NFS Storage Domain
```
$ make storage r=setup s=nfs c=server

or
$ make storage r=remove s=nfs c=server
```


### Deploy Open Virtualization
#### 1) Enable/Disable oVirt Package Repository
```
$ make ovirt r=enable s=repo

or
$ make ovirt r=disable s=repo
```

#### 2) Install/Uninstall oVirt Packages
```
$ make ovirt r=install s=pkgs

or
$ make ovirt r=uninstall s=pkgs
```

#### 3) Setup/Remove oVirt Engine
```
$ make ovirt r=setup s=engine
$ make ovirt r=setup s=sdk


or
$ make ovirt r=clean s=engine
```

#### 4) Create/Delete oVirt Data Center
```
$ make ovirt r=create s=dc

or
$ make ovirt r=delete s=dc
```

#### 5) Create/Delete oVirt Cluster
```
$ make ovirt r=create s=cluster

or
$ make ovirt r=delete s=cluster
```

#### 6) Add/Remove oVirt Hosts
```
$ make ovirt r=add s=host

or
$ make ovirt r=remove s=host
```

#### 7) Add/Remove oVirt Storage Domain
```
$ make storage r=add s=domain c=nfs
$ make storage r=add s=domain c=iscsi
$ make storage r=add s=domain c=gluster
$ make storage r=add s=domain c=local

or
$ make storage r=remove s=domain c=local
$ make storage r=remove s=domain c=gluster
$ make storage r=remove s=domain c=iscsi
$ make storage r=remove s=domain c=nfs
```

## References
- https://computingforgeeks.com/how-to-install-ovirt-engine-on-centos-stream/
- https://www.server-world.info/en/note?os=CentOS_Stream_9&p=ovirt45&f=1

## Similar Playbook
## TODO
## Debugging
## Tracking Issues

## Errors
### Hosted Engine Setup Error
- https://lists.ovirt.org/archives/list/users@ovirt.org/thread/QTQ4QMGOJLS6GNRVXI47QKI3ZULVGLOA/
```
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Fetch IPv6 CIDR for virbr0]
[ INFO  ] skipping: [localhost]
[ INFO  ] 192.168.222.1/255.255.255.0
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Add IPv4 outbound route rules]
[ INFO  ] changed: [localhost]
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Add IPv4 inbound route rules]
[ ERROR ] fatal: [localhost]: FAILED! => {"msg": "The conditional check 'not ipv6_deployment|bool and route_rules_ipv4.stdout | from_json | selectattr('priority', 'equalto', 100) | selectattr('dst', 'equalto', virbr_cidr_ipv4) | list | length == 0' failed. The error was: error while evaluating conditional (not ipv6_deployment|bool and route_rules_ipv4.stdout | from_json | selectattr('priority', 'equalto', 100) | selectattr('dst', 'equalto', virbr_cidr_ipv4) | list | length == 0): 'dict object' has no attribute 'dst'. 'dict object' has no attribute 'dst'\n\nThe error appears to be in '/usr/share/ansible/collections/ansible_collections/ovirt/ovirt/roles/hosted_engine_setup/tasks/bootstrap_local_vm/01_prepare_routing_rules.yml': line 79, column 7, but may\nbe elsewhere in the file depending on the exact syntax problem.\n\nThe offending line appears to be:\n\n      changed_when: true\n    - name: Add IPv4 inbound route rules\n      ^ here\n"}
[ ERROR ] Failed to execute stage 'Closing up': Failed getting local_vm_dir
[ INFO  ] Stage: Clean up
[ INFO  ] Cleaning temporary resources
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Execute just a specific set of steps]
```
* Resolution
- There was a NIC which has priority 100 in my case. You can find which NIC has this priority with this command,  ip -j rule | jq. This issue could be resolved by modifying network configuration in my script ( ovirt-netconfig.sh ) as below
```

# SEQ,NET,TABLE,PRIO,MTU,NETNUM,NETWORK_RANGE,ROUTABLE,AUTOCONN,CONNPERM
INFO_TABLE="
0,192.168.0.17,200,103,$MTU0,1s0,$NET0,yes,$GW0,yes,no
1,192.168.1.17,201,102,$MTUx,7s0,$NET1,yes,$GW1,no,yes
2,192.168.2.17,202,101,$MTUx,8s0,$NET2,no,$GW2,yes,no
"
```
### Repoitory Failure
```
[ INFO  ] TASK [ovirt.ovirt.engine_setup : Install required packages for oVirt Engine deployment]
[ INFO  ] ok: [localhost]
[ INFO  ] TASK [ovirt.ovirt.engine_setup : Install oVirt Engine package]
[ ERROR ] fatal: [localhost -> 192.168.222.173]: FAILED! => {"changed": false, "msg": "Failed to download metadata for repo 'centos-ceph-pacific': Cannot prepare internal mirrorlist: Curl error (6): Couldn't resolve host name for http://mirrorlist.centos.org/?release=8-stream&arch=x86_64&repo=storage-ceph-pacific [Could not resolve host: mirrorlist.centos.org]", "rc": 1, "results": []}
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Sync on engine machine]
[ INFO  ] changed: [localhost -> 192.168.222.173]
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Set destination directory path]
[ INFO  ] ok: [localhost -> localhost]
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Create destination directory]
```
* Resolution
- https://syk531.tistory.com/120
```
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
```
and
Disable centos-ceph-pacific repository


### Python Crypt module is deperecated
```
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Copy engine logs]
[ INFO  ] changed: [localhost]
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Change ownership of copied engine logs]
[ INFO  ] changed: [localhost -> localhost]
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Notify the user about a failure]
[ ERROR ] fatal: [localhost]: FAILED! => {"changed": false, "msg": "There was a failure deploying the engine on the local engine VM. The system may not be provisioned according to the playbook results: please check the logs for the issue, fix accordingly or re-deploy from scratch.\n"}
[ ERROR ] b'[DEPRECATION WARNING]: Encryption using the Python crypt module is deprecated. \n'
[ ERROR ] b'The Python crypt module is deprecated and will be removed from Python 3.13. \n'
[ ERROR ] b'Install the passlib library for continued encryption functionality. This \n'
[ ERROR ] b'feature will be removed in version 2.17. Deprecation warnings can be disabled \n'
[ ERROR ] b'by setting deprecation_warnings=False in ansible.cfg.\n'
[ ERROR ] Failed to execute stage 'Closing up': Failed executing ansible-playbook
[ INFO  ] Stage: Clean up
[ INFO  ] Cleaning temporary resources
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Execute just a specific set of steps]
[ INFO  ] ok: [localhost]
[ INFO  ] TASK [ovirt.ovirt.hosted_engine_setup : Force facts gathering]
[ INFO  ] ok: [localhost]
```

### Postgres Options Required when using Remote Database
```
[ ERROR ]
         Please note the following required changes in postgresql.conf on '192.168.2.175':
           'autovacuum_vacuum_scale_factor' is currently '0.2'. It is required to be at most '0.01'.
           'autovacuum_analyze_scale_factor' is currently '0.1'. It is required to be at most '0.075'.
           'autovacuum_max_workers' is currently '3'. It is required to be at least '6'.
           'work_mem' is currently '4096'. It is required to be at least '8192'.
           'max_connections' is currently '100'. It is required to be at least '150'.
         postgresql.conf is usually in /var/lib/pgsql/data,  or somewhere under /etc/postgresql* . You have to restart PostgreSQL after making these changes.
```
### DISPERSE Mode is not supported
```
==> vdsm.log <==
2025-02-27 18:25:13,496+0900 WARN  (jsonrpc/1) [storage.storageServer] Unsupported volume type, volume: 'distvol01', volume type: 'DISTRIBUTED_DISPERSE'. Please use the replicate type.To recover existing migrate it to supported type. (storageServer:352)
2025-02-27 18:25:13,496+0900 INFO  (jsonrpc/1) [storage.storageServer] Creating directory '/rhev/data-center/mnt/glusterSD/co9-node01:_distvol01' (storageServer:217)
2025-02-27 18:25:13,496+0900 INFO  (jsonrpc/1) [storage.fileutils] Creating directory: /rhev/data-center/mnt/glusterSD/co9-node01:_distvol01 mode: None (fileUtils:213)
2025-02-27 18:25:13,496+0900 INFO  (jsonrpc/1) [storage.mount] mounting co9-node01:/distvol01 at /rhev/data-center/mnt/glusterSD/co9-node01:_distvol01 (mount:190)
```

### Error in Creating Gluster Storage Domain
- https://unix.stackexchange.com/questions/774769/io-uring-with-fio-fails-on-rocky-9-3-w-kernel-5-14-0-362-18-1-el9-3-x86-64
$ tail -f /var/log/glusterfs/rhev-data-center-mnt-glusterSD-*.log
```
r=/usr/sbin/glusterfs --process-name fuse --volfile-server=192.168.2.171 --volfile-server=co9-node01 --volfile-server=co9-node02 --volfile-server=co9-node03 --volfile-id=/distvol01 /rhev/data-center/mnt/glusterSD/192.168.2.171:_distvol01}]
[2025-02-27 14:32:44.497650 +0000] I [glusterfsd.c:2447:daemonize] 0-glusterfs: Pid of current running process is 28546
[2025-02-27 14:32:44.505608 +0000] I [MSGID: 101190] [event-epoll.c:667:event_dispatch_epoll_worker] 0-epoll: Started thread with index [{index=0}]
[2025-02-27 14:32:44.505679 +0000] I [MSGID: 101190] [event-epoll.c:667:event_dispatch_epoll_worker] 0-epoll: Started thread with index [{index=1}]
[2025-02-27 14:32:44.506350 +0000] I [glusterfsd-mgmt.c:2209:mgmt_getspec_cbk] 0-glusterfs: Received list of available volfile servers: co9-node02:24007 co9-node03:24007
[2025-02-27 14:32:44.506381 +0000] I [MSGID: 101221] [common-utils.c:3847:gf_set_volfile_server_common] 0-gluster: duplicate entry for volfile-server [{errno=17}, {error=File exists}]
[2025-02-27 14:32:44.508104 +0000] I [io-stats.c:3711:ios_sample_buf_size_configure] 0-distvol01: Configure ios_sample_buf  size is 1024 because ios_sample_interval is 0
[2025-02-27 14:32:44.508747 +0000] I [MSGID: 114020] [client.c:2336:notify] 0-distvol01-client-0: parent translators are ready, attempting connect on transport []
[2025-02-27 14:32:44.510421 +0000] I [MSGID: 114020] [client.c:2336:notify] 0-distvol01-client-1: parent translators are ready, attempting connect on transport []
```


### glusterfs geo replication not installed
```
==> cli.log <==
[2025-02-28 06:00:23.647974 +0000] I [cli.c:828:main] 0-cli: Started running /usr/sbin/gluster with version 10.5
[2025-02-28 06:00:23.648060 +0000] I [cli.c:702:cli_rpc_init] 0-cli: Connecting to remote glusterd at co9-node01
[2025-02-28 06:00:23.651784 +0000] I [cli-cmd-volume.c:2066:cli_check_gsync_present] 0-: geo-replication not installed
[2025-02-28 06:00:23.652013 +0000] I [MSGID: 101190] [event-epoll.c:667:event_dispatch_epoll_worker] 0-epoll: Started thread with index [{index=0}]
[2025-02-28 06:00:23.652107 +0000] I [MSGID: 101190] [event-epoll.c:667:event_dispatch_epoll_worker] 0-epoll: Started thread with index [{index=1}]
[2025-02-28 06:00:23.652635 +0000] I [cli-rpc-ops.c:767:gf_cli_get_volume_cbk] 0-cli: Received resp to get vol: 0
[2025-02-28 06:00:23.653123 +0000] I [input.c:31:cli_batch] 0-: Exiting with: 0


$ dnf install -y glusterfs-geo-replication

```

### oVirt Engine Web UI not Responding
- It was resolved by DNS Config in Desktop Rebooted and dns cache may be deleted

### iSCSI Login Problem
- In case woring iqn of iscsi target in /etc/iscsi/initiatorname.iscsi, it would be failed to create iscsi storage domain.
If there are nothing in /etc/iscsi directory, vdsm create new initiatorname.iscsi. So, make empty directory to /etc/iscsi in order to solve this problem.

### Prepare CentOS for Hosted Engine
1) yum repo
mirror -> valut
disable ceph repo

