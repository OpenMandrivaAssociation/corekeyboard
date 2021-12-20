#global debug_package %{nil}

Name:           corekeyboard
Version:        4.2.0
Release:        1
Summary:        A virtual keyboard for X11 from the CoreApps family
License:        GPL3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/corekeyboard
Source0:        https://gitlab.com/cubocore/coreapps/corekeyboard/-/archive/v%{version}/corekeyboard-v%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(cprime)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(x11)

Requires: libcprime
  
%description
A virtual keyboard for X11 for C Suite. This project uses X11 functions from from kvkbd.

%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake

%build
%make_build

%install
%make_install -C build

%files
%{_bindir}/corekeyboard
%{_datadir}/applications/corekeyboard.desktop
%{_datadir}/icons/*/*/*/corekeyboard.*
