%define upstream_name    Crypt-UnixCrypt_XS
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl-xs implementation of crypt(3)

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/Crypt-UnixCrypt_XS-%{upstream_version}.tar.gz
Patch0:		Crypt-UnixCrypt_XS-0.10-debug.patch

BuildRequires: perl(Test::More)
BuildRequires: perl-devel

%description
This module implements the DES-based Unix _crypt_ function. For those who
need to construct non-standard variants of _crypt_, the various building
blocks used in _crypt_ are also supplied separately.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/*


