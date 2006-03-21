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
Summary(nb):	En Python-fortolker for webtjeneren Apache
Summary(pl):	Wbudowany interpreter jêzyka Python dla serwera WWW Apache
Summary(pt):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru):	÷ÓÔÒÏÅÎÎÙÊ ÉÎÔÅÒÐÒÅÔÁÔÏÒ Perl ÄÌÑ WWW-ÓÅÒ×ÅÒÁ Apache
Summary(sk):	Interpreter jazyka Perl pre webový server Apache
Summary(sl):	Vkljuèeni pythonski tolmaè za spletni stre¾nik Apache
Summary(sv):	En inbyggd Python-interpretator för webbservern Apache
Name:		apache-mod_%{mod_name}
Version:	3.2.8
Release:	1
License:	Apache Group License
Group:		Networking/Daemons
Source0:	http://www.apache.org/dist/httpd/modpython/mod_%{mod_name}-%{version}.tgz
# Source0-md5:	d03452979a6a334f73cc2b95b39db331
Source1:	%{name}.conf
Patch0:		%{name}-lib64.patch
Patch1:		%{name}-apr-status-is-success.patch
Patch2:		%{name}-httpd-not-needed.patch
Patch3:		%{name}-ldflags.patch
URL:		http://www.modpython.org/
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0.52-7
BuildRequires:	apr-devel >= 1:1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex >= 2.5.31
BuildRequires:	python
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache(modules-api) = %apache_modules_api
Requires:	apr >= 1:1.0.0
# apache.py uses pdb module
Requires:	python-devel-tools
%requires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

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
%if "%{_libdir}" == "%{_prefix}/lib64"
%patch0
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-apxs=%{apxs}
%{__make} dso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/httpd.conf}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/60_mod_python.conf
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q httpd restart

%preun
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc doc-html/* README COPYRIGHT NEWS CREDITS
%doc examples
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*.so
%dir %{py_sitedir}/mod_%{mod_name}
%attr(755,root,root) %{py_sitedir}/mod_%{mod_name}/*.so
%{py_sitedir}/mod_%{mod_name}/*.py[co]
