# norootforbuild

%define __cmake %{_bindir}/cmake
%define _cmake_lib_suffix64 -DLIB_SUFFIX=64
%define cmake \
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ; \
%__cmake \\\
-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \\\
%if "%{?_lib}" == "lib64" \
%{?_cmake_lib_suffix64} \\\
%endif \
-DBUILD_SHARED_LIBS:BOOL=ON

Name:           spectra
Version:        0.9.0
Release:        1%{?dist}
Summary:        C++ Library For Large Scale Eigenvalue Problems
Group:          System Environment/Libraries
License:        MPL2
URL:            https://spectralib.org/
Source0:        https://github.com/yixuan/spectra/archive/spectra-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gcc-c++, cmake, eigen3-devel
Requires:       spectra-devel

%description
C++ Library For Large Scale Eigenvalue Problems.

%package devel
Summary:        C++ Library For Large Scale Eigenvalue Problems
Group:          Development/Libraries/C and C++
Requires:       eigen3-devel

%description devel
C++ Library For Large Scale Eigenvalue Problems (development files)

%prep
%setup -q

%build
%cmake .
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root,-)
%{_includedir}/Spectra/
%{_prefix}/cmake/

%changelog
* Wed Feb 5 2020 Julien Schueller <schueller at phimeca dot com> 0.8.1-1
- Initial package creation
