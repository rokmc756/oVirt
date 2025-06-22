%global rolesdir %{_sysconfdir}/ansible/roles/gluster.features
%global buildnum 15

Name:      gluster-ansible-features
Version:   1.0.5
Release:   15%{?dist}
Summary:   Ansible roles for GlusterFS infrastructure management

URL:       https://github.com/gluster/gluster-ansible-features
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.
The features role enables user to configure CTDB, NFS-Ganesha, Geo-Replication,
Gluster HCI on GlusterFS clusters

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{rolesdir}
cp -dpr defaults handlers meta roles tasks tests README.md LICENSE vars examples README.md\
   %{buildroot}/%{rolesdir}

%files
%{rolesdir}

%license LICENSE

%changelog
* Mon Jun 27 2022 Gobinda Das <godas@redhat.com> 1.0.5-15
- Rebase: 1.0.5-15

* Thu May 19 2022 Gobinda Das <godas@redhat.com> 1.0.5-14
- Resolves: rhbz#2074765

* Sun Apr 24 2022 Gobinda Das <godas@redhat.com> 1.0.5-13
- Resolves: rhbz#2074765

* Tue Mar 29 2022 Gobinda Das <godas@redhat.com> 1.0.5-12
- Resolves: rhbz#2068510

* Thu Mar 18 2021 Gobinda Das <godas@redhat.com> 1.0.5-11
- Disabling lookup-optimize option, Resolves:rhbz#1939894

* Thu Oct 08 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-9
- Removing geo-rep feature on top of rebuild for RHEL8.3, Resolves: rhbz#1882715

* Fri Sep 25 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-8
- Rebuild for RHEL8.3, Resolves: rhbz#1882715

* Fri Sep 25 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-7
- Rebuild for RHEL8.3, Resolves: rhbz#1882715 

* Fri Mar 06 2020 Gobinda Das <godas@redhat.com> 1.0.5-6
- Doing builds for RHHI 1.8 in RHEL8

* Fri Mar 06 2020 Gobinda Das <godas@redhat.com> 1.0.5-5
- Doing builds for RHHI 1.8 in RHEL8

* Thu Nov 14 2019 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-4
- Building gluster-ansible-features for RHEL8

* Thu Jul 4 2019  Sachidananda Urs <sac@redhat.com> 1.0.5-3
- Remove the hosted-engine pre-req check  - rhbz#1674600
- Fix the SSL setup issues  - rhbz#1693979,1693982

* Thu Jun 20 2019 Sachidananda Urs <sac@redhat.com> 1.0.5-2
- Move rhhi pre-requisites to playbooks
- Remove the ipv6 FQDN check while enabling ipv6 in glusterd
- Resolves rhbz#1686359 rhbz#1688188

* Mon May 8 2019 Sachidananda Urs <sac@redhat.com> 1.0.5-1
- Add ssl setup feature for RHHI deployments rhbz#1693979

* Mon Mar 4 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-5
- Add slice setup for glusterd process rhbz#1683528

* Fri Mar 1 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-4
- Validate if the disks have logical sector size of 512B rhbz#1674608

* Wed Feb 20 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-3
- Add more validations rhbz#1674580 rhbz#1674617 rhbz#1674659

* Mon Feb 11 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-2
- Rebuilding since package was built with wrong tag

* Mon Feb 11 2019 Sachidananda Urs <sac@redhat.com> 1.0.4
- Add support to create distribute volume rhbz#1653575

* Tue Oct 23 2018 Sachidananda Urs <sac@redhat.com> 1.0.3
- Address security concerns regarding plaintext passwd rhbz#1641887

* Mon Oct 15 2018 Sachidananda Urs <sac@redhat.com> 1.0.2
- Removed implicit setting of granular-entry-heal rhbz#1635683

* Fri Sep 28 2018 Sachidananda Urs <sac@redhat.com> 1.0.1
- Removed Nagios dependency

* Fri Sep 21 2018 Sachidananda Urs <sac@redhat.com> 1.0
- Initial downstream release

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.2
- Disabled geo-replication for the initial release

* Tue Apr 24 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release.

