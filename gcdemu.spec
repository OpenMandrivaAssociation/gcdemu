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


%changelog
* Mon Feb 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.5.0-1
+ Revision: 781118
- update to 1.5.0

* Wed Nov 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.4.0-1
+ Revision: 732868
- version update to 1.4.0

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 1.3.0-3
+ Revision: 677699
- rebuild to add gconftool as req

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 1.3.0-2mdv2011.0
+ Revision: 594780
- rebuild for python 2.7

* Sat Sep 04 2010 Anssi Hannula <anssi@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 575787
- new version
- bump requirement on cdemu-daemon due to bus switch

* Thu Dec 03 2009 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 472925
- new version 1.2.0

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-2mdv2010.0
+ Revision: 437657
- rebuild

* Tue Jan 27 2009 Guillaume Bedot <littletux@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 333932
- Release 1.1.0

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 1.0.0-1.svn300.2mdv2009.1
+ Revision: 324193
- rebuild

* Wed Apr 23 2008 Anssi Hannula <anssi@mandriva.org> 1.0.0-1.svn300.1mdv2009.0
+ Revision: 197018
- initial Mandriva release

