%include	/usr/lib/rpm/macros.python
%define		mod_name	python
%define 	apxs		/usr/sbin/apxs
Summary:	An embedded Python interpreter for the Apache Web server
Summary(cs):	Vestavìný interpret Pythonu pro WWW server Apache
Summary(da):	En indbygget Python-fortolker for webtjeneren Apache
Summary(de):	Ein eingebetteter Python-Interpreter für den Apache Web-Server
Summary(es):	Intérprete Perl para el servidor Web Apache
Summary(fr):	Interpréteur Python intégré pour le serveur Web Apache
Summary(id):	Interpreter Perl untuk web server Apache
Summary(is):	Perl túlkur fyrir Apache vefþjóninn
Summary(it):	Interprete Python integrato per il server Web Apache
Summary(ja):	Apache Web ¥µ¡¼¥Ð¡¼ÍÑ¤ÎÁÈ¹þ¤ß Perl ¥¤¥ó¥¿¡¼¥×¥ê¥¿
Summary(no):	En Python-fortolker for webtjeneren Apache
Summary(pl):	Wbudowany interpreter Pythona dla serwera WWW Apache
Summary(pt):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru):	÷ÓÔÒÏÅÎÎÙÊ ÉÎÔÅÒÐÒÅÔÁÔÏÒ Perl ÄÌÑ WWW-ÓÅÒ×ÅÒÁ Apache
Summary(sk):	Interpreter jazyka Perl pre webový server Apache
Summary(sl):	Vkljuèeni pythonski tolmaè za spletni stre¾nik Apache
Summary(sv):	En inbyggd Python-interpretator för webbservern Apache
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
Balíèek mod_python obsahuje modul, který umo¾ní serveru Apache pøímo
interpretovat CGI skripty napsané v jazyce Python. To vede k výraznému
zvý¹ení rychlosti jejich provedení.

%description -l de
Mod_python ist ein Modul, das den Python-Sprachinterpreter innerhalb
des Servers einbettet und es den Apache-Handlern ermöglicht, in Python
geschrieben zu werden.

Mod_python verbindet die Vielseitigkeit von Python und die
Leistungsstärke des Apache Web-Servers, was eine enorme Steigerung der
Flexibilität und Leistung gegenüber dem traditionellen CGI-Ansatz
bedeutet.

%description -l es
Mod_python es un módulo que activa el intérprete de Python en el
servidor, permitiendo que se escriban gestores para Apache en Python.

Mod_python proporciona la versatilidad y el poder del servidor web
Apache para acelerar considerablemente la flexibilidad y prestaciones
en comparación a una aproximación tradicional con CGI.

%description -l fr
Mod_python est un module qui intègre l'interpréteur de langage Python
dans le serveur, permettant aux gestionnaires Apache d'être écrits en
Python.

Mod_python conjugue la versatilité de Python et la puissance du
serveur Web Apache de façon à augmenter considérablement la
flexibilité et la performance par rapport à une approche CGI
traditionnelle.

%description -l it
Mod_python è un modulo che integra nel server l'interprete del
linguaggio Python, in modo che i programmi di gestione possano essere
scritti in Python.

Mod_python unisce in sé la versatilità di Python e la potenza del
server Web Apache, con un conseguente accrescimento di flessibilità e
un miglioramento notevole nelle prestazioni rispetto all'approccio
tradizionale CGI.

%description -l ja
Mod_python ¤Ï¥µ¡¼¥Ð¡¼Æâ¤Ë Python
¸À¸ì¥¤¥ó¥¿¡¼¥×¥ê¥¿¤òÁÈ¤ß¹þ¤ó¤À¥â¥¸¥å¡¼¥ë ¤Ç¤¹¡£¤³¤ì¤Ë¤è¤ê¡¢Apache
¥Ï¥ó¥É¥é¤ò Python ¤Çµ­½Ò¤Ç¤­¤Þ¤¹¡£ Mod_python ¤Ï¡¢Python ¤ÎÈÆÍÑÀ­¤È
Apache Web ¥µ¡¼¥Ð¡¼¤Î¥Ñ¥ï¡¼¤òÁÈ¤ß¹ç¤ï¤»¤ë ¤³¤È¤Ë¤è¤ê¡¢½¾Íè¤Î CGI
¥¢¥×¥í¡¼¥Á¤«¤é½ÀÆðÀ­¤È¥Ñ¥Õ¥©¡¼¥Þ¥ó¥¹¤òÂçÉý¤Ë¸þ¾å¤µ¤»¤Þ¤¹¡£

%description -l pl
mod_python jest modu³em osadzaj±cym interpreter jêzyka Python w
serwerze WWW Apache, umo¿liwiaj±c mu obs³ugê kodu napisanego w
Pythonie.

mod_python ³±czy wszechstronno¶æ Pythona i moc Apache'a jako serwera
WWW, co daje zwiêkszon± elastyczno¶æ i zauwa¿aln± poprawê wydajno¶ci w
stosunku do tradycyjnego rozwi±zania opartego na CGI.

%description -l sv
Mod_python är en modul som bygger in en interpretator för språket
Python i servern, och låter Apach-hanterare skrivas i Python.

Mod_python sammanför mångsidigheten hos Python och kraften hos
webbservern Apache till en avsevärd ökning av flexibiliteten och
prestandan jämfört med den traditionella CGI-metoden.

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
