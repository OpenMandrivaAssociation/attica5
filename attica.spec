%define major	5
%define libname %mklibname KF5Attica %{major}
%define devname %mklibname KF5Attica -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Open Collaboration Service providers library
Name:		attica5
Version:	5.4.0
Release:	3
License:	GPLv2+
Group:		System/Base
Url:		http://www.kde.org/
Source0:	http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/attica-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qt5-devel
BuildRequires:	extra-cmake-modules5 >= %(echo %{version} |sed -e 's,^5,1,')
BuildRequires:	pkgconfig(egl)

%description
A library to access Open Collaboration Service providers 
Required to access OSC providers in get hot new stuff. 

%package -n %{libname}
Summary:	Open Collaboration Service providers library, part of KDE Frameworks 5
Group:		System/Libraries

%description -n %{libname}
A library to access Open Collaboration Service providers 
Required to access OSC providers in get hot new stuff. 

It is part of KDE Frameworks 5.

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < 0.4.1-2

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%prep
%setup -q -n attica-%{version}

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install

%files -n %{libname}
%{_libdir}/libKF5Attica.so.%{version}
%{_libdir}/libKF5Attica.so.%{major}

%files -n %{devname}
%dir %{_includedir}/KF5
%{_includedir}/KF5/attica_version.h
%{_includedir}/KF5/Attica
%{_libdir}/libKF5Attica.so
%{_libdir}/pkgconfig/libKF5Attica.pc
%{_libdir}/cmake/KF5Attica
%{_libdir}/qt5/mkspecs/modules/*.pri
