Summary:	Graphical boot logo for lilo and syslinux
Name:		gfxboot
Version:	4.2.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	d37d8bbb10df63723a895203e4289dd0
URL:		http://www.gamers.org/~quinet/lilo/
BuildRequires:	freetype-devel
BuildRequires:	nasm
BuildRequires:	perl-base
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Here you find the graphical boot logo. Suitable for both lilo and
syslinux.

%package themes
Summary:	Tools for creating a graphical boot logo
Group:		Applications/System

%description themes
Here you find the necessary programs to create your own graphical boot
logo. The logo can be used with lilo and syslinux.

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
