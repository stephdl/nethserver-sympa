Summary: nethserver-sympa  is a module for the software sympa
%define name nethserver-sympa
Name: %{name}
%define version 0.0.5
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: sympa sympa-httpd
Requires: nethserver-mail-server
Requires: nethserver-mysql
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Sympa is a Mailing list management (MLM) software. Its name, which is an acronym 
for Système de Multi-Postage Automatique (i.e. Automatic Mailing System)


%prep
%setup

%build
%{makedocs}
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post

%postun
if [ $1 == 0 ] ; then
    /usr/bin/rm -f /etc/httpd/conf.d/sympa.conf
    /usr/bin/rm -f /etc/httpd/conf.d/zzz_sympa.conf
    /usr/bin/systemctl reload httpd
fi

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%config(noreplace) /etc/sympa/list_aliases.tt2
%config(noreplace) %attr(0644,sympa,sympa) /etc/sympa/scenari/create_list.public_listmaster
%attr(0440,root,root) /etc/sudoers.d/50_nsapi_nethserver_sympa

%changelog
* Tue Feb 15 2022 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5
- Fix the visudo warning 

* Sat Jul 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4
- Remove http templates after rpm removal

* Sat May 02 2020 stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.3
- Beta stage released

* Sun Apr 26 2020 stephane de Labrusse <stephdl@de-labrusse.fr>
- Multi domain email available

* Tue Apr 21 2020 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial
