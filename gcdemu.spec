Name:		gcdemu
Version:	1.4.0
Summary:	GNOME applet for controlling CDEmu daemon
Release:	1
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.gz
Group:		Emulators
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-root
# bonobo/server is in arched dir
#BuildArch:	noarch
BuildRequires:	python
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	pygtk2.0-devel
BuildRequires:	libGConf2-devel
# cdemu-daemon 1.3.0 switched to session bus
Requires:	cdemu-daemon >= 1.3.0
Requires:	pygtk2.0
Requires:	gnome-python-gconf
Requires:	gnome-python-applet
Requires:	python-dbus
Requires:	python-notify

%description
This is gCDEmu, a GNOME applet for controlling CDEmu daemon. It is
part of the userspace-cdemu suite, a free, GPL CD/DVD-ROM device
emulator for linux.

It provides a graphic interface that allows performing the key tasks
related to controlling the CDEmu daemon, such as loading and
unloading devices, displaying devices' status and retrieving/setting
devices' debug masks.

In addition, the applet listens to signals emitted by CDEmu daemon
and provides notifications via libnotify.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

%if %mdkversion < 200900
%post
%post_install_gconf_schemas gcdemu
%preun
%preun_uninstall_gconf_schemas gcdemu
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%{_sysconfdir}/gconf/schemas/gcdemu.schemas
%{_bindir}/gcdemu
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
