%global udevdir %(dirname %{_udevrulesdir})

%define major 10
%define oldlibname %mklibname input 10
%define libname %mklibname input
%define develname %mklibname -d input

%bcond_with bootstrap

Summary:	Handles input devices for display servers
Name:		libinput
Version:	1.29.0
Release:	1
License:	LGPLv2
Group:		System/Libraries
URL:		https://www.freedesktop.org/wiki/Software/libinput/
Source0:	https://gitlab.freedesktop.org/libinput/libinput/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libinput-1.25.0-default-enable-tap.patch
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(check)
%if ! %{with bootstrap}
BuildRequires:	pkgconfig(libwacom)
%endif
BuildRequires:	meson
BuildRequires:	systemd-rpm-macros

%description
libinput is a library to handle input devices in Wayland
compositors and to provide a generic X.Org input driver.

%package -n %{libname}
Summary:	Libraries for libinput
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
%rename %{oldlibname}

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

%meson	-Dudev-dir=%{udevdir} \
	-Ddocumentation=false \
	-Ddebug-gui=false \
	-Dtests=false \
%if %{with bootstrap}
	-Dlibwacom=false
%endif

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/libinput
%{udevdir}/libinput-device-group
%{udevdir}/libinput-fuzz-extract
%{udevdir}/libinput-fuzz-to-zero
%{_udevrulesdir}/*.rules
%{_libexecdir}/libinput/libinput*
%{_datadir}/%{name}/*.quirks
%doc %{_mandir}/man1/%{name}*.1*
%{_datadir}/zsh/site-functions/*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc README.md COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
