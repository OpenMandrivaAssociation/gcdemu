
%define version 1.0.0
%define snapshot 300
%define rel	1

%if 0
# Update commands:
REV=$(svn info https://cdemu.svn.sourceforge.net/svnroot/cdemu/trunk/gcdemu | sed -ne 's/^Last Changed Rev: //p')
svn export -r $REV https://cdemu.svn.sourceforge.net/svnroot/cdemu/trunk/gcdemu gcdemu-$REV
tar -cjf gcdemu-$REV.tar.bz2 gcdemu-$REV
%endif

Name:		gcdemu
Version:	%version
Summary:	GNOME applet for controlling CDEmu daemon
%if %snapshot
Release:	%mkrel 1.svn%snapshot.%rel
Source:		%name-%snapshot.tar.bz2
%else
Release:	%mkrel %rel
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2
%endif
Group:		Emulators
License:	GPLv2+
URL:		http://cdemu.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-root
# bonobo/server is in arched dir
#BuildArch:	noarch
BuildRequires:	python
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	pygtk2.0-devel
Requires:	cdemu-daemon
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
%if %snapshot
%setup -q -n %name-%snapshot
%else
%setup -q
%endif

%build
%if %snapshot
./autogen.sh
%endif
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

%post
%post_install_gconf_schemas gcdemu

%preun
%preun_uninstall_gconf_schemas gcdemu

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
