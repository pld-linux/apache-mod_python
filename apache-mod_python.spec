%define		mod_name	python
%define		apxs		/usr/sbin/apxs
Summary:	An embedded Python interpreter for the Apache Web server
Summary(cs.UTF-8):	Vestavěný interpret Pythonu pro WWW server Apache
Summary(da.UTF-8):	En indbygget Python-fortolker for webtjeneren Apache
Summary(de.UTF-8):	Ein eingebetteter Python-Interpreter für den Apache Web-Server
Summary(es.UTF-8):	Intérprete Perl para el servidor Web Apache
Summary(fr.UTF-8):	Interpréteur Python intégré pour le serveur Web Apache
Summary(id.UTF-8):	Interpreter Perl untuk web server Apache
Summary(is.UTF-8):	Perl túlkur fyrir Apache vefþjóninn
Summary(it.UTF-8):	Interprete Python integrato per il server Web Apache
Summary(ja.UTF-8):	Apache Web サーバー用の組込み Perl インタープリタ
Summary(nb.UTF-8):	En Python-fortolker for webtjeneren Apache
Summary(pl.UTF-8):	Wbudowany interpreter języka Python dla serwera WWW Apache
Summary(pt.UTF-8):	Um interpretador de Perl embebido para o servidor Web Apache
Summary(ru.UTF-8):	Встроенный интерпретатор Perl для WWW-сервера Apache
Summary(sk.UTF-8):	Interpreter jazyka Perl pre webový server Apache
Summary(sl.UTF-8):	Vključeni pythonski tolmač za spletni strežnik Apache
Summary(sv.UTF-8):	En inbyggd Python-interpretator för webbservern Apache
Name:		apache-mod_%{mod_name}
Version:	3.3.1
Release:	20
License:	Apache
Group:		Networking/Daemons/HTTP
Source0:	http://www.apache.org/dist/httpd/modpython/mod_%{mod_name}-%{version}.tgz
# Source0-md5:	a3b0150176b726bd2833dac3a7837dc5
Source1:	%{name}.conf
Patch0:		%{name}-httpd-not-needed.patch
Patch1:		%{name}-ldflags.patch
Patch2:		%{name}-apr_brigade_sentinel.patch
Patch3:		%{name}-apache24.patch
URL:		http://www.modpython.org/
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

%define		apachelibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		apacheconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)/conf.d

%description
Mod_python is a module that embeds the Python language interpreter
within the server, allowing Apache handlers to be written in Python.

Mod_python brings together the versatility of Python and the power of
the Apache Web server for a considerable boost in flexibility and
performance over the traditional CGI approach.

%description -l cs.UTF-8
Balíček mod_python obsahuje modul, který umožní serveru Apache přímo
interpretovat CGI skripty napsané v jazyce Python. To vede k výraznému
zvýšení rychlosti jejich provedení.

%description -l de.UTF-8
Mod_python ist ein Modul, das den Python-Sprachinterpreter innerhalb
des Servers einbettet und es den Apache-Handlern ermöglicht, in Python
geschrieben zu werden.

Mod_python verbindet die Vielseitigkeit von Python und die
Leistungsstärke des Apache Web-Servers, was eine enorme Steigerung der
Flexibilität und Leistung gegenüber dem traditionellen CGI-Ansatz
bedeutet.

%description -l es.UTF-8
Mod_python es un módulo que activa el intérprete de Python en el
servidor, permitiendo que se escriban gestores para Apache en Python.

Mod_python proporciona la versatilidad y el poder del servidor web
Apache para acelerar considerablemente la flexibilidad y prestaciones
en comparación a una aproximación tradicional con CGI.

%description -l fr.UTF-8
Mod_python est un module qui intègre l'interpréteur de langage Python
dans le serveur, permettant aux gestionnaires Apache d'être écrits en
Python.

Mod_python conjugue la versatilité de Python et la puissance du
serveur Web Apache de façon à augmenter considérablement la
flexibilité et la performance par rapport à une approche CGI
traditionnelle.

%description -l it.UTF-8
Mod_python è un modulo che integra nel server l'interprete del
linguaggio Python, in modo che i programmi di gestione possano essere
scritti in Python.

Mod_python unisce in sé la versatilità di Python e la potenza del
server Web Apache, con un conseguente accrescimento di flessibilità e
un miglioramento notevole nelle prestazioni rispetto all'approccio
tradizionale CGI.

%description -l ja.UTF-8
Mod_python はサーバー内に Python
言語インタープリタを組み込んだモジュール です。これにより、Apache
ハンドラを Python で記述できます。 Mod_python は、Python の汎用性と
Apache Web サーバーのパワーを組み合わせる ことにより、従来の CGI
アプローチから柔軟性とパフォーマンスを大幅に向上させます。

%description -l pl.UTF-8
mod_python jest modułem osadzającym interpreter języka Python w
serwerze WWW Apache, umożliwiając mu obsługę kodu napisanego w
Pythonie.

mod_python łączy wszechstronność Pythona i moc Apache'a jako serwera
WWW, co daje zwiększoną elastyczność i zauważalną poprawę wydajności w
stosunku do tradycyjnego rozwiązania opartego na CGI.

%description -l sv.UTF-8
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
%{__aclocal}
%{__autoconf}
%configure \
	--with-apxs=%{apxs}
%{__make} dso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apachelibdir},%{apacheconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{apacheconfdir}/60_mod_python.conf
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q httpd restart

%postun
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc doc-html/* README COPYRIGHT NEWS CREDITS
%doc examples
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{apacheconfdir}/*_mod_%{mod_name}.conf
%attr(755,root,root) %{apachelibdir}/*.so
%dir %{py_sitedir}/mod_%{mod_name}
%if "%{py_ver}" > "2.4"
%{py_sitedir}/mod_%{mod_name}-*.egg-info
%endif
%attr(755,root,root) %{py_sitedir}/mod_%{mod_name}/*.so
%{py_sitedir}/mod_%{mod_name}/*.py[co]
