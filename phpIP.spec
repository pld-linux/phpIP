Summary:	phpIP Manager - Management of IP Addresses
Summary(pl.UTF-8):	phpIP Manager - zarządzanie adresami IP
Name:		phpIP
Version:	3.2
Release:	4
License:	GPL v2
Group:		Applications/Databases/Interfaces
#Source0Download: http://www.vermeer.org/projects/phpip/
Source0:	http://www.vermeer.org/projects/dl/phpip-%{version}.tar.gz
# Source0-md5:	34d615fc899de321a0062c099f3b28d1
Source1:	%{name}.conf
URL:		http://www.vermeer.org/projects/phpip/
Requires:	mysql
Requires:	php(mysql)
Requires:	php-common >= 3:4.1.0
Requires:	webserver
Obsoletes:	phpip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
phpIP Management is tool to manage IP addresses. It features
authentication for accessing the IP database, form validity checks,
and customizable searches.

%description -l pl.UTF-8
phpIP Management jest narzędziem do zarządzania adresami IP. Ma
możliwość uwierzytelniania przy dostępie do bazy IP, sprawdzanie
poprawności danych w formularzach oraz konfigurowalne opcje szukania.

%prep
%setup -q -n phpip-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir}/{img,includes,style},%{_sysconfdir}}

install *.php		$RPM_BUILD_ROOT%{_appdir}
install includes/*.php	$RPM_BUILD_ROOT%{_appdir}/includes
install style/*.css	$RPM_BUILD_ROOT%{_appdir}/style
install img/*.gif	$RPM_BUILD_ROOT%{_appdir}/img
install includes/config_inc.php $RPM_BUILD_ROOT%{_sysconfdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO INSTALL sql/*
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/config_inc.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%dir %{_appdir}
%dir %{_appdir}/img
%dir %{_appdir}/style
%dir %{_appdir}/includes
%{_appdir}/*.php
%{_appdir}/img/*.gif
%{_appdir}/style/*.css
%{_appdir}/includes/[!c]*.php
