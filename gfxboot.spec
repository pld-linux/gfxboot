#
# spec file for package gfxboot (Version 1.4)
#
# Copyright  (c)  2001  SuSE GmbH  Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# please send bugfixes or comments to feedback@suse.de.
#

# neededforbuild  nasm xdevel xf86 xshared
# usedforbuild    aaa_base aaa_dir autoconf automake base bash bindutil binutils bison bzip compress cpio cpp cracklib cyrus-sasl db devs diffutils e2fsprogs file fileutils findutils flex gawk gcc gdbm gdbm-devel gettext glibc glibc-devel gpm gppshare grep groff gzip kbd less libtool libz m4 make man mktemp modutils nasm ncurses ncurses-devel net-tools netcfg pam pam-devel patch perl ps rcs readline rpm sendmail sh-utils shadow strace syslogd sysvinit texinfo textutils timezone unzip util-linux vim xdevel xf86 xshared

Name:		gfxboot
Copyright:	Copyright (c) 1999 SuSE GmbH
Summary:	Graphical boot logo for lilo and syslinux
Version:	4.2.1
Release:	1
Group:		Applications/System
URL:		http://www.gamers.org/~quinet/lilo/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	d37d8bbb10df63723a895203e4289dd0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
AutoReqProv:	on

%description
Here you find the graphical boot logo. Suitable for both lilo and
syslinux.

SuSE series: ap

%package themes
Summary:	Tools for creating a graphical boot logo
Group:		Applications/System

%description themes
Here you find the necessary programs to create your own graphical boot
logo. The logo can be used with lilo and syslinux.

SuSE series: ap

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/gfxboot
%attr(755,root,root) %{_sbindir}/gfxboot-compile
%attr(755,root,root) %{_sbindir}/gfxboot-font
%attr(755,root,root) %{_sbindir}/gfxtest

%files themes
%defattr(644,root,root,755)
%{_sysconfdir}/bootsplash/themes/SLED
%{_sysconfdir}/bootsplash/themes/SLES
%{_sysconfdir}/bootsplash/themes/openSUSE
%{_sysconfdir}/bootsplash/themes/upstream
