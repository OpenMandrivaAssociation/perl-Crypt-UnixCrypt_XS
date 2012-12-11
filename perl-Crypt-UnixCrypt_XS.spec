%define upstream_name    Crypt-UnixCrypt_XS
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl-xs implementation of crypt(3)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.lzma


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements the DES-based Unix _crypt_ function. For those who
need to construct non-standard variants of _crypt_, the various building
blocks used in _crypt_ are also supplied separately.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.90.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2
+ Revision: 680872
- mass rebuild

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 573813
- import perl-Crypt-UnixCrypt_XS

