#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : swift
Version  : 2.18.0
Release  : 22
URL      : http://tarballs.openstack.org/swift/swift-2.18.0.tar.gz
Source0  : http://tarballs.openstack.org/swift/swift-2.18.0.tar.gz
Source1  : swift-account-auditor.service
Source2  : swift-account-reaper.service
Source3  : swift-account-replicator.service
Source4  : swift-account.service
Source5  : swift-container-auditor.service
Source6  : swift-container-replicator.service
Source7  : swift-container-updater.service
Source8  : swift-container.service
Source9  : swift-object-auditor.service
Source10  : swift-object-replicator.service
Source11  : swift-object-updater.service
Source12  : swift-object.service
Source13  : swift-proxy.service
Source14  : swift.tmpfiles
Source99 : http://tarballs.openstack.org/swift/swift-2.18.0.tar.gz.asc
Summary  : OpenStack Object Storage
Group    : Development/Tools
License  : Apache-2.0
Requires: swift-bin
Requires: swift-python3
Requires: swift-config
Requires: swift-data
Requires: swift-license
Requires: swift-python
Requires: PasteDeploy
Requires: Sphinx
Requires: bandit
Requires: boto
Requires: castellan
Requires: coverage
Requires: cryptography
Requires: dnspython
Requires: eventlet
Requires: fixtures
Requires: greenlet
Requires: hacking
Requires: keystonemiddleware
Requires: lxml
Requires: netifaces
Requires: nose
Requires: nosexcover
Requires: openstackdocstheme
Requires: os-api-ref
Requires: os-testr
Requires: oslo.config
Requires: pyeclib
Requires: python-keystoneclient
Requires: python-mock
Requires: python-openstackclient
Requires: python-swiftclient
Requires: reno
Requires: requests
Requires: requests-mock
Requires: six
Requires: xattr
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the swift package.
Group: Binaries
Requires: swift-data
Requires: swift-config
Requires: swift-license

%description bin
bin components for the swift package.


%package config
Summary: config components for the swift package.
Group: Default

%description config
config components for the swift package.


%package data
Summary: data components for the swift package.
Group: Data

%description data
data components for the swift package.


%package license
Summary: license components for the swift package.
Group: Default

%description license
license components for the swift package.


%package python
Summary: python components for the swift package.
Group: Default
Requires: swift-python3

%description python
python components for the swift package.


%package python3
Summary: python3 components for the swift package.
Group: Default
Requires: python3-core

%description python3
python3 components for the swift package.


%prep
%setup -q -n swift-2.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533876733
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/swift
cp LICENSE %{buildroot}/usr/share/doc/swift/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/swift-account-auditor.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/swift-account-reaper.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/swift-account-replicator.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/swift-account.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/swift-container-auditor.service
install -m 0644 %{SOURCE6} %{buildroot}/usr/lib/systemd/system/swift-container-replicator.service
install -m 0644 %{SOURCE7} %{buildroot}/usr/lib/systemd/system/swift-container-updater.service
install -m 0644 %{SOURCE8} %{buildroot}/usr/lib/systemd/system/swift-container.service
install -m 0644 %{SOURCE9} %{buildroot}/usr/lib/systemd/system/swift-object-auditor.service
install -m 0644 %{SOURCE10} %{buildroot}/usr/lib/systemd/system/swift-object-replicator.service
install -m 0644 %{SOURCE11} %{buildroot}/usr/lib/systemd/system/swift-object-updater.service
install -m 0644 %{SOURCE12} %{buildroot}/usr/lib/systemd/system/swift-object.service
install -m 0644 %{SOURCE13} %{buildroot}/usr/lib/systemd/system/swift-proxy.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE14} %{buildroot}/usr/lib/tmpfiles.d/swift.conf
## install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/swift
for i in proxy-server account-server container-server object-server container-reconciler object-expirer swift; do
install -p -D -m 644 etc/${i}.conf-sample %{buildroot}/usr/share/defaults/swift/${i}.conf
done
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swift-account-audit
/usr/bin/swift-account-auditor
/usr/bin/swift-account-info
/usr/bin/swift-account-reaper
/usr/bin/swift-account-replicator
/usr/bin/swift-account-server
/usr/bin/swift-config
/usr/bin/swift-container-auditor
/usr/bin/swift-container-info
/usr/bin/swift-container-reconciler
/usr/bin/swift-container-replicator
/usr/bin/swift-container-server
/usr/bin/swift-container-sharder
/usr/bin/swift-container-sync
/usr/bin/swift-container-updater
/usr/bin/swift-dispersion-populate
/usr/bin/swift-dispersion-report
/usr/bin/swift-drive-audit
/usr/bin/swift-form-signature
/usr/bin/swift-get-nodes
/usr/bin/swift-init
/usr/bin/swift-manage-shard-ranges
/usr/bin/swift-object-auditor
/usr/bin/swift-object-expirer
/usr/bin/swift-object-info
/usr/bin/swift-object-reconstructor
/usr/bin/swift-object-relinker
/usr/bin/swift-object-replicator
/usr/bin/swift-object-server
/usr/bin/swift-object-updater
/usr/bin/swift-oldies
/usr/bin/swift-orphans
/usr/bin/swift-proxy-server
/usr/bin/swift-recon
/usr/bin/swift-recon-cron
/usr/bin/swift-reconciler-enqueue
/usr/bin/swift-ring-builder
/usr/bin/swift-ring-builder-analyzer

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/swift-account-auditor.service
/usr/lib/systemd/system/swift-account-reaper.service
/usr/lib/systemd/system/swift-account-replicator.service
/usr/lib/systemd/system/swift-account.service
/usr/lib/systemd/system/swift-container-auditor.service
/usr/lib/systemd/system/swift-container-replicator.service
/usr/lib/systemd/system/swift-container-updater.service
/usr/lib/systemd/system/swift-container.service
/usr/lib/systemd/system/swift-object-auditor.service
/usr/lib/systemd/system/swift-object-replicator.service
/usr/lib/systemd/system/swift-object-updater.service
/usr/lib/systemd/system/swift-object.service
/usr/lib/systemd/system/swift-proxy.service
/usr/lib/tmpfiles.d/swift.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/swift/account-server.conf
/usr/share/defaults/swift/container-reconciler.conf
/usr/share/defaults/swift/container-server.conf
/usr/share/defaults/swift/object-expirer.conf
/usr/share/defaults/swift/object-server.conf
/usr/share/defaults/swift/proxy-server.conf
/usr/share/defaults/swift/swift.conf

%files license
%defattr(-,root,root,-)
/usr/share/doc/swift/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
