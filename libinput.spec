%define major 10
%define libname %mklibname input %{major}
%define develname %mklibname -d input

%global optflags %{optflags} -O3

Summary:	Handles input devices for display servers
Name:		libinput
Version:	1.15.2
Release:	1
License:	LGPLv2
Group:		System/Libraries
URL:		http://www.freedesktop.org/wiki/Software/libinput/
Source0:	http://www.freedesktop.org/software/libinput/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(libwacom)
BuildRequires:	pkgconfig(check)
BuildRequires:	meson
BuildRequires:	systemd-macros

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
%autosetup -p1

%meson -Dudev-dir=/lib/udev -Ddocumentation=false -Ddebug-gui=false

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/libinput
/lib/udev/libinput-device-group
/lib/udev/libinput-fuzz-extract
/lib/udev/libinput-fuzz-to-zero
%{_udevrulesdir}/*.rules
%{_libexecdir}/libinput/libinput*
%{_datadir}/%{name}/*.quirks
%{_mandir}/man1/%{name}*.1*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc README.md COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
