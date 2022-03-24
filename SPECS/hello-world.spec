Summary: Example of RPM-packaged hello world 
Name: hello-world
Version: 1.1
Release: 1%{?dist}
License: GPLv3+ and GFDL
Group: Applications/File
Source0: hello-world.tar.gz
Patch0: brand-new.patch
URL: http://www.ok.org/
#Requires:
BuildRequires: gcc, make, grep
Provides: hello-world

%description
This is a simple package that consists of Hello World app.

%global debug_package %{nil}

%prep
%setup -q
%patch0

%build
export CC="%{__cc}"
export CPP="%{__cpp}"
export CXX="%{__cxx}"
export CFLAGS=""
make
make check

%install
%make_install

%post

%preun

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
* Thu Mar 24 2022 Some Guy <some.guy@there.com> - 1.1-1
- Fix bug n1
  Thats it

