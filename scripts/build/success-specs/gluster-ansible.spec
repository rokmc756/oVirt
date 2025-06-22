%global rolesdir %{_sysconfdir}/ansible/roles/gluster.ansible
%global docdir %{_datadir}/doc/gluster.ansible
%global buildnum 28

Name:      gluster-ansible-roles
Version:   1.0.5
Release:   28%{?dist}
Summary:   Ansible roles for GlusterFS deployment and management

URL:       https://github.com/gluster/gluster-ansible
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12
Requires:  gluster-ansible-infra >= 1.0.4
Requires:  gluster-ansible-features >= 1.0.5
Requires:  gluster-ansible-cluster >= 1.0
Requires:  gluster-ansible-repositories >= 1.0.1
Requires:  gluster-ansible-maintenance >= 1.0.1

Obsoletes: ansible < 2.10.0

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{rolesdir}
cp -a playbooks/ %{buildroot}/%{rolesdir}

mkdir -p %{buildroot}/%{docdir}
install -p -m 644 README.md LICENSE %{buildroot}/%{docdir}


%files
%{rolesdir}
%doc %{docdir}

%license LICENSE

%changelog
* Fri May 13 2022 Gobinda Das <godas@redhat.com> 1.0.5-28
- Resolves: rhbz#2074765

* Sun Apr 24 2022 Gobinda Das <godas@redhat.com> 1.0.5-27
- Resolves: rhbz#2074765

* Tue Mar 29 2022 Gobinda Das <godas@redhat.com> 1.0.5-26
- Resolves: rhbz#2068510

* Fri Jul 30 2021 Gobinda Das <godas@redhat.com> 1.0.5-25
- Resolves: rhbz#1986367

* Mon Mar 29 2021 Gobinda Das <godas@redhat.com> 1.0.5-24
- Resolves: rhbz#1944064

* Mon Dec 15 2020 Gobinda Das <godas@redhat.com> 1.0.5-23
- Resolves: rhbz#1903000, rhbz#1901364

* Mon Oct 05 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-20
- Dont allow mix of 4K and 512B disk block disks per volume across hosts Resolves: rhbz#1857667

* Fri Sep 25 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-19
- Rebuilding ,top of changelog since RHEL8.3  buildroot changed Resolves: rhbz#1871039

* Thu Aug 27 2020 Prajith Kesava Prasad <pkesavap@redhat.com> 1.0.5-18
- Resolves: rhbz#1871039

* Fri Jul 10 2020 Gobinda Das <godas@redhat.com> 1.0.5-17
- Resolves: rhbz#1855352

* Mon Jul 06 2020 Gobinda Das <godas@redhat.com> 1.0.5-16
- Resolves: rhbz#1848898

* Sun Jul 05 2020 Gobinda Das <godas@redhat.com> 1.0.5-15
- Resolves: rhbz#1848898

* Tue Jun 30 2020 Gobinda Das <godas@redhat.com> 1.0.5-14
- Resolves: rhbz#1848898

* Thu Jun 25 2020 Gobinda Das <godas@redhat.com> 1.0.5-13
- Resolves: rhbz#1848898

* Wed Jun 24 2020 Gobinda Das <godas@redhat.com> 1.0.5-13.1
- Resolves: rhbz#1848898

* Tue Jun 02 2020 Gobinda Das <godas@redhat.com> 1.0.5-12
- Bug fixes for RHHI 1.8

* Mon Jun 01 2020 Gobinda Das <godas@redhat.com> 1.0.5-11
- Bug fixes for RHHI 1.8

* Tue Apr 14 2020 Gobinda Das <godas@redhat.com> 1.0.5-10
- Bug fixes for RHHI 1.8 in RHEL8

* Tue Apr 14 2020 Gobinda Das <godas@redhat.com> 1.0.5-8
- Bug fixes for RHHI 1.8 in RHEL8

* Fri Mar 13 2020 Gobinda Das <godas@redhat.com> 1.0.5-7
- Doing builds for RHHI 1.8 in RHEL8

* Fri Mar 06 2020 Gobinda Das <godas@redhat.com> 1.0.5-6
- Doing builds for RHHI 1.8 in RHEL8

* Wed Nov 13 2019 Sachidananda Urs <sac@redhat.com> 1.0.5-5
- Doing builds for RHEL8

* Fri Jun 28 2019 Sachidananda Urs <sac@redhat.com> 1.0.5-4
- Fix a typo s/152/512/

* Wed Jun 26 2019 Sachidananda Urs <sac@redhat.com> 1.0.5-3
- Fix the 512B check in cases of mix of vdo and non-vdo rhbz#1713816

* Thu Jun 20 2019 Sachidananda Urs <sac@redhat.com> 1.0.50-2
- Move rhhi pre-requisites to playbooks
- rhbz#1686359 rhbz#1712798 rhbz#1713816 rhbz#1713816

* Wed May 8 2019 Sachidananda Urs <sac@redhat.com> 1.0.5-1
- Update documentation and hyperlinks, fix peer issue. rhbz#1692786

* Fri Mar 1 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-4
- Move the playbooks to roles directory from doc/ rhbz#1683625

* Fri Feb 22 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-3
- Rebuilding with new release number to new branch. rhbz#1674725

* Fri Feb 22 2019 Sachidananda Urs <sac@redhat.com> 1.0.4-2
- Add example playbook to clean up the setup. rhbz#1674725

* Tue Oct 23 2018 Sachidananda Urs <sac@redhat.com> 1.0.4
- Fix security concerns regarding plaintext passwords rhbz#1641887

* Mon Oct 15 2018 Sachidananda Urs <sac@redhat.com> 1.0.3
- Playbook improvements, resolves bz#1636044

* Fri Sep 28 2018 Sachidananda Urs <sac@redhat.com> 1.0.2-2
- Add playbook directory to /usr/share/doc

* Fri Sep 28 2018 Sachidananda Urs <sac@redhat.com> 1.0.2-1
- Removed Nagios dependency, added more examples

* Mon Sep 24 2018 Sachidananda Urs <sac@redhat.com> 1.0.1-1
- Add example playbooks for rhhi end-to-end deployment

* Tue Sep 18 2018 Sachidananda Urs <sac@redhat.com> 1.0-1
- Initial build, supports basic installations
