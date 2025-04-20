%undefine _debugsource_packages

Name: moarvm
Version: 2025.04
Release: 1
Source0: https://moarvm.org/releases/MoarVM-%{version}.tar.gz
Summary: Moar (Metamodel On A Runtime) Virtual Machine, used for NQP and Rakudo
URL: https://moarvm.org/
License: Artistic
Group: Development/Tools
BuildRequires: perl
BuildRequires: perl(ExtUtils::Command)
BuildRequires: make

%description
Moar (Metamodel On A Runtime) Virtual Machine, used for NQP and Rakudo

%package devel
Summary: Development files for the Moar VM
Requires: %{name} = %{EVRD}

%description devel
Development files for the Moar VM

%prep
%autosetup -p1 -n MoarVM-%{version}

%conf
perl Configure.pl --prefix %{_prefix} --libdir %{_libdir}

%build
%make_build

%install
%make_install

%files
%{_bindir}/moar
%{_datadir}/nqp
%{_libdir}/libmoar.so

%files devel
%{_includedir}/moar
%{_datadir}/pkgconfig/moar.pc
%{_libdir}/libmoar.so-gdb.py
# FIXME use system libs
%{_includedir}/dyncall
%{_includedir}/libtommath
%{_includedir}/libuv
%{_includedir}/mimalloc
