%include	/usr/lib/rpm/macros.python
%define		mod_name	python
%define 	apxs		/usr/sbin/apxs
%define		beta	BETA4
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
Version:	3.0.0
Release:	0.2
License:	distributable
Group:		Networking/Daemons
Source0: http://www.apache.org/dist/httpd/modpython/dev/mod_%{mod_name}-%{version}-%{beta}.tgz
Source1:        apache-mod_python-3.conf
#Patch0:		%{name}-shared.patch
##Patch1:		%{name}-DESTDIR.patch
#Patch2:		%{name}-Makefile-in.patch
#Patch3:		%{name}-cleanup.patch
# PLD keeps static libs in /usr/lib default python install stores them in .../config/
Patch1: 	%{name}-3-static-lib-dir-fix.patch
Patch2:		%{name}-3-DESTDIR.patch

URL:		http://www.modpython.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	apache-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:  python-static >= 2.2
BuildRequires:	rpm-pythonprov
BuildRequires:	%{apxs}
Prereq:		%{_sbindir}/apxs
Requires:	apache
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apache_moddir	%(%{apxs} -q LIBEXECDIR)
%define         apache_confdir	%(%{apxs} -q SYSCONFDIR)/httpd.conf

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
%setup -q -n mod_%{mod_name}-%{version}-%{beta}
# Patch reverted. Dynamic build makes apache segfault on all my i686 machines
# No working reports collected on IRC/mailing lists.
#%patch0 -p1
%patch1 -p0
%patch2 -p0
#%patch3 -p1
#%patch4 -p1

%build
%{__aclocal}
%{__autoconf}


# new apache needs it
CFLAGS="-DEAPI %{rpmcflags}"
%configure \
	--with-apxs=%{apxs}

%{__make} dso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apache_moddir},%{apache_confdir},%{py_sitedir}/mod_%{mod_name}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{apache_confdir}/66_mod_python.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post 
if [ -f /var/lock/subsys/httpd ]; then
        /etc/rc.d/init.d/httpd restart 1>&2
else
   echo "Run \"/etc/rc.d/init.d/httpd start\" to start apache http daemon."
fi

%preun 
if [ "$1" = "0" ]; then
        if [ -f /var/lock/subsys/httpd ]; then
                /etc/rc.d/init.d/httpd restart 1>&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc doc-html/*
%doc README COPYRIGHT NEWS CREDITS
%attr(755,root,root) %{apache_moddir}/*
%{py_sitedir}/mod_%{mod_name}
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/httpd.conf/*_mod_python.conf
