#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries
#
Summary:	A C++ implementation of a fast hash map and hash set using robin hood hashing
Name:		robin-map
Version:	0.6.1
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	https://github.com/Tessil/robin-map/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	41e517be7cd6fc9294384687d453b27c
URL:		https://github.com/Tessil/robin-map
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The robin-map library is a C++ implementation of a fast hash map and
hash set using open-addressing and linear robin hood hashing with
backward shift deletion to resolve collisions.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries

%description devel
Header files for %{name} library.

The robin-map library is a C++ implementation of a fast hash map and
hash set using open-addressing and linear robin hood hashing with
backward shift deletion to resolve collisions.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
mkdir -p build
cd build
%{cmake} ../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README.md
%dir %{_includedir}/tsl
%{_includedir}/tsl/robin*.h
%{_datadir}/cmake/tsl-robin-map
