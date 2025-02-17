## What is this Ansible Playbook for oVirt
It is Ansible Playbook to deploy oVirt for Rocky/CentOS 9.x. The purpose of this is only for development environment not production.

## What is oVirt?
OKD is the community distribution of Kubernetes optimized for continuous application development and multi-tenant deployment. It adds developer and operational-centric tools on top of Kubernetes, enabling rapid application development, easy deployment and scaling, and long-term lifecycle maintenance.

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

## How to Deploy and Destroy oVirt
### Download oVirt Software Binaries to Ansible Files Directory
```
$ make download

```
### Setup DNS with FreeIPA
#### 1) Configure Varialbes for DNS Zone and Records
```
---
_dns:
  zone:
    - { name: jtest.pivotal.io, type: forward }
    - { name: 2.168.192.in-addr.arpa, type: reverse }
  resource:
    forward:
      - {  name: "co9-node01",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.171"  }
      - {  name: "co9-node02",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.172"  }
      - {  name: "co9-node03",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.173"  }
      - {  name: "co9-node04",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.174"  }
      - {  name: "co9-node05",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.175"  }
      - {  name: "co9-node06",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.176"  }
      - {  name: "co9-node07",    i   zone: "okd4.pivotal.io",  type: "-a-rec",  value: "192.168.2.177"  }
    reverse:
      - { name: "171",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node02.pivotal.io."  }
      - { name: "172",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node03.pivotal.io."  }
      - { name: "173",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node04.pivotal.io."  }
      - { name: "174",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node05.pivotal.io."  }
      - { name: "175",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node06.pivotal.io."  }
      - { name: "176",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node07.pivotal.io."  }
      - { name: "177",  zone: 2.168.192.in-addr.arpa,  type: "--ptr-rec", value: "co9-node08.pivotal.io."  }
_selinux:
  policy:
    - { name: httpd_can_network_connect, toggle: on }
    - { name: httpd_gracefull_shutdown, toggle: on }
    - { name: httpd_can_network_relay, toggle: on }
  semange:
    - { name: port , type: http_port, proto: tcp, port: 6443 }
    - { name: port , type: http_port, proto: tcp, port: 22623 }
    - { name: port , type: http_port, proto: tcp, port: 1936 }


_firewall:
  service:
    - { name: dns,    state: enabled }
    - { name: http,   state: enabled }
    - { name: https,  state: enabled }
  port:
    - { state: enabled, port: 6443, proto: tcp, zone: public }
    - { state: enabled, port: 1936, proto: tcp, zone: public }
    - { state: enabled, port: 8080, proto: tcp, zone: public }
```

#### 2) Add DNS Zones and Records
```
$ make okd r=setup s=dns c=zone
$ make okd r=setup s=dns c=record
or
$ make okd r=setup s=dns c=all
```

#### 3) Remove DNS Zones and Records
```yaml
$ make okd r=remove s=dns c=record
$ make okd r=remove s=dns c=zone
or
$ make okd r=remove s=dns c=all
```

###  Setup NFS Server
$ vi ansible-hosts=co9
```
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

#### 2) Setup/Remove NFS Server and Client
```
$ make nfs r=setup s=server
$ make nfs r=setup s=client
or
$ make nfs r=remove s=client
$ make nfs r=remove s=server
```

#### 3) Create/Delete iSCSI Target/Initiator
```
$ make iscsi r=create s=target
$ make iscsi r=create s=initiator

or
$ make iscsi r=delete s=initiator
$ make iscsi r=delete s=target
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


### Prepare CentOS
1) yum repo
mirror -> valut
disable ceph repo

