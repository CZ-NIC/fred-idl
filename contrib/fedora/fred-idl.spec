%define debug_package %{nil}
Name:		%{project_name}
Version:	%{our_version}
Release:	%{?our_release}%{!?our_release:1}%{?dist}
Summary:	FRED - idl interface files
Group:		Applications/Utils
License:	GPLv3+
URL:		http://fred.nic.cz
Source:         %{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
%define python_version python2
%if 0%{?el7}
BuildRequires: centos-release-scl, llvm-toolset-7-cmake, llvm-toolset-7-build
%else
BuildRequires: cmake
%endif
BuildRequires:  omniORBpy-devel, %{python_version}-devel

%description
FRED (Free Registry for Enum and Domain) is free registry system for 
managing domain registrations. This package contains idl files with definition
of corba interfaces to server

%prep
%setup -q

%build
%if 0%{?el7}
%{?scl:scl enable llvm-toolset-7 - << \EOF}
%global __cmake /opt/rh/llvm-toolset-7/root/usr/bin/cmake
%endif
%cmake -DPYTHON=%{python_version} -DVERSION=%{version} .
%if 0%{?el7}
%make_build
%else
%cmake_build
%endif
%if 0%{?el7}
%{?scl:EOF}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if 0%{?el7}
%make_install
%else
%cmake_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/idl/fred/*.idl
%{python2_sitearch}/*

%changelog
