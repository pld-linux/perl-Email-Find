#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Find
Summary:	Email::Find - find RFC 822 email addresses in plain text
Summary(pl.UTF-8):	Email::Find - wyszukiwanie adresów pocztowych RFC 822 w czystym tekście
Name:		perl-Email-Find
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	988182c9b5ec80861ee3749a434104ea
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl-Email-Valid
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Find is a module for finding a _subset_ of RFC 822 email
addresses in arbitrary text. The addresses it finds are not guaranteed
to exist or even actually be email addresses at all, but they will be
valid RFC 822 syntax.

%description -l pl.UTF-8
Email::Font to moduł do wyszukiwania _podzbioru_ adresów pocztowych
RFC 822 w dowolnym tekście. Nie ma gwarancji, że znalezione adresy
będą istniały lub nawet faktycznie będą adresami pocztowymi, ale będą
miały składnie zgodną z RFC 822.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
