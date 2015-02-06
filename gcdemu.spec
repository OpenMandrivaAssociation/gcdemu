Summary:	GTK+ based GUI for controlling CDEmu daemon
Name:		gcdemu
Version:	2.1.1
Release:	2
Group:		Emulators
License:	GPLv2+
Url:		http://cdemu.sourceforge.net/
Source0:	http://downloads.sourceforge.net/cdemu/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	cmake
BuildRequires:	intltool
# for cdemu daemon interface v3
Requires:	cdemu-daemon
Requires:	python-gi
Requires:	typelib(Notify) >= 0.7
Requires:	typelib(Gtk) >= 3.0
BuildArch:	noarch

%description
gCDEmu is a Gtk+ based GUI for controlling CDEmu daemon. It is part of the
userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator for linux.

It provides a graphic interface that allows performing the key tasks related to
controlling the CDEmu daemon, such as loading and unloading devices, displaying
devices' status and retrieving/setting devices' debug masks.

In addition, it listens to signals emitted by CDEmu daemon and provides
notifications via libnotify.

%files -f %{name}.lang
%doc README AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.svg
%{_datadir}/glib-2.0/schemas/net.sf.cdemu.gcdemu.gschema.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DPOST_INSTALL_HOOKS:BOOL=OFF
%make

%install
%makeinstall_std -C build

%find_lang %{name}


