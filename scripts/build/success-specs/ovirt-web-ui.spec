# Used for rpm-packaging of pre-bundled application with already resolved JS dependencies
%global product oVirt
%global source_basename ovirt-web-ui
%define debug_package %{nil}

# build condition `ovirt_use_nodejs_modules`
#   - on by default, requires a build with `--without ovirt_use_nodejs_modules` to turn off
#   - if on, the build uses `ovirt-engine-nodejs-modules`
#   - if off, the build uses standard `yarn` accessing all node_modules packages directly
%bcond_without ovirt_use_nodejs_modules

Name:           ovirt-web-ui
Version:        1.9.3
Release:        1%{?release_suffix}%{?checkout}%{?dist}
Summary:        VM Portal for %{product}
License:        ASL 2.0
URL:            https://github.com/oVirt/ovirt-web-ui
Source0:        %{source_basename}-%{version}.tar.gz

BuildArch: noarch

# requirements for automation/build.sh (to be included in the build container)
BuildRequires: git
BuildRequires: jq
BuildRequires: rpmlint
BuildRequires: rpm-build

# requirements for building the rpm from src.rpm
BuildRequires: autoconf
BuildRequires: automake
%if %{with ovirt_use_nodejs_modules}
# nodejs-modules embeds yarn and requires nodejs
BuildRequires: ovirt-engine-nodejs-modules >= 2.3.20
%else
BuildRequires: nodejs >= 14.15
BuildRequires: yarn >= 1.22
%endif

%description
This package provides the VM Portal for %{product}.

%prep
%setup -q -n"%{source_basename}-%{version}"

%build
%configure
export SKIP_AUTOGEN=1
%if %{with ovirt_use_nodejs_modules}
rpm -qa | grep ovirt-engine-nodejs
source /usr/share/ovirt-engine-nodejs-modules/setup-env.sh
%else
yarn install
%endif
make

%install
make install DESTDIR=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_datarootdir}/ovirt-web-ui
%{_datarootdir}/ovirt-engine/ovirt-web-ui.war
%{_sysconfdir}/ovirt-engine/engine.conf.d/50-ovirt-web-ui.conf
%{_sysconfdir}/ovirt-web-ui/branding/00-ovirt.brand

%changelog
* Mon Dec 19 2022 Sharon Gratch <sgratch@redhat.com> - 1.9.3-1
 - user/account settings - add support for the Virtual Machines layout (card/table view) property option
 - fix a bug of displaying the correct month in the 'Created' field of the snapshot details card and in the NotificationDrawer
   events timestamp
 - optimize the entity permission to permit mappings code to avoid the application from hanging out in case of a large
   amount of entities
 - enhance the support of TPM devices for Windows 11/2022 VMs by enforcing the Q35 Chipset with UEFI Firmware Type, if
   current firmware prevents enabling TPM
 - github actions: update actions versions to current supported ones
 - update dependencies of various packages:
   minimist from 1.2.5 to 1.2.7
   moment from 2.29.1 to 2.29.4
   minimatch from 3.0.4 to 3.1.2
   shelljs from 0.8.4 to 0.8.5
   react-redux from 7.2.6 to 7.2.9
   redux from ^4.1.2 to 4.2.0
   redux-saga from 1.1.3 to 1.2.1
   patternfly from 4.185.1 to 4.215.1
   react-charts from 6.55.16 to 6.94.1
   react-console from 4.53.20 to 4.92.1
   react-core from 4.202.16 to 4.241.1
   react-icons from 4.53.16 to 4.92.1
   react-table from 4.71.16 to 4.110.1

* Fri Sep 30 2022 Sharon Gratch <sgratch@redhat.com> - 1.9.2-1
 - VM Details - users can now create a new NIC with an empty vNIC profile, even if they don't have permissions for NIC profiles within the DC
 - VM details - force tooltips on the VM's react-chart charts to a constant width
 - VMs dashboard - support table view (in additions to cards view) on the Virtual Machines dashboard screen
 - add basic support for TPM devices for Windows 11/2022 VMs of cluster level >= 4.7
 - build issues: specify COPR chroot explicitly
 - build issues: remove broken Docker support
 - bump the Zanata version to 1.9
 - update dependencies: bump terser to 5.14.2, bump follow-redirects to 1.15.2
 - documentation updates - remove EL9 limitation note

* Fri Jul 22 2022 Sharon Gratch <sgratch@redhat.com> - 1.9.1-1
 - VM details snapshots card: add a frontend lock for the restored snapshot during the restore operation
 - VM details - force tooltips on the VM's utilization  charts to a constant width
 - fix a bug for opening a console on full screen mode after clicking the "full screen" button even when also set by account settings
 - fix a regression bug for redirecting to the welcome page after clicking on the logo
 - fix a bug for enabling to enter values into NumberInput on few dialogs
 - fix a bug of missing card IDs on the VM List screen
 - build issues:: add conditional build for offline/online builds
 - bump underscore from 1.6.0 to 1.13.1

* Fri Jun 17 2022 Sharon Gratch <sgratch@redhat.com> - 1.9.0-1
 - migrate all VM Portal components from PatternFly 3 to PatternFly 4. No use of PatternFly 3 anymore
 - migrate from Webpack 4 to Webpack 5 and use newest versions of Webpack plugins
 - user/account settings - display the notification settings tooltip as hint instead
 - VM details - allow a user to consume ISO images without granting a 'create disk' permission
 - VM details snapshots card - display notification after a successful snapshot restore
 - VM details snapshots card - fix a bug so that after deleting an existing snapshot, the 'create snapshot' button won't stay disabled
 - VM details snapshots card - fix a bug so that the snapshots locking mechanism is for the current VM only
 - add new NIC type "e1000e"
 - i18n: add support for Georgian language as a community translation
 - i18n: translations update, expire translations after zanata push
 - i18n: pull translations for Georgian language (ka-GE)
 - build: use hours, minutes and seconds in RPM snapshot name, version part
 - build: mark the Copr make_srpm git dir as safe (git 2.35.2 security fix)
 - github actions: add an offline build for el9
 - update dependencies of caniuse-lite for browserslist to version 1.0.30001346

* Wed Mar 30 2022 Sharon Gratch <sgratch@redhat.com> - 1.8.1-1
 - fix a bug for removing deleted pool entities from VMs dashboard after refresh for the last pool
 - add an option to trigger OST run with "/ost" via Github

* Tue Mar 15 2022 Sharon Gratch <sgratch@redhat.com> - 1.8.0-1
 - user/account settings - support auto connect for a VM
 - user/account settings -  support setting a full screen mode for the noVnc console
 - create VM Wizard - set the first disk as bootable by default
 - VM details - fix a bug for displaying numeric values in all utilization charts tooltips
 - VM details - fix a bug of displaying the correct values of VM's utilization disk charts in case of more than one reported file system
 - VM details - fix VM's utilization disk charts colors to be based on thresholds
 - VM details - remove 'restore snapshot' button from snapshot details dialog since it duplicates the functionality located on the card
 - fix a bug for removing deleted pool entities from VMs dashboard after refresh
 - fix a bug of VM Portal crashes at login time when nic.mac is fetched as null
 - fix a bug to enable assignment of user quota when creating a VM from a non-blank template
 - handle SSO deprecation by removing the default attempt to use SSO
 - code refactoring for reducer utils functions, convert reducers from ImmutableJS to ImmerJS
 - enable Copr builds
 - move the project to GitHub and update the relevant documentation and readme file
 - upgrade dependencies of various libraries
 - i18n: update Zanata configuration

* Mon Oct 11 2021 Sharon Gratch <sgratch@redhat.com> - 1.7.2-1
 - fix disks creation by correctly handling disk format and sparse attributes based on the target storage domain and
   also based on the template's disk format for server/high performance/desktop VM types
 - display error messages when VM's virtual CPU topology is set to invalid values
 - fix downloading Remote Desktop file for Firefox browser with the correct .rdp file extension instead of .vv extension
 - push master builds to ovirt-4.4 branch as well
 - update dependencies of immer, ua-parser-js and glob-parent packages

* Wed Aug 11 2021 Sharon Gratch <sgratch@redhat.com> - 1.7.1-1
 - refactor initial VM/Pool page loading and background refresh
 - refactor login managed base-data, user, group, and role fetches
 - refactor and improve disk permit/permissions calculations
 - refactor and remove unused sagas utils
 - refactor and optimize snapshot disks and nics fetching
 - refactor callExternalAction() to log the API method with Function.name
 - refactor console connection code and also support opening RDP console for headless Windows VMs
 - remove all of the OvirtApi toInternal functions
 - remove non used NewDiskDialog actions/reducers
 - upgrade eslint and all related dependencies to current versions and update configurations for react/jsx indent and eslint errors
 - add packages dependencies of flow-bin and postcss
 - add babel plugin fancy-console
 - avoid displaying manual refresh or setting actions in the header/navbar until the app is ready
 - fix a bug that when editing an exising disk via VM details, it always resulted with an inactive disk
 - fix fetchVmSnapshots() transform error
 - make the package.json scripts intl:* working again
 - fix a bug for enable loading Portuguese or Chinese languages when reading locales from the url
 - fix a bug for always setting a VM with the correct number of virtual CPUs
 - enhance user settings cancel dialog by informing the user that it is applied to all tabs/sections

* Thu Jun 24 2021 Sharon Gratch <sgratch@redhat.com> - 1.7.0-1
 - user/account settings - mark default options on Account Settings dialog
 - user/account settings - add option to reset global user settings to default/installation settings
 - user/account settings - seperate to sections on Account Settings
 - user/account settings - preserve the order and group options by sections in Confirmation dialog and error notification
 - user/account settings - add Console section options to Account Settings
 - user/account settings - add 'persist Locale' advanced settings option to Account Settings dialog
 - user/account settings - update the locales list on Account Settings dialog
 - retrieve current graphic consoles for re-enabling the option to select console types on dashboard (which was removed on ovirt-web-ui-1.6.8)
 - refactor handling ovirt engine config values in general and MaxNumOfVmCpus in specific
 - fix a bug of handling user group permissions which didn't work in ovirt-web-ui-1.6.9-1
 - convert all API Boolean attributes used by "toApi" functions to our new ApiBooleanType
 - fix uptime render in VM Details and Overview Card
 - switch formatDateFromNow() to use moment.humanize()
 - replace custom wrapper around PF3 with PF4 Switch component
 - upgrade the project's Webpack to version 4, babel to version 7
 - upgrade patternfly 4 packages and force lodash version
 - update/fix dependencies of handlebars, bootstrap-select and jquery
 - avoid using translated strings in "key" property
 - code cleanups
 - bump zanata.xml version to 1.7
 - translation update, 17-May-2021

* Tue Apr 27 2021 Sharon Gratch <sgratch@redhat.com> - 1.6.9-1
 - user/account settings - support user locale changes by hot reload
 - user/account settings - adding a confirmation dialog before saving user settings changes
 - user/account settings - create a "home" breadcrumbs root to resolve the confusion with "Virtual Machines" Breadcrumbs root
 - user/account settings - add support for setting the refresh interval
 - user/account settings - add labels by design for planned translation cycle
 - create VM Wizard - update create VM steps navigation and disk create checks
 - create VM Wizard- fix a bug so that disk type of new disks based on a 'server/HP' template should be based on the template's disk allocation policy
 - when launching in dev mode, support reading user name, password and domain from env variable
 - add check/validation if permission response is an array, to prevent crashing
 - fixed a bug of missing VmStatusIcon tooltip for a paused vm
 - use semver to verify API engine versions
 - allow users to select/deselect saving the memory while creating a snapshot for a running vm
 - fix a bug of which user permit calculations included invalid permissions
 - show VM's IP address if the vm is up and guest agent is running
 - update the dependency of lodash

* Thu Mar 11 2021 Sharon Gratch <sgratch@redhat.com> - 1.6.8-1
 - create VM Wizard - ass support for creating VMs based on a High Performance optimized for template
 - enhance graphic consoles data fetching time by fetching consoles info on demand instead of on refresh. This changes the way consoles are opened on dashboard
 - prevent crash when viewing a suspending/shutting down VM's details card
 - fixed few translated strings on VMs dashboard
 - enhance user/account settings by adding support for locale changes and displaying email info
 - a fix for reading new format of config val MaxNumOfVmCpus

* Wed Feb 10 2021 Sharon Gratch <sgratch@redhat.com> - 1.6.7-1
 - create VM Wizard - display a validation text message next to the VM Name and Cloud-init/Sysprep's host name fields on basic settings step
 - create VM Wizard - add a validation to disk name field on the storage step
 - create VM Wizard - force template disk's storage domain selection and change default disk type for Template and ISO provisioned VMs
 - create VM Wizard - validate the disk's storage domain for the current user based on user permissions
 - create VM Wizard - fix the create VM from template's bootable disk flag option
 - create VM Wizard - select The correct "Other OS" option in OS field of basic settings step, based on cluster's cpu architecture
 - create VM Wizard - fix the basic settings step behaviour when only one cluster exists and no hosts are assigned to the cluster
 - create VM Wizard - remove disk size inconsistent tooltip in storage step
 - create VM Wizard - fix eslint import errors
 - fix an exception occurs when a VM is taken from a pool while a refresh is done with a filter
 - fix an error occurs after changing a cluster for an existed VM via the details card component
 - update dependencies of immer and datatables.net
 - remove Fedora 30 from STDCI since it's EOL

* Wed Dec 9 2020 Sharon Gratch <sgratch@redhat.com> - 1.6.6-1
 - create VM Wizard - handle buttons "Save", "Cancel" position to be fixed for avoiding movements when clicking on them repeatedly
 - create VM Wizard - auto focus on the 'VM Name' field on 'Basic Settings' step
 - create VM Wizard - display proper sysprep timezone default value
 - create VM Wizard - automatically set fields values when possible on 'Basic Settings' step
 - for both create VM Wizard and VM details view card - filter out the clusters with no architecture and cpu-type attached
 - change the VM's filters to be case insensitive
 - support user settings first phase - setting SSH key and impersistent blocking toast notifications
 - fix the virt-viewer console file for SPICE to be downloaded as a console.vv file name instead of a temp long file name and without the .vv extension
 - tooltip refactoring - use one type of tooltip for consistency in VM portal
 - change all delete icons to red in the VM details view for helping to distinguish between edit and delete icons easily
 - prevent duplicate refresh on page change
 - display only Pool VMs that the user is supposed to see after manual refresh
 - add linting rules for React hooks
 - add 'yarn intl:check-use' for automated translations script
 - update parsing of VM statistics (fetched with VM details)

* Wed Oct 21 2020 Sharon Gratch <sgratch@redhat.com> - 1.6.5-1
 - create VM Wizard - support tab through fields in Storage and Networking steps
 - create VM Wizard - VM time zone format is now compatible with VM OS and also displayed on the review step
 - create VM Wizard - prevent the unsaved data confirmation dialog from being displayed in last step after VM creation
 - create VM Wizard - add Timezone field for sysprep options
 - create VM Wizard - sort alphabetically the list of Disks and NICs on the review step
 - create VM Wizard - fix setting the disk size by using arrows to work properly
 - create VM Wizard - Validate add/edit NIC name field on row save action
 - create VM Wizard - support creation of a new NIC with an empty (n/a) profile
 - create VM Wizard - support advanced CPU topology setting on "Basic Settings" step
 - create VM Wizard - add indication of which field is invalid/missing on "Basic Settings" step for enablng the next step
 - the CPU Utilization chart details are fixed to be displayed properly, based on the number of vCPUs
 - set enable-usb-autoshare in console.vv file according to SpiceUsbAutoShare engine config value
 - refactor DetailsCard component to use explicit config values
 - increase spacing between Boot Order and VCPU Topology sections in VM Details card
 - use pf3 ExpandCollapse react component in the VM Details card
 - rephrase the "Threads per Core" tooltip text
 - update dependencies of handlebars and bootstrap-select
 - update minimum ovirt version to 4.4
 - translations update 2020-Sep-2
 - translate the About modal missing strings
 - refactor i18n normalize script by adding an explicit key sorting function
 - translate the Duration formatting for VM uptime and refactor intl scripts
 - refactor intl initialization and remove react-intl package
 - update Zanata tools to use the maven plugin

* Wed Aug 19 2020 Sharon Gratch <sgratch@redhat.com> - 1.6.4-1
 - create VM Wizard - prevent the dialog from being closed without a confirmation
 - create VM Wizard - add a tooltip message to Disk size field on edit mode
 - create VM Wizard - allow valid only calls to onUpdate functions
 - create VM Wizard - support setting disks as bootable
 - create VM Wizard - adjust table rows spacers for consistency between edit and create modes
 - support VM Card List pagination and infinite scrolling
 - set usb-filter and enable-usb-autoshare entries in console.vv properly
 - automatically open console.vv with virt-viewer when clicking on VM console, if it's set to default application on Firefox
 - fix disk creation for an existing VM to support all allocation policies and also set default to "Thin Provision"
 - remove Components that are no longer used
 - on logout, set the page to NO_REFRESH and stop the scheduler
 - add initial favicon to index.hbs, branding and config updates as needed
 - update dependencies of jquery and lodash
 - translations update 2020-July-02

* Mon Jul 6 2020 Sharon Gratch <sgratch@redhat.com> - 1.6.3-1
 - create VM Wizard - fixed a bug so that nics and disks data resetting happens only when it is supposed to
 - create VM Wizard - enable resetting of basic settings to baseline defaults when changing the provision source
 - create VM Wizard - add a tooltip to the "T" badge for Templates disks and nics
 - create VM Wizard - the Storage Domain menu field width, displayed on a new disk row, is fixed to be aligned
 - the VM's filter is fixed to return only Pools entities that answer the query result
 - enable the Shutdown button for a suspended VM
 - fix a bug of displaying an error in UPDATE_VMS reducer in scheduled refresh done after a manual refresh
 - fix a bug for enable maximizing of the Notifications drawer
 - enable setting disk's of exisiting VMs as "Bootable"
 - change VM/Pool fetch page size and optimize refresh scheduling for improving the loading performance
 - increase parallel calls during login data fetch for improving the login loading performance
 - update Dockerfile with yarn network timeout mitigations
 - refactor Makefile to prevent unexpected symlinks
 - translations update

* Tue May 12 2020 Sharon Gratch <sgratch@redhat.com> - 1.6.2-1
 - fix a bug in which VM Portal fails to initialize if the environment contains an Export storage domain
 - fix a bug in which opening a VM console of type SPICE or VNC is always failing
 - fix VMs filter results to include all VMs with entered string exists anywhere inside the Vm name and not just the prefix
 - change the snapshots rpm file names to contain the latest commit hash
 - apply ovirt 4.4 branding changes to the error page as well
 - yarn dependencies update
 - translations update

* Mon Apr 6 2020 Sharon Gratch <sgratch@redhat.com> - 1.6.1-1
 - fixed saving NIC with empty VNIC Profile
 - make the vm poratl more responsive for browser resizing, set minimum card widths and fixed alignments.
 - add kebob actions menu and changed Shutdown button type to default in VM's dashboard
 - disable auto log out when the "UserSessionTimeOut" config value is set to value of -1
 - tooltip Code Refactoring, including using one type of style for tooltips on CardEditButton
 - added a tooltip for the 'Disk Edit' Dialog.
 - replaced Patternfly 3 charts with Patternfly 4
 - fixed wrong html element ids for the VM and Pool
 - changed 'automation/build.repos' location for matching the STDCI V2 used by ovirt-engine-nodejs-modules
 - allowed use of alternate branding by the DEV server
 - Fixed hover texts in masthead
 - updated build to use yarn from ovirt-engine-nodejs-modules
 - hid host info from non-admin users
 - fixed Windows VM creation timezone bug such that if template/vm time zone format isn't compatible with VM OS, time zone is changed to default
 - updated autogen/automake configurations and yarn integration
 - removed 'ovirt-4.2' from STDCI release branch config
 - updated title and warning messages for 'Remove VM' confirmation modal
 - pool and pool vms redesign
 - added toast notifications for Start/Shutdown VM requests.
 - added documentation link and updated report issues url for the 'About' dialog
 - hanlded 404 errors
 - Added better handling for token expiration by redesign of the log out component and support Patternfly 4
 - refactored the user messages
 - fixed typo in pool allocated VMs tooltip message
 - changed the VM card list page so that if a VM is running then default action item is set openning the VM console
 - redesign create vm - using a new create VM Wizard.
 - Added a "full screen" mode for the webvnc console.
 - fixed a bug that the disk create modal didn't show the storage domains
 - added an external service button to the VM's action panel
 - updated branding and navbar masthead for allowing branding to continue to use the same CSS class names
 - fixed the navbar icons layout
 - fetched roles and permit at login and do entity permission to permit mapping on frontend
 - changed VM details Disks card disk sort order to sort by disk name only
 - replaced local VncConsole by patternfly VncConsole
 - fixed Pool handling and refactor VM loading bugs
 - added scrollbar to the notification menu
 - disabled the Console action on a headless VM
 - updated DEVELOPERS.md
 - updated zanata server and version
 - created script for auto checking of the translation file
 - updated translations for ovirt 4.4

* Tue Aug 27 2019 Michal Skrivanek <michal.skrivanek@redhat.com> - 1.6.0-1
 - updated translations
 - limit CD/ISO list by data center
 - improve responsiveness on small screens (mobile)
 - updated patternfly3 and js dependencies
 - added Sysprep to Details card for Windows VM

* Mon Jul 1 2019 Sharon Gratch <sgratch@redhat.com> - 1.5.3-1
 - Added check for inactivity during session and logout after expiration
 - Added NoVNC console support
 - Resolve login data load concurrency issues (allows ISOs to load at login)
 - updated translations
 - Added template filtering for VM create dialog
 - Added validation for Disk name
 - Allow adding more CPUs than the max sockets count

* Wed Mar 27 2019 Greg Sheremeta <gshereme@redhat.com> - 1.5.2-1
 - Remove edibility of a VM's template
 - Remove wrap for hostname and FQDN, add ellipsis with tooltip

* Mon Feb 18 2019 Greg Sheremeta <gshereme@redhat.com> - 1.5.1-1
 - Fixed several issues
 - updated translations

* Wed Jan 9 2019 Greg Sheremeta <gshereme@redhat.com> - 1.5.0-1
 - Redesign of VM Edit / Dashboard view complete
 - Fixed several issues

* Tue Sep 4 2018 Greg Sheremeta <gshereme@redhat.com> - 1.4.3-1
  Fixed issues:
- ux-redesign: make old Normal View the default when clicking a VM [#751](https://github.com/oVirt/ovirt-web-ui/issues/751)

* Fri Aug 17 2018 Greg Sheremeta <gshereme@redhat.com> - 1.4.2-1
  Fixed issues:
- Main > InfiniteScroll is broken [#708](https://github.com/oVirt/ovirt-web-ui/issues/708)
- dev server doesn't work without redux dev tools installed [#688](https://github.com/oVirt/ovirt-web-ui/issues/688)
- RDP button sends 'console.rdp' to the user at render time instead of onClick event time [#686](https://github.com/oVirt/ovirt-web-ui/issues/686)
- Redesign notifications [#647](https://github.com/oVirt/ovirt-web-ui/issues/647)
- cloud-init switch has no function [#642](https://github.com/oVirt/ovirt-web-ui/issues/642)
- Redesign main page [#641](https://github.com/oVirt/ovirt-web-ui/issues/641)
- ScrollPositionHistory not working [#416](https://github.com/oVirt/ovirt-web-ui/issues/416)
- Sort operating systems [#409](https://github.com/oVirt/ovirt-web-ui/issues/409)
- mobile: VMs in grid view are not all visible on mobile device [#367](https://github.com/oVirt/ovirt-web-ui/issues/367)

* Thu Aug 2 2018 Greg Sheremeta <gshereme@redhat.com> - 1.4.1-1
  Fixed issues:
  - 'failed Not found' error with Connect automatically console option bug major [#509](https://github.com/oVirt/ovirt-web-ui/issues/509)
  - reattach VmDialog's sagas to the root saga so VM edits get saved [#683](https://github.com/oVirt/ovirt-web-ui/pull/683)
  - VM edits don't save bug [#684](https://github.com/oVirt/ovirt-web-ui/issues/684)

* Mon Jul 16 2018 Marek Libra <mlibra@redhat.com> - 1.4.0-3
Fixed issues:
- web-ui about windows7 display？ [#644](https://github.com/oVirt/ovirt-web-ui/issues/644)
- Refactor About and Options dialogs [#617](https://github.com/oVirt/ovirt-web-ui/issues/617)
- No confirmation after `Esc` [#613](https://github.com/oVirt/ovirt-web-ui/issues/613)
- filter os entries by cluster [#608](https://github.com/oVirt/ovirt-web-ui/issues/608)
- fix os sorting [#607](https://github.com/oVirt/ovirt-web-ui/issues/607)
- If yarn.lock gets fully regenerated, flow will break with a bad configuration [#602](https://github.com/oVirt/ovirt-web-ui/issues/602)
- Messages option text "No messages" not proper. [#594](https://github.com/oVirt/ovirt-web-ui/issues/594)
- VM Portal does not auto refresh [#593](https://github.com/oVirt/ovirt-web-ui/issues/593)
- Edit VM 'Close' without saving fails [#592](https://github.com/oVirt/ovirt-web-ui/issues/592)
- Safari browser [#590](https://github.com/oVirt/ovirt-web-ui/issues/590)
- After reload Edit VM page, page become empty [#574](https://github.com/oVirt/ovirt-web-ui/issues/574)
- VM Snapshot management [#573](https://github.com/oVirt/ovirt-web-ui/issues/573)
- first click on vNIC profile select box item doesn't change the selected value [#571](https://github.com/oVirt/ovirt-web-ui/issues/571)
- NIC hot unplug not work [#569](https://github.com/oVirt/ovirt-web-ui/issues/569)
- Pending changes tooltip overflow [#568](https://github.com/oVirt/ovirt-web-ui/issues/568)
- After click on 'Set default Icon' every additional data of VM is disappearing  [#567](https://github.com/oVirt/ovirt-web-ui/issues/567)
- no way to boot from a network if the VM has no disk [#565](https://github.com/oVirt/ovirt-web-ui/issues/565)
- Redirect to main page after F5 on VM Detail page [#563](https://github.com/oVirt/ovirt-web-ui/issues/563)
- InfiniteScroller console warning about unique key [#562](https://github.com/oVirt/ovirt-web-ui/issues/562)
- Upgrade npm dependencies [#558](https://github.com/oVirt/ovirt-web-ui/issues/558)
- disable Boot menu switch in edit dialog when VM is running [#549](https://github.com/oVirt/ovirt-web-ui/issues/549)
- add option to force shutdown a VM [#522](https://github.com/oVirt/ovirt-web-ui/issues/522)
- Suspend button not disabled for pooled VMs [#462](https://github.com/oVirt/ovirt-web-ui/issues/462)
- 16 users limit in vm pool [#456](https://github.com/oVirt/ovirt-web-ui/issues/456)
- Toobar overlaps tooltip [#452](https://github.com/oVirt/ovirt-web-ui/issues/452)
- Top line of tooltip not visible [#434](https://github.com/oVirt/ovirt-web-ui/issues/434)
- Popup descriptions hidden in edit page [#422](https://github.com/oVirt/ovirt-web-ui/issues/422)
- no cake as VM icon [#415](https://github.com/oVirt/ovirt-web-ui/issues/415)
- Error message partially overlapped [#395](https://github.com/oVirt/ovirt-web-ui/issues/395)
- New VM name validation & requirements [#382](https://github.com/oVirt/ovirt-web-ui/issues/382)
- Move icon editing from VM detail page to VM edit page [#356](https://github.com/oVirt/ovirt-web-ui/issues/356)
- Remove small icon from edit page [#355](https://github.com/oVirt/ovirt-web-ui/issues/355)
- mobile: status and truncated description in VM grid is not clickable for mobile device [#344](https://github.com/oVirt/ovirt-web-ui/issues/344)
- and other changes not tracked via issues (see github for full list of merged PRs)

* Mon Jul 16 2018 Marek Libra <mlibra@redhat.com> - 1.4.0-2

* Mon Jun 25 2018 Marek Libra <mlibra@redhat.com> - 1.4.0
- A lot of UI fixes

* Wed Apr 25 2018 Marek Libra <mlibra@redhat.com> - 1.3.9
- fix: cluster can be in no datacenter - https://github.com/oVirt/ovirt-web-ui/pull/577
- fix: storage domain can be in multiple datacenters https://github.com/oVirt/ovirt-web-ui/pull/578

* Thu Apr 12 2018 Marek Libra <mlibra@redhat.com> - 1.3.8-2
- Adjust min memory while editing memory - https://github.com/oVirt/ovirt-web-ui/pull/538
- Fixed the VmDisks sort - https://github.com/oVirt/ovirt-web-ui/pull/547
- All HTTP methods use proper 'Filter' header - https://github.com/oVirt/ovirt-web-ui/pull/550
- Fix: Avoid VM IDs in VMS navigation item list - https://github.com/oVirt/ovirt-web-ui/pull/540
- Fixed disk sorting - https://github.com/oVirt/ovirt-web-ui/pull/547
- Fixed error by deleting disk - https://github.com/oVirt/ovirt-web-ui/pull/551
- Add warning for Boot menu - https://github.com/oVirt/ovirt-web-ui/pull/560
- Fix Cloud-Init switch - https://github.com/oVirt/ovirt-web-ui/pull/559
- Fixed align of Delete buttons for Disks - https://github.com/oVirt/ovirt-web-ui/pull/553
- additional smaller UI enhancements

* Mon Mar 26 2018 Marek Libra <mlibra@redhat.com> - 1.3.7-2
- VM networks editation - https://github.com/oVirt/ovirt-web-ui/pull/517
- VM disks editation - https://github.com/oVirt/ovirt-web-ui/pull/523
- ssh dialog UI fix - https://github.com/oVirt/ovirt-web-ui/pull/519
- cloud-init VM name fix - https://github.com/oVirt/ovirt-web-ui/pull/528
- minor UI fixes
- Translations updated

* Wed Feb 28 2018 Marek Libra <mlibra@redhat.com> - 1.3.6
- VM detail landing after refresh fixed (https://github.com/oVirt/ovirt-web-ui/pull/497)
- Dialog for SSH keys fixed (https://github.com/oVirt/ovirt-web-ui/pull/464)
- Basic cloud-init support (https://github.com/oVirt/ovirt-web-ui/pull/498)
- CD removed from New VM dialog (https://github.com/oVirt/ovirt-web-ui/pull/496)
- Boot menu configuration added (https://github.com/oVirt/ovirt-web-ui/pull/493)
- Console re-connect fixed for warning message (https://github.com/oVirt/ovirt-web-ui/pull/483)
- Tooltips fixed (https://github.com/oVirt/ovirt-web-ui/pull/469)
- Close button navigates to previous page (https://github.com/oVirt/ovirt-web-ui/pull/482)
- Broken grid fixed for pools (https://github.com/oVirt/ovirt-web-ui/pull/473)
- Flow type check fix (https://github.com/oVirt/ovirt-web-ui/pull/470)
- Fix label in CTRL+ALT+DEL option (https://github.com/oVirt/ovirt-web-ui/pull/484)
- Change logo link to home page URL (https://github.com/oVirt/ovirt-web-ui/pull/474)
- Translations updated

* Wed Jan 24 2018 Marek Libra <mlibra@redhat.com> - 1.3.5
- Translations updated
- Fix for page reload - https://github.com/oVirt/ovirt-web-ui/pull/465
- Fix for pool removal - https://github.com/oVirt/ovirt-web-ui/issues/446
- Fix for infinite scroller - https://github.com/oVirt/ovirt-web-ui/pull/459


* Thu Nov 30 2017 Marek Libra <mlibra@redhat.com> - 1.3.4
- Fix for headless VMs - https://github.com/oVirt/ovirt-web-ui/pull/444
- Updated translations

* Tue Nov 28 2017 Marek Libra <mlibra@redhat.com> - 1.3.3
- Minor UI fixes and improvements
- Fix frozen "Loading" msg - https://github.com/oVirt/ovirt-web-ui/pull/430
- Fix of sorting of VMs in left vertical panel - https://github.com/oVirt/ovirt-web-ui/pull/428
- Fix in locale recognition - https://github.com/oVirt/ovirt-web-ui/pull/438
- Use of translated messages from API - https://github.com/oVirt/ovirt-web-ui/pull/131

* Tue Nov 14 2017 Marek Libra <mlibra@redhat.com> - 1.3.2
- fix of scrollbar on Webkit browsers

* Mon Nov 13 2017 Marek Libra <mlibra@redhat.com> - 1.3.1
- verbose warning in console - https://github.com/oVirt/ovirt-web-ui/issues/376
- scrolling of popups - https://github.com/oVirt/ovirt-web-ui/issues/394
- no autologout - https://github.com/oVirt/ovirt-web-ui/issues/308
- Make use of "AlwaysFilterResultsForWebUi" engine configuration parameter - https://github.com/oVirt/ovirt-web-ui/issues/317
- fix empty name in Create VM dialog - https://github.com/oVirt/ovirt-web-ui/issues/365
- select boxes are left-alligned - https://github.com/oVirt/ovirt-web-ui/issues/370
- allow empty memory/cpu - https://github.com/oVirt/ovirt-web-ui/issues/369
- docker image fixed - https://github.com/oVirt/ovirt-web-ui/issues/304
- HTML IDs added for automated testing
- Minor UI fixes
- translations updated

* Mon Oct 30 2017 Marek Libra <mlibra@redhat.com> - 1.3.0
- BnB (Brand new Branding) - alligned witth ovirt-engine
- Smartcard Enabled option
- SSH public key
- Gust OS names as labels
- i18n improvements, first tranlsations
- multiple fixes and minor UI enhancements


* Wed Aug 16 2017 Marek Libra <mlibra@redhat.com> - 1.2.1
- noarch rpm
- minor fixes, runtime dependencies generally updated
- usb-filter in .vv file
- basics for internationalization, but translation missing

* Wed Aug 2 2017 Marek Libra <mlibra@redhat.com> - 1.2.0
- branding
- infinite scroller for VMS list
- Change CD function
- "Runs on Host" - hyperlink to the host running particular VM
- "Loading ..." indicator of background activity
- "Pending Changes" tag rendered when NEXT_RUN configuration exists
- VM Type
- error messages improved
- fixed setting of VM icon
- multiple additional functional & UI fixes

* Tue Jun 20 2017 Marek Libra <mlibra@redhat.com> - 1.1.0
- Navigation via list of VMs to see details simplified
- Component for VM's Disks redesigned
- Context-based help
- Support for RDP graphics consoles
- ESC key used as back-button
- multiple UI fixes and improvements
- Configuration of graphics console added

* Fri Jun 2 2017 Marek Libra <mlibra@redhat.com> - 1.0.0
- "Door effect" removed, replaced by standard patternfly design
- User Messages are not closed automatically
- Check "Console in use" added
* Mon May 15 2017 Marek Libra <mlibra@redhat.com> - 0.2.2
- Minor fixes for pools
* Mon May 15 2017 Marek Libra <mlibra@redhat.com> - 0.2.1
- React and Redux updated to latest version
* Fri May 12 2017 Marek Libra <mlibra@redhat.com> - 0.2.0
- Add/Edit VM Dialog
- Autoconnect and Console options
- VM Pools
- the Remove VM action
- confirmation dialog improved
- functionality and UI fixes
* Wed Apr 19 2017 Marek Libra <mlibra@redhat.com> - 0.1.4
- Confirmation component
- About dialog
- UI fixes
- docker builds
- stability fixes
* Wed Apr 12 2017 Marek Libra <mlibra@redhat.com> - 0.1.3
- UI fixes
- docker builds
- oVirt API version check
- About dialog
* Mon Feb 20 2017 Marek Libra <mlibra@redhat.com> - 0.1.2
- Minor UI fixes, npm replaced by yarn
* Fri Dec 16 2016 Marek Libra <mlibra@redhat.com> - 0.1.1
- Minor UI fixes, authorizedRedirect.jsp
* Mon Nov 14 2016 Marek Libra <mlibra@redhat.com> - 0.1.0
- First version, Technical Preview
