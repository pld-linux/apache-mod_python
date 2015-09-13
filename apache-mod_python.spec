# TODO:
#	1) make mod_python3 use it's own set of config directives
#	2) test if both flavors can be loaded at the same time
#	3) after 1 and 2 are done, drop conflicts
#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module

%define		mod_name	python
%define		apxs		/usr/sbin/apxs
Summary:	An embedded Python interpreter for the Apache Web server
Summary(cs.UTF-8):	Vestavěný interpret Pythonu pro WWW server Apache
Summary(de.UTF-8):	Ein eingebetteter Python-Interpreter für den Apache Web-Server
Summary(es.UTF-8):	Intérprete Python para el servidor Web Apache
Summary(fr.UTF-8):	Interpréteur Python intégré pour le serveur Web Apache
Summary(it.UTF-8):	Interprete Python integrato per il server Web Apache
Summary(ja.UTF-8):	Apache Web サーバー用の組込み Python インタープリタ
Summary(pl.UTF-8):	Wbudowany interpreter języka Python dla serwera WWW Apache
Summary(sv.UTF-8):	En inbyggd Python-interpretator för webbservern Apache
Name:		apache-mod_%{mod_name}
Version:	3.5.0
Release:	15
License:	Apache
Group:		Networking/Daemons/HTTP
Source0:	http://dist.modpython.org/dist/mod_%{mod_name}-%{version}.tgz
# Source0-md5:	2e61621e8d030f535f112d8e739161e2
Source1:	%{name}.conf
Source2:	%{name}3.conf
Patch0:		%{name}-httpd-not-needed.patch
Patch1:		no-git.patch
Patch2:		set-request-response-status.patch
URL:		http://www.modpython.org/
BuildRequires:	apache-devel >= 2.0.52-7
BuildRequires:	apr-devel >= 1:1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex >= 2.5.31
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.671
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-devel >= 2.6
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-devel >= 3.3
%endif
Requires(post,preun,postun):	systemd-units >= 38
Requires:	rc-scripts
Requires:	apache(modules-api) = %apache_modules_api
Requires:	apr >= 1:1.0.0
# apache.py uses pdb module
Requires:	python-devel-tools
%requires_eq	python-libs
Requires:	systemd-units >= 38
Conflicts:	apache-mod_python3
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

%package -n apache-mod_python3
Summary:	An embedded Python 3 interpreter for the Apache Web server
Summary(cs.UTF-8):	Vestavěný interpret Pythonu 3 pro WWW server Apache
Summary(de.UTF-8):	Ein eingebetteter Python3-Interpreter für den Apache Web-Server
Summary(es.UTF-8):	Intérprete Python 3 para el servidor Web Apache
Summary(fr.UTF-8):	Interpréteur Python 3 intégré pour le serveur Web Apache
Summary(it.UTF-8):	Interprete Python 3 integrato per il server Web Apache
Summary(ja.UTF-8):	Apache Web サーバー用の組込み Python 3 インタープリタ
Summary(pl.UTF-8):	Wbudowany interpreter języka Python 3 dla serwera WWW Apache
Summary(sv.UTF-8):	En inbyggd Python3-interpretator för webbservern Apache
Group:		Networking/Daemons/HTTP
Requires(post,preun,postun):	systemd-units >= 38
Requires:	rc-scripts
Requires:	apache(modules-api) = %apache_modules_api
Requires:	apr >= 1:1.0.0
# apache.py uses pdb module
Requires:	python3-devel-tools
%requires_eq	python3-libs
Requires:	systemd-units >= 38
Conflicts:	apache-mod_python

%description -n apache-mod_python3
mod_python3 is a module that embeds the Python 3 language interpreter
within the server, allowing Apache handlers to be written in Python 3.

mod_python3 brings together the versatility of Python 3 and the power
of the Apache Web server for a considerable boost in flexibility and
performance over the traditional CGI approach.

%description -n apache-mod_python3 -l cs.UTF-8
Balíček mod_python3 obsahuje modul, který umožní serveru Apache přímo
interpretovat CGI skripty napsané v jazyce Python 3. To vede k
výraznému zvýšení rychlosti jejich provedení.

%description -n apache-mod_python3 -l de.UTF-8
mod_python3 ist ein Modul, das den Python3-Sprachinterpreter innerhalb
des Servers einbettet und es den Apache-Handlern ermöglicht,
in Python 3 geschrieben zu werden.

mod_python3 verbindet die Vielseitigkeit von Python 3 und die
Leistungsstärke des Apache Web-Servers, was eine enorme Steigerung der
Flexibilität und Leistung gegenüber dem traditionellen CGI-Ansatz
bedeutet.

%description -n apache-mod_python3 -l es.UTF-8
mod_python3 es un módulo que activa el intérprete de Python 3 en el
servidor, permitiendo que se escriban gestores para Apache en
Python 3.

mod_python3 proporciona la versatilidad y el poder del servidor web
Apache para acelerar considerablemente la flexibilidad y prestaciones
en comparación a una aproximación tradicional con CGI.

%description -n apache-mod_python3 -l fr.UTF-8
mod_python3 est un module qui intègre l'interpréteur de langage
Python 3 dans le serveur, permettant aux gestionnaires Apache d'être
écrits en Python 3.

mod_python3 conjugue la versatilité de Python 3 et la puissance du
serveur Web Apache de façon à augmenter considérablement la
flexibilité et la performance par rapport à une approche CGI
traditionnelle.

%description -n apache-mod_python3 -l it.UTF-8
mod_python3 è un modulo che integra nel server l'interprete del
linguaggio Python 3, in modo che i programmi di gestione possano
essere scritti in Python 3.

mod_python3 unisce in sé la versatilità di Python 3 e la potenza del
server Web Apache, con un conseguente accrescimento di flessibilità e
un miglioramento notevole nelle prestazioni rispetto all'approccio
tradizionale CGI.

%description -n apache-mod_python3 -l ja.UTF-8
mod_python3 はサーバー内に Python 3
言語インタープリタを組み込んだモジュール です。これにより、Apache
ハンドラを Python 3 で記述できます。 mod_python3 は、Python 3 
の汎用性と Apache Web サーバーのパワーを組み合わせる ことにより、
従来の CGI アプローチから柔軟性とパフォーマンスを大幅に向上させます。

%description -n apache-mod_python3 -l pl.UTF-8
mod_python3 jest modułem osadzającym interpreter języka Python 3 w
serwerze WWW Apache, umożliwiając mu obsługę kodu napisanego w
Pythonie 3.

mod_python3 łączy wszechstronność Pythona 3 i moc Apache'a jako
serwera WWW, co daje zwiększoną elastyczność i zauważalną poprawę
wydajności w stosunku do tradycyjnego rozwiązania opartego na CGI.

%description -n apache-mod_python3 -l sv.UTF-8
mod_python3 är en modul som bygger in en interpretator för språket
Python 3 i servern, och låter Apach-hanterare skrivas i Python 3.

mod_python3 sammanför mångsidigheten hos Python 3 och kraften hos
webbservern Apache till en avsevärd ökning av flexibiliteten och
prestandan jämfört med den traditionella CGI-metoden.

%prep
%setup -q -n mod_%{mod_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}

%if %{with python2}
%configure \
	--with-apxs=%{apxs} \
	--with-python=%{__python}

%{__make} clean
%{__make} dso
install -d apache-mod_python{%{apachelibdir},%{apacheconfdir},%{_bindir}}
%{__make} install \
	DESTDIR=`pwd`/apache-mod_python
%endif

%if %{with python3}
%configure \
	--with-apxs=%{apxs} \
	--with-python=%{__python3}

%{__make} clean
%{__make} dso
install -d apache-mod_python3{%{apachelibdir},%{apacheconfdir},%{_bindir}}
%{__make} install \
	DESTDIR=`pwd`/apache-mod_python3
%{__mv} apache-mod_python3%{_bindir}/mod_python{,3}
%{__mv} apache-mod_python3%{apachelibdir}/mod_python{,3}.so
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apachelibdir},%{apacheconfdir},%{_bindir}}

%if %{with python2}
cp -a apache-mod_python/* $RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{apacheconfdir}/60_mod_python.conf
%endif

%if %{with python3}
cp -a apache-mod_python3/* $RPM_BUILD_ROOT
install %{SOURCE2} $RPM_BUILD_ROOT%{apacheconfdir}/60_mod_python3.conf
%endif

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q httpd restart
%systemd_service_restart httpd.service

%postun
if [ "$1" = "0" ]; then
	%service -q httpd restart
	%systemd_service_restart httpd.service
fi

%post -n apache-mod_python3
%service -q httpd restart
%systemd_service_restart httpd.service

%postun -n apache-mod_python3
if [ "$1" = "0" ]; then
	%service -q httpd restart
	%systemd_service_restart httpd.service
fi

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc doc-html/* README.md COPYRIGHT NEWS CREDITS
%doc examples
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{apacheconfdir}/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_bindir}/mod_python
%attr(755,root,root) %{apachelibdir}/mod_python.so
%dir %{py_sitedir}/mod_%{mod_name}
%{py_sitedir}/mod_%{mod_name}-*.egg-info
%attr(755,root,root) %{py_sitedir}/mod_%{mod_name}/*.so
%{py_sitedir}/mod_%{mod_name}/*.py[co]
%endif

%if %{with python3}
%files -n apache-mod_python3
%defattr(644,root,root,755)
%doc doc-html/* README.md COPYRIGHT NEWS CREDITS
%doc examples
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{apacheconfdir}/*_mod_%{mod_name}3.conf
%attr(755,root,root) %{_bindir}/mod_python3
%attr(755,root,root) %{apachelibdir}/mod_python3.so
%dir %{py3_sitedir}/mod_%{mod_name}
%{py3_sitedir}/mod_%{mod_name}-*.egg-info
%attr(755,root,root) %{py3_sitedir}/mod_%{mod_name}/*.so
%{py3_sitedir}/mod_%{mod_name}/__pycache__
%{py3_sitedir}/mod_%{mod_name}/*.py
%endif
