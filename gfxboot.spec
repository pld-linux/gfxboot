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
Group:		Applications/System
Summary:	Graphical boot logo for lilo and syslinux.
Version:	1.4
Release:	1
URL:		http://www.gamers.org/~quinet/lilo/
Source0:	http://members.optusnet.com.au/rkelsen/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pld.patch
AutoReqProv:	on
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Here you find the graphical boot logo. Suitable for both lilo and
syslinux.

SuSE series: ap

%package -n gfxboot-devel
Summary:	Tools for creating a graphical boot logo.
Group:		Applications/System

%description -n gfxboot-devel
Here you find the necessary programs to create your own graphical boot
logo. The logo can be used with lilo and syslinux.

SuSE series: ap

%prep
%setup -q
%patch0 -p1

%build
%{__make}
./mkbootmsg -c suselogo.config suselogo

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_sbindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/gfxboot
install -d -m 755 $RPM_BUILD_ROOT/boot
install -m 755 -s mkbootmsg getx11font $RPM_BUILD_ROOT%{_sbindir}
install -m 644 suselogo $RPM_BUILD_ROOT/boot/message
install -m 644 fixed_10x20 suselogo{,.config,.pcx} $RPM_BUILD_ROOT%{_datadir}/gfxboot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/boot/message
%doc README

%files -n gfxboot-devel
%defattr(644,root,root,755)
%dir %{_datadir}/gfxboot
%attr(755,root,root) %{_sbindir}/mkbootmsg
%attr(755,root,root) %{_sbindir}/getx11font
%{_datadir}/gfxboot/suselogo
%{_datadir}/gfxboot/suselogo.config
%{_datadir}/gfxboot/suselogo.pcx
%{_datadir}/gfxboot/fixed_10x20
