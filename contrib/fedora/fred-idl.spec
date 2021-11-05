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
BuildRequires: cmake

%description
FRED (Free Registry for Enum and Domain) is free registry system for 
managing domain registrations. This package contains idl files with definition
of corba interfaces to server

%package -n python3-fred-idl
Summary: FRED - python3 compiled idl interfaces
BuildRequires: python3 python3-omniORB omniORBpy-devel omniORB-devel python3-devel

%package -n python2-fred-idl
Summary: FRED - python2 compiled idl interfaces
BuildRequires: python2 python2-omniORB omniORBpy-devel omniORB-devel python2-devel

%description -n python3-fred-idl
FRED (Free Registry for Enum and Domain) is free registry system for 
managing domain registrations. This package contains python3 compiled idl
files with definition of corba interfaces to server.

%description -n python2-fred-idl
FRED (Free Registry for Enum and Domain) is free registry system for 
managing domain registrations. This package contains python3 compiled idl
files with definition of corba interfaces to server.

%prep
%setup -q

%build

mkdir build_py2
pushd build_py2
export PYTHON=%{__python2}
%cmake -DPYTHON=python2 -DVERSION=%{version} ..
%cmake_build
popd

mkdir build_py3
pushd build_py3
export PYTHON=%{__python3}
%cmake -DPYTHON=python3 -DVERSION=%{version} ..
%cmake_build
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd build_py2
%cmake_install
popd
pushd build_py3
%cmake_install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files -n fred-idl
%defattr(-,root,root,-)
/usr/share/idl/fred/*.idl

%files -n python3-fred-idl
%{python3_sitearch}/*

%files -n python2-fred-idl
%{python2_sitearch}/*


%changelog
