%include	/usr/lib/rpm/macros.python
%define		mod_name	python
Summary:	A Python for the Apache Web server
Summary(pl):	Python dla serwera WWW Apache
Name:		apache-mod_%{mod_name}
Version:	2.7.6
Release:	4
License:	distributable
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(es):	Red/Servidores
Group(fr):	Réseau/Serveurs
Group(pl):	Sieciowe/Serwery
Group(pt):	Rede/Server
Source0:	http://www.modpython.org/dist/mod_%{mod_name}-%{version}.tgz
Patch0:		apache-mod_python-shared.patch
Patch1:		apache-mod_python-DESTDIR.patch
URL:		http://www.modpython.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	apache
BuildRequires:	apache-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
Requires:	apache
%requires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apache_moddir	%(/usr/sbin/apxs -q LIBEXECDIR)

%description
mod_python allows embedding Python within the Apache Web server for a
considerable boost in performance and added flexibility in designing
web based applications.

%description -l pl
mod_python pozwala na zagnie¿d¿enie pythona w serwerze WWW Apache w
celu zauwa¿alnej poprawy wydajno¶ci i zwiêkszonej elastyczno¶ci przy
tworzeniu aplikacji opartych na WWW.

%prep 
%setup -q -n mod_%{mod_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf

# new apache needs it
CFLAGS="-DEAPI %{rpmcflags}"
%configure \
	--with-apxs=/usr/sbin/apxs
 
%{__make} dso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apache_moddir},%{py_sitedir}/mod_%{mod_name}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README COPYRIGHT NEWS CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/apxs -e -a -n %{mod_name} %{apache_moddir}/mod_%{mod_name}.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	/etc/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n %{mod_name} %{apache_moddir}/mod_%{mod_name}.so 1>&2
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
