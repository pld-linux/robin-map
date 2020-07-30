Summary:	A C++ implementation of a fast hash map and hash set using robin hood hashing
Summary(pl.UTF-8):	Implementacja C++ szybkiej tablicy asocjacyjnej i zbioru wykorzytujących haszowanie robin hood
Name:		robin-map
Version:	0.6.3
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/Tessil/robin-map/releases
Source0:	https://github.com/Tessil/robin-map/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e6a362bff8372bbb4d901d2e28993a8a
URL:		https://github.com/Tessil/robin-map
BuildRequires:	cmake >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The robin-map library is a C++ implementation of a fast hash map and
hash set using open-addressing and linear robin hood hashing with
backward shift deletion to resolve collisions.

%description -l pl.UTF-8
Biblioteka robin-map to implementacja C++ szybkiej tablicy
asocjacyjnej (mapy) i zbioru wykorzystujących adresowanie otwarte i
haszowanie robin hood z usuwaniem przez przesunięcie wstecz przy
rozwiązywaniu kolizji.

%package devel
Summary:	Header files for robin-map library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki robin-map
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.8

%description devel
Header files for robin-map library.

The robin-map library is a C++ implementation of a fast hash map and
hash set using open-addressing and linear robin hood hashing with
backward shift deletion to resolve collisions.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki robin-map.

Biblioteka robin-map to implementacja C++ szybkiej tablicy
asocjacyjnej (mapy) i zbioru wykorzystujących adresowanie otwarte i
haszowanie robin hood z usuwaniem przez przesunięcie wstecz przy
rozwiązywaniu kolizji.

%prep
%setup -q

%build
mkdir -p build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{_includedir}/tsl
%{_includedir}/tsl/robin*.h
%{_datadir}/cmake/tsl-robin-map
