%define major 10
%define libname %mklibname input %{major}
%define develname %mklibname -d input

Summary:	Handles input devices for display servers
Name:		libinput
Version:	0.12.0
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
Requires:	%{name} = %{EVRD}

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

%files
%{_libdir}/udev/libinput-device-group
%{_libdir}/udev/rules.d/80-libinput-device-groups.rules

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc README.txt COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
