#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swift
Version  : 2.5.0
Release  : 10
URL      : http://tarballs.openstack.org/swift/swift-2.5.0.tar.gz
Source0  : http://tarballs.openstack.org/swift/swift-2.5.0.tar.gz
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
Summary  : OpenStack Object Storage
Group    : Development/Tools
License  : Apache-2.0
Requires: swift-bin
Requires: swift-python
Requires: swift-config
Requires: swift-data
BuildRequires : PasteDeploy
BuildRequires : cffi
BuildRequires : eventlet
BuildRequires : funcsigs
BuildRequires : iso8601
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : nose
BuildRequires : oslo.config
BuildRequires : oslo.log
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycparser
BuildRequires : pyeclib
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python-swiftclient
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : xattr
Patch1: cve-2016-0738.patch
Patch2: 0001-remove-sphinx-1.2.patch

%description
rebuild the .mo with msgfmt (included with GNU gettext)
msgfmt eo.po

%package bin
Summary: bin components for the swift package.
Group: Binaries
Requires: swift-data
Requires: swift-config

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


%package python
Summary: python components for the swift package.
Group: Default
Requires: pyeclib
Requires: simplejson

%description python
python components for the swift package.


%prep
%setup -q -n swift-2.5.0
%patch1 -p1
%patch2 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
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
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/swift
for i in proxy-server account-server container-server object-server container-reconciler object-expirer swift; do
install -p -D -m 644 etc/${i}.conf-sample %{buildroot}/usr/share/defaults/swift/${i}.conf
done
## make_install_append end

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
/usr/bin/swift-container-sync
/usr/bin/swift-container-updater
/usr/bin/swift-dispersion-populate
/usr/bin/swift-dispersion-report
/usr/bin/swift-drive-audit
/usr/bin/swift-form-signature
/usr/bin/swift-get-nodes
/usr/bin/swift-init
/usr/bin/swift-object-auditor
/usr/bin/swift-object-expirer
/usr/bin/swift-object-info
/usr/bin/swift-object-reconstructor
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
/usr/bin/swift-temp-url

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

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
