Summary:	Matchbox applet for managing software input methods
Summary(pl):	Aplet ¶rodowiska Matchbox do zarz±dzania programowymi metodami wprowadzania
Name:		matchbox-applet-input-manager
Version:	0.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/mb-applet-input-manager/%{version}/mb-applet-input-manager-%{version}.tar.bz2
# Source0-md5:	8a7ac22fdbbc7d3fdbfd0d7e98bb0de0
Patch0:		%{name}-desktop.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	libmatchbox-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox applet for managing software input methods.

%description -l pl
Aplet ¶rodowiska Matchbox do zarz±dzania programowymi metodami
wprowadzania.

%prep
%setup -q -n mb-applet-input-manager-%{version}
%patch0 -p1

%build
%configure
# %{?with_gnome:--enable-gnomeapplet} (broken)
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/mbinputmgr
%{_desktopdir}/mbinputmgr.desktop
%{_pixmapsdir}/mbinputmgr.png
