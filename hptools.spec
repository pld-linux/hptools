Summary:	HP Tools - utilities to setup HP printers
Summary(pl):	HP Tools - narzêdzia do sterowania drukarkami HP
Name:		hptools
Version:	1.2.3
Release:	1
License:	freely distributable
Group:		Applications/Printing
Source0:	ftp://metalab.unc.edu/pub/Linux/system/printing/%{name}-%{version}.tar.gz
# Source0-md5:	50fe26553a0309bd6ef06144c177c5c8
Patch0:		%{name}-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hpset is used to send commands to a printer. These commands are
synonyms for ESC Codes based on the PCL standard from Hewlett Packard.

%description -l pl
hpset s³u¿y do wysy³ania poleceñ do drukarki. Polecenia te s±
synonimami kodów ESC bazuj±cych na standardzie PCL Hewletta Packarda.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
