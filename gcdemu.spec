Name:		gcdemu
Version:	1.5.0
Summary:	GNOME applet for controlling CDEmu daemon
Release:	1
Source0:	http://downloads.sourceforge.net/project/cdemu/%{name}/%{name}-%{version}.tar.bz2
Group:		Emulators
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	pygtk2.0-devel
#BuildRequires:	libGConf2-devel
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
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%{_datadir}/glib-2.0/schemas/apps.gcdemu.gschema.xml
%{_bindir}/gcdemu
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
