%define		mod_name	python
Summary:	A Python for the Apache Web server
Name:		apache-mod_%{mod_name}
Version:	2.6.4
Release:	1
License:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:	        http://www.modpython.org/dist/mod_%{mod_name}-%{version}.tgz
Patch0:		apache-mod_python-shared.patch
Patch1:		apache-mod_python-DESTDIR.patch
URL:		http://www.modpython.org/
Requires:	apache
Requires:	python 
BuildRequires:	apache
BuildRequires:	apache-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	apache_moddir  %(/usr/sbin/apxs -q LIBEXECDIR)
%define python_prefix  %(echo `python -c "import sys; print sys.prefix"`)
%define python_version %(echo `python -c "import sys; print sys.version[:3]"`)
%define python_libdir      %{python_prefix}/lib/python%{python_version}
%define python_includedir  %{python_prefix}/include/python%{python_version}
%define python_sitedir     %{python_libdir}/site-packages

%description
mod_python allows embedding Python within the Apache Web server 
for a considerable boost in performance and added flexibility 
in designing web based applications. 

NOTE: This versions should still be considered Beta

%prep 
%setup -q -n mod_%{mod_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
autoconf
%{configure} --with-apxs=/usr/sbin/apxs
%{__make} dso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{apache_moddir},%{python_sitedir}/mod_%{mod_name}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README COPYRIGHT NEWS CREDITS

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%doc {README,COPYRIGHT,NEWS,CREDITS}.gz
%attr(755,root,root) %{apache_moddir}/*
%{python_sitedir}/mod_%{mod_name}
