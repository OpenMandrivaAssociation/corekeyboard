#global debug_package %{nil}

Name:           corekeyboard
Version:        5.0.1
Release:        1
Summary:        A virtual keyboard for X11 from the CoreApps family
License:        GPL3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/corekeyboard
Source0:        https://gitlab.com/cubocore/coreapps/corekeyboard/-/archive/v%{version}/corekeyboard-v%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: make
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(x11)

Requires: %{_lib}cprime
  
%description
A virtual keyboard for X11 for C Suite. This project uses X11 functions from from kvkbd.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%make_build

%install
%make_install -C build

%files
%{_bindir}/corekeyboard
#{_sysconfdir}/xdg/autostart/org.cubocore.CoreKeyboard-Tray.desktop
%{_datadir}/applications/org.cubocore.CoreKeyboard.desktop
%{_iconsdir}/hicolor/scalable/apps/org.cubocore.CoreKeyboard.svg
