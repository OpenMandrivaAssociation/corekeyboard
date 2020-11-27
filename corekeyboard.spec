Name:           corekeyboard
Version:        4.0.0
Release:        1
Summary:        A virtual keyboard for X11 from the CoreApps family
License:        GPL3
Group:          System/Libraries
URL:            https://gitlab.com/cubocore/coreapps/corekeyboard
Source0:        https://gitlab.com/cubocore/coreapps/corekeyboard/-/archive/v4.0.0/corekeyboard-v4.0.0.tar.bz2

BuildRequires: qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: libcprime
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(x11)

Requires: libcprime
  
%description
A virtual keyboard for X11 for C Suite. This project uses X11 functions from from kvkbd.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%qmake_qt5 \
            PREFIX=/usr
            
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}


%files
