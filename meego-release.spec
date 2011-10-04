%define release_name MeeGo
%define dist_version 1.2.90

Summary:	%{release_name} release files
Name:		meego-release
Version:	%{dist_version}
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.meego.com
Provides:	system-release = %{version}-%{release}
Provides:   moblin-release = 2.2
Obsoletes:  moblin-release <= 2.1.92-4.6
BuildArch:	noarch
Source0:    RPM-GPG-KEY-meego

%description
%{release_name} release files such as various /etc/ files that define the release.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
echo "MeeGo release %{dist_version} (%{release_name})" > $RPM_BUILD_ROOT/etc/meego-release
cp -p $RPM_BUILD_ROOT/etc/meego-release $RPM_BUILD_ROOT/etc/issue

echo "Kernel \r on an \m" >> $RPM_BUILD_ROOT/etc/issue
cp -p $RPM_BUILD_ROOT/etc/issue $RPM_BUILD_ROOT/etc/issue.net
echo >> $RPM_BUILD_ROOT/etc/issue

ln -s meego-release $RPM_BUILD_ROOT/etc/system-release
ln -s meego-release $RPM_BUILD_ROOT/etc/moblin-release

# Install the MeeGo GPG RPM pubkey
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp %{SOURCE0} $RPM_BUILD_ROOT/etc/pki/rpm-gpg
pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg
ln -sf RPM-GPG-KEY-meego RPM-GPG-KEY-meego-2-primary
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) /etc/meego-release
/etc/system-release
/etc/moblin-release
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
/etc/pki/rpm-gpg
