%include	/usr/lib/rpm/macros.python
%define		mod_name	python
%define 	apxs		/usr/sbin/apxs
Summary:	An embedded Python interpreter for the Apache Web server
Summary(cs):	Vestav�n� interpret Pythonu pro WWW server Apache
Summary(da):	En indbygget Python-fortolker for webtjeneren Apache
Summary(de):	Ein eingebetteter Python-Interpreter f�r den Apache Web-Server
Summary(es):	Int�rprete Perl para el servidor Web Apache
Summary(fr):	Interpr�teur Python int�gr� pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl t�lkur fyrir Apache vef�j�ninn
Summary(it):	Interprete Python integrato per il server Web Apache
Summary(ja):	Apache Web �����С��Ѥ��ȹ��� Perl ���󥿡��ץ꥿
Summary(no):	En Python-fortolker for webtjeneren Apache
Summary(pl):	Wbudowany interpreter Pythona dla serwera WWW Apache
Summary(pt):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru):	���������� ������������� Perl ��� WWW-������� Apache
Summary(sk):	Interpreter jazyka Perl pre webov� server Apache
Summary(sl):	Vklju�eni pythonski tolma� za spletni stre�nik Apache
Summary(sv):	En inbyggd Python-interpretator f�r webbservern Apache
Name:		apache-mod_%{mod_name}
Version:	2.7.8
Release:	3
License:	distributable
Group:		Networking/Daemons
Source0:	http://www.modpython.org/dist/mod_%{mod_name}-%{version}.tgz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-Makefile-in.patch
Patch3:		%{name}-cleanup.patch
URL:		http://www.modpython.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	apache-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	%{apxs}
Prereq:		%{_sbindir}/apxs
Requires:	apache
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apache_moddir	%(%{apxs} -q LIBEXECDIR)

%description
Mod_python is a module that embeds the Python language interpreter
within the server, allowing Apache handlers to be written in Python.

Mod_python brings together the versatility of Python and the power of
the Apache Web server for a considerable boost in flexibility and
performance over the traditional CGI approach.

%description -l cs
Bal��ek mod_python obsahuje modul, kter� umo�n� serveru Apache p��mo
interpretovat CGI skripty napsan� v jazyce Python. To vede k v�razn�mu
zv��en� rychlosti jejich proveden�.

%description -l de
Mod_python ist ein Modul, das den Python-Sprachinterpreter innerhalb
des Servers einbettet und es den Apache-Handlern erm�glicht, in Python
geschrieben zu werden.

Mod_python verbindet die Vielseitigkeit von Python und die
Leistungsst�rke des Apache Web-Servers, was eine enorme Steigerung der
Flexibilit�t und Leistung gegen�ber dem traditionellen CGI-Ansatz
bedeutet.

%description -l es
Mod_python es un m�dulo que activa el int�rprete de Python en el
servidor, permitiendo que se escriban gestores para Apache en Python.

Mod_python proporciona la versatilidad y el poder del servidor web
Apache para acelerar considerablemente la flexibilidad y prestaciones
en comparaci�n a una aproximaci�n tradicional con CGI.

%description -l fr
Mod_python est un module qui int�gre l'interpr�teur de langage Python
dans le serveur, permettant aux gestionnaires Apache d'�tre �crits en
Python.

Mod_python conjugue la versatilit� de Python et la puissance du
serveur Web Apache de fa�on � augmenter consid�rablement la
flexibilit� et la performance par rapport � une approche CGI
traditionnelle.

%description -l it
Mod_python � un modulo che integra nel server l'interprete del
linguaggio Python, in modo che i programmi di gestione possano essere
scritti in Python.

Mod_python unisce in s� la versatilit� di Python e la potenza del
server Web Apache, con un conseguente accrescimento di flessibilit� e
un miglioramento notevole nelle prestazioni rispetto all'approccio
tradizionale CGI.

%description -l ja
Mod_python �ϥ����С���� Python
���쥤�󥿡��ץ꥿���Ȥ߹�����⥸�塼�� �Ǥ�������ˤ�ꡢApache
�ϥ�ɥ�� Python �ǵ��ҤǤ��ޤ��� Mod_python �ϡ�Python ����������
Apache Web �����С��Υѥ���Ȥ߹�碌�� ���Ȥˤ�ꡢ����� CGI
���ץ�������������ȥѥե����ޥ󥹤������˸��夵���ޤ���

%description -l pl
mod_python jest modu�em osadzaj�cym interpreter j�zyka Python w
serwerze WWW Apache, umo�liwiaj�c mu obs�ug� kodu napisanego w
Pythonie.

mod_python ��czy wszechstronno�� Pythona i moc Apache'a jako serwera
WWW, co daje zwi�kszon� elastyczno�� i zauwa�aln� popraw� wydajno�ci w
stosunku do tradycyjnego rozwi�zania opartego na CGI.

%description -l sv
Mod_python �r en modul som bygger in en interpretator f�r spr�ket
Python i servern, och l�ter Apach-hanterare skrivas i Python.

Mod_python sammanf�r m�ngsidigheten hos Python och kraften hos
webbservern Apache till en avsev�rd �kning av flexibiliteten och
prestandan j�mf�rt med den traditionella CGI-metoden.

%prep
%setup -q -n mod_%{mod_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal
%{__autoconf}

# new apache needs it
CFLAGS="-DEAPI %{rpmcflags}"
%configure \
	--with-apxs=%{apxs}

%{__make} dso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apache_moddir},%{py_sitedir}/mod_%{mod_name}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README COPYRIGHT NEWS CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{apxs} -e -a -n %{mod_name} %{apache_moddir}/mod_%{mod_name}.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n %{mod_name} %{apache_moddir}/mod_%{mod_name}.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc doc-html/*
%doc {README,COPYRIGHT,NEWS,CREDITS}.gz
%attr(755,root,root) %{apache_moddir}/*
%{py_sitedir}/mod_%{mod_name}
