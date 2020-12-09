%global debug_package %{nil}

Name:           corekeyboard
Version:        4.1.0
Release:        1
Summary:        A virtual keyboard for X11 from the CoreApps family
License:        GPL3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/corekeyboard
Source0:        https://gitlab.com/cubocore/coreapps/corekeyboard/-/archive/v%{version}/corekeyboard-v%{version}.tar.bz2
#Patch0:		corekeyboard-4.0.0-clang-11.patch

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
%qmake_qt5 \
            PREFIX=%{_prefix}

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/corekeyboard
%{_datadir}/applications/corekeyboard.desktop
%{_datadir}/icons/*/*/*/corekeyboard.*
