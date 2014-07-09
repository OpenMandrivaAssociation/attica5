%define major	5
%define libname %mklibname KF5Attica %{major}
%define devname %mklibname KF5Attica -d

Summary:	Open Collaboration Service providers library
Name:		attica5
Version:	5.0.0
Release:	1
License:	GPLv2+
Group:		System/Base
Url:		http://www.kde.org/
Source0:	http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/attica-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	extra-cmake-modules5 >= 1.0.0

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
%cmake
%make

%install
%makeinstall_std -C build

# qmake bits are installed into the wrong location...
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

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
