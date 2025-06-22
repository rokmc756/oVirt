
Name:           ansible-macros
Summary:        Ansible collections RPM Macros
Version:        2021.1.2
Release:        2.2%{?dist}

License:        GPLv3+
Group:          Development/Libraries/Python
URL:            http://ansible.com

Source1:        ansible.attr
Source2:        ansible-generator
Source3:        macros.ansible

BuildArch:      noarch

Supplements:    ansible-core

%description
This package provides RPM macros for packaging Ansible collections.

%prep

%build

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} %{SOURCE1}
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} %{SOURCE2}
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE3}

%files
%{_fileattrsdir}/ansible.attr
%{_rpmmacrodir}/macros.ansible
%{_rpmconfigdir}/ansible-generator

%changelog
* Thu Sep 23 2021 Alfredo Moralejo <amoralej> - 2021.1.2-2
- Suplements ansible-core instead of ansible.
- Automatic requires in CentOS Stream 9 is ansible-core instead of ansible-base

* Thu Feb 04 2021 Joel Capitao <jcapitao@redhat.com>
- Initial package
