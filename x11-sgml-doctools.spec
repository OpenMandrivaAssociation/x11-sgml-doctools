Name: x11-sgml-doctools
Version: 1.6
Release: %mkrel 1
Summary: Xorg X11 sgml documentation tools
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/doc/xorg-sgml-doctools-%{version}.tar.bz2
License: MIT

BuildRequires: x11-util-macros >= 1.0.1

Obsoletes: xorg-x11 < 7.0

%description
Xorg X11 sgml documentation tools

%prep
%setup -q -n xorg-sgml-doctools-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/sgml/X11/defs.ent
%{_datadir}/sgml/X11/xorg.css
%{_datadir}/sgml/X11/xorg.xsl
%{_datadir}/pkgconfig/xorg-sgml-doctools.pc
