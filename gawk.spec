Summary:	The GNU version of the awk text processing utility
Summary(de):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(fr):	Traitement de texte des utilitaires GNU
Summary(pl):	Wersja GNU awk - narz�dzia do obr�bki tekst�w
Summary(tr):	GNU ara�lar� metin d�zenleyici
Name:		gawk
Version:	3.0.6
Release:	3
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-unaligned.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-mktemp.patch
Patch3:		%{name}-DESTDIR.patch
Requires:	mktemp
Requires:	sed
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gawk-doc

%define		_libexecdir	%{_prefix}/lib
%define		_libdir		%{_prefix}/lib

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%description -l de
Das gawk-Paket enth�lt die GNU-Version von awk, einem
Textverarbeitungs-Utility. Awk interpretiert eine spezielle
Programmiersprache, um Textmuster zu suchen, und neu zu formatieren.
Gawk ist kompatibel zu der Bell Labs research-Version von awk, und ist
fast kompatibel zum 1993 POSIX 1003.2-awk-Standard.

%description -l fr
awk de GNU, compatible vers le haut avec les versions awk des Bell
Labs. Il est presque totalement conforme au standard 1993 POSIX 1003.2
de awk.

gawk sert � traiter les fichiers texte est est consid�r� comme un
outil standard de Linux.

%description -l pl
Pakiet zawiera implementacj� GNU interpretera j�zyka awk, kt�ry
powinien by� kompatybilny z aplikacj� o tej samej nazwie zrobion�
przez Bell Labs. GNU awk jest w pe�ni zgodny ze standardem 1993 POSIX
1003.2.

Gawk (GNU awk) jest zaawansowanym j�zykiem skryptowym, doskonale
nadaj�cym si� do obr�bki plik�w tekstowych. Jest to jedno z
podstawowych narz�dzi systemu Linux.

%description -l tr
Gawk metin dosyalar�n� i�lemek i�in kullan�lan standart Linux
Ara�lar�ndan biridir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .wiget

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

rm -f $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}

gzip -9nf README ACKNOWLEDGMENT FUTURES LIMITATIONS NEWS PORTS \
	README_d/README.linux POSIX.STD

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz README_d/README.linux.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*
%attr(755,root,root) %{_libdir}/awk
%{_datadir}/awk
