#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Find
Summary:	Email::Find - find RFC 822 email addresses in plain text
Summary(pl):	Email::Find - wyszukiwanie adresów pocztowych RFC 822 w czystym tek¶cie
Name:		perl-Email-Find
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	988182c9b5ec80861ee3749a434104ea
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Email::Font to modu³ do wyszukiwania _podzbioru_ adresów pocztowych
RFC 822 w dowolnym tek¶cie. Nie ma gwarancji, ¿e znalezione adresy
bêd± istnia³y lub nawet faktycznie bêd± adresami pocztowymi, ale bêd±
mia³y sk³adnie zgodn± z RFC 822.

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
