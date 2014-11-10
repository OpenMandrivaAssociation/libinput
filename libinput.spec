%define major 5
%define libname %mklibname input %{major}
%define develname %mklibname -d input

Summary:	Handles input devices for display servers
Name:		libinput
Version:	0.6.0
Release:	1
License:	LGPLv2
Group:		System/Libraries
URL:		http://www.freedesktop.org/wiki/Software/libinput/
Source0:	http://www.freedesktop.org/software/libinput/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libevdev)

%description
libinput is a library to handle input devices in Wayland
compositors and to provide a generic X.Org input driver.

%package -n %{libname}
Summary:	Libraries for libinput
Group:		System/Libraries

%description -n %{libname}
libinput is a library to handle input devices in Wayland
compositors and to provide a generic X.Org input driver.

%package -n %{develname}
Summary:	Development files and heders for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Development files and heders for %{name}.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
