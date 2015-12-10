%define major 10
%define libname %mklibname input %{major}
%define develname %mklibname -d input

Summary:	Handles input devices for display servers
Name:		libinput
Version:	1.1.2
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
CFLAGS="%{optflags} -Qunused-arguments" %configure

%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files

%{_bindir}/libinput-list-devices
%{_bindir}/libinput-debug-events
%{_libdir}/udev/libinput-device-group
%{_libdir}/udev/hwdb.d/90-libinput-model-quirks.hwdb
%{_libdir}/udev/rules.d/*.rules
%{_libdir}/udev/libinput-model-quirks
%{_mandir}/man1/libinput-list-devices.1.*
%{_mandir}/man1/libinput-debug-events.1.*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc README.txt COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
