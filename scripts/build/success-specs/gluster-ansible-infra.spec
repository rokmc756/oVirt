%global rolesdir %{_sysconfdir}/ansible/roles/gluster.infra
%global buildnum 22

Name:      gluster-ansible-infra
Version:   1.0.4
Release:   %{buildnum}%{?dist}
Summary:   Ansible roles for GlusterFS infrastructure management

URL:       https://github.com/gluster/gluster-ansible-infra
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.
The infra role enables user to configure firewall, setup backend disks, reset
backend disks.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{rolesdir}
cp -dpr defaults handlers meta roles tasks README.md LICENSE vars playbooks README.md \
   %{buildroot}/%{rolesdir}
# remove the molecule based tests
rm -rf %{buildroot}/%{rolesdir}/roles/firewall_config/molecule/
rm -rf %{buildroot}/%{rolesdir}/roles/backend_setup/molecule/

%files
%{rolesdir}

%license LICENSE

%changelog
* Mon Jun 27 2022 Gobinda Das <godas@redhat.com> 1.0.4-22
- Rebase: 1.0.4-22

* Fri Apr 29 2022 Gobinda Das <godas@redhat.com> 1.0.4-21
- Resolves: rhbz#2074765

* Tue Mar 29 2022 Gobinda Das <godas@redhat.com> 1.0.4-20
- Resolves: rhbz#2068510

* Mon Mar 01 2021 Gobinda Das <godas@redhat.com> 1.0.4-19
- Resolves: rhbz#1917661

* Mon Dec 15 2020 Gobinda Das <godas@redhat.com> 1.0.4-18
- Resolves: rhbz#1903905

* Thu Oct 1 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.4-14
- Fixes LVM Filter excluding issue , Resolves: rhbz#1883805

* Fri Sep 25 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.4-13
- Rebuilding ,top of changelog since RHEL8.3  buildroot changed

* Wed Aug 19 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.4-12
- Restarting only specific VDO's w.r.t to the inverntory, rather than all the VDO's

* Thu Jun 25 2020 Gobinda Das <godas@redhat.com> 1.0.4-11
- Resolves: rhbz#1848898

* Mon Jun 01 2020 Gobinda Das <godas@redhat.com> 1.0.4-10
- Fixed rhhi-1.8 issues

* Mon May 04 2020 Gobinda Das <godas@redhat.com> 1.0.4-9
- Fixed multipath issue

* Tue Apr 14 2020 Gobinda Das <godas@redhat.com> 1.0.4-8
- Bug fixes for RHHI 1.8 in RHEL8

* Fri Mar 27 2020 Gobinda Das <godas@redhat.com> 1.0.4-7
- Bug fixes for RHHI 1.8 in RHEL8

* Fri Mar 13 2020 Gobinda Das <godas@redhat.com> 1.0.4-6
- Doing builds for RHHI 1.8 in RHEL8

* Fri Mar 06 2020 Gobinda Das <godas@redhat.com> 1.0.4-5
- Doing builds for RHHI 1.8 in RHEL8

* Fri Nov 15 2019 Sheersha Jain <shjain@redhat.com> 1.0.4-4
- Build for RHEL8

* Thu Jun 20 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-3
- Update the vdo systemd file to load kvdo modules rhbz#1690606

* Thu May 9 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-2
- Start vdo services only if vdo variable is defined rhbz#1690606

* Wed May 8 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-1
- Add validations for storage disks and vdo fixes rhbz#1690606,1674600

* Fri Mar 1 2019 Sachidananda Urs <sac@redhat.com> 1.0.3-3
- Do not fail when RAID5 is used as disktype rhbz#1683355

* Wed Feb 20 2019 Sachidananda Urs <sac@redhat.com> 1.0.3-2
- Add validation to check if vdo service is running rhbz#1674580

* Fri Feb 8 2019 Sachidananda Urs <sac@redhat.com> 1.0.3
- Add fstab entries specific to VDO BZ#1667208

* Tue Nov 6 2018 Sachidananda Urs <sac@redhat.com> 1.0.2-2
- Do not include molecule based test code in package BZ#1642025

* Mon Oct 15 2018 Sachidananda Urs <sac@redhat.com> 1.0.2
- Add SeLinux labels to brick dirs, remove xfs runtime opts
- Resolves BZs: 1638940, 1635527, 1635938

* Fri Sep 28 2018 Sachidananda Urs <sac@redhat.com> 1.0.1
- Removed outdated playbooks, updated examples

* Fri Sep 21 2018 Sachidananda Urs <sac@redhat.com> 1.0
- Initial downstream build

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.2
- Backend setup enhancements

* Tue Apr 24 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release.
