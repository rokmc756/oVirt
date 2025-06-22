%global collection_namespace ansible
%global collection_name utils

Name:           ansible-collection-%{collection_namespace}-%{collection_name}
Version:        2.3.0
Release:        2.2%{?dist}
Summary:        Ansible Network Collection for Common Code

License:        GPLv3+
URL:            %{ansible_collection_url}
Source:         https://github.com/ansible-collections/ansible.utils/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-core >= 2.12.0
BuildRequires:  ansible-macros

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n ansible.utils-%{version}
sed -i -e '/version:/s/null/%{version}/' galaxy.yml
find -type f ! -executable -type f -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
rm -fvr tests/integration tests/unit bindep.txt .pre-commit-config.yaml .yamllint changelogs/fragments/.keep
find -type f -name '.gitignore' -print -delete

%build
%ansible_collection_build

%install
%ansible_collection_install

%files
%license LICENSE
%doc README.md
%{ansible_collection_files}

%changelog
* Thu Mar 31 2022 Martin Necas <mnecas@redhat.com> - 2.2.0-3.2
- Rebuild for only ansible-core 2.12 or ansible >= 2.9

* Fri Mar 25 2022 Martin Necas <mnecas@redhat.com> - 2.3.0-2.1
- Build with ansible-core 2.12

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Sagi Shnaidman <sshnaidm@redhat.com> - 2.3.0-1
- Initial package

