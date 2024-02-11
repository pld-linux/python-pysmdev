# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver	20220115
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libcthreads_ver	20160404
%define		libuna_ver	20210801
Summary:	Python 2 bindings for libsmdev library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libsmdev
Name:		python-pysmdev
Version:	20221028
Release:	1
License:	LGPL v3+
Group:		Libraries/Python
#Source0Download: https://github.com/libyal/libsmdev/releases
Source0:	https://github.com/libyal/libsmdev/releases/download/%{version}/libsmdev-alpha-%{version}.tar.gz
# Source0-md5:	193ab43fb38b3a6668d43c8313d25d05
URL:		https://github.com/libyal/libsmdev/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
Requires:	libcerror >= %{libcerror_ver}
Requires:	libsmdev >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libsmdev library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libsmdev.

%prep
%setup -q -n libsmdev-%{version}

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python2 \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keep only python module
%{__rm} $RPM_BUILD_ROOT%{_bindir}/smdevinfo
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/libsmdev*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmdev.*
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/libsmdev.pc
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man{1,3}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pysmdev.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/pysmdev.so
