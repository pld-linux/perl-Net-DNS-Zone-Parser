#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-Zone-Parser
Summary:	Net::DNS::Zone::Parser - a zone pre-parser
Summary(pl):	Net::DNS::Zope::Parser - preparser stref
Name:		perl-Net-DNS-Zone-Parser
Version:	0.002
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	849d8fa00b82da2dc29ec6bf909f4c13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# for `which named-checkzone`
BuildRequires:	bind
BuildRequires:	perl-Net-DNS >= 0.46
BuildRequires:	perl-Net-DNS-SEC >= 0.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::DNS::Zone::Parser should be considered a preprocessor that
"normalizes" a zonefile.

It will read a zonefile in a format conforming to the relevant RFCs
with the addition of BIND's GENERATE directive from disk and will
write fully specified resource records (RRs) to a filehandle.

Note that this module does not have a notion of what constitutes a
valid zone; it only parses. For example, the parser will happilly
parse RRs with ownernames that are below in another zone because a NS
RR elsewhere in the zone.

%description -l pl
Net::DNS::Zone::Parser powinien byæ uwa¿any za preprocesor
"normalizuj±cy" pliki stref. Czyta on z dysku plik strefy w formacie
zgodnym z odpowiednimi RFC oraz dyrektyw± BIND-a GENERATE i zapisuje
w pe³ni okre¶lone rekordy zasobów (RR) do uchwytu pliku.

Nale¿y zauwa¿yæ, ¿e ten modu³ nie ma pojêcia o tym, co stanowi
poprawn± strefê; on jedynie przetwarza. Na przyk³ad parser ten
pomy¶lnie przetworzy rekordy z nazwami w³a¶cicieli bêd±cymi poni¿ej
w innej strefie z powodu rekordów NS w innym miejscu strefy.

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
%doc CHANGES TODO
%{perl_vendorlib}/Net/DNS/Zone/*.pm
%{_mandir}/man3/*
