Name: x11-sgml-doctools
Version: 1.11
Release: 6
Summary: Xorg X11 sgml documentation tools
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/doc/xorg-sgml-doctools-%{version}.tar.bz2
License: MIT
BuildArch: noarch

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
%makeinstall_std

%files
%{_datadir}/sgml/X11/defs.ent
%{_datadir}/sgml/X11/xorg.css
%{_datadir}/sgml/X11/xorg.xsl
%{_datadir}/sgml/X11/dbs/masterdb.*
%{_datadir}/sgml/X11/xorg-fo.xsl
%{_datadir}/sgml/X11/xorg-chunk.xsl
%{_datadir}/sgml/X11/xorg-xhtml.xsl
%{_datadir}/pkgconfig/xorg-sgml-doctools.pc
