%define version 1.3.0
%define rel	1

Name:		gcdemu
Version:	%version
Summary:	GNOME applet for controlling CDEmu daemon
Release:	%mkrel %rel
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

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS
%{_sysconfdir}/gconf/schemas/gcdemu.schemas
%{python_sitelib}/gcdemu
%{_libdir}/bonobo/servers/GNOME_gCDEmuApplet.server
%{_libdir}/gcdemu
%{_datadir}/omf/gcdemu
%doc %{_datadir}/gnome/help/gcdemu
%{_datadir}/pixmaps/%{name}
