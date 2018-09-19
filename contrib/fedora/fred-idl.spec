%define debug_package %{nil}
Name:		%{project_name}
Version:	%{our_version}
Release:	%{?our_release}%{!?our_release:1}%{?dist}
Summary:	FRED - idl interface files
Group:		Applications/Utils
License:	GPL
URL:		http://fred.nic.cz
Source:         %{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
%if 0%{?centos}
%define python_version python36
BuildRequires: centos-release-scl, llvm-toolset-7-cmake, llvm-toolset-7-build
%else
%define python_version python3
BuildRequires: cmake
%endif
BuildRequires:  omniORBpy-devel, %{python_version}

%description
FRED (Free Registry for Enum and Domain) is free registry system for 
managing domain registrations. This package contains idl files with definition
of corba interfaces to server

%prep
%setup -q

%build
%if 0%{?centos}
%{?scl:scl enable llvm-toolset-7 - << \EOF}
%global __cmake /opt/rh/llvm-toolset-7/root/usr/bin/cmake
%endif
%cmake -DPYTHON=%{python_version} -DVERSION=%{version} .
%make_build
%if 0%{?centos}
%{?scl:EOF}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/idl/fred/*.idl
/usr/lib/*

%changelog
