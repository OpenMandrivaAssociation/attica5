%define major	1.0
%define libname %mklibname attica %{major}
%define devname %mklibname attica -d

Summary:	Open Collaboration Service providers library
Name:		attica5
Version:	4.95.0
Release:	2
License:	GPLv2+
Group:		System/Base
Url:		http://www.kde.org/
Source0:	http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/attica-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qt5-devel

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

%files -n %{libname}
%{_libdir}/libattica.so.%{major}*

%files -n %{devname}
%{_includedir}/attica
%{_libdir}/libattica.so
%{_libdir}/pkgconfig/libattica.pc
%{_libdir}/cmake/LibAttica
