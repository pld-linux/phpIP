Summary:	phpIP Manager - Management of IP Addresses
Summary(pl):	phpIP Manager - zarz±dzanie adresami IP
Name:		phpIP
Version:	2.2
Release:	1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	http://www.vermeer.org/projects/dl/%{name}-%{version}.tar.gz
URL:		http://www.vermeer.org/projects/
Requires:	mysql
Requires:	php-mysql >= 4.1.0
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	phpip

%define		_phpdir	/home/services/httpd/html/phpip

%description
phpIP Management is tool to manage IP addresses. It features
authentication for accessing the IP database, form validity checks,
and customizable searches.

%description -l pl
phpIP Management jest narzêdziem do zarz±dzania adresami IP. Posiada
mo¿liwo¶æ autentyfikacji przy dostêpie do bazy IP, sprawdzanie
poprawno¶ci danych w formularzach oraz konfigurowalne opcje szukania.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}/{img,includes,style}

install *.php		$RPM_BUILD_ROOT%{_phpdir}
install includes/*.php	$RPM_BUILD_ROOT%{_phpdir}/includes
install style/*.css	$RPM_BUILD_ROOT%{_phpdir}/style
install img/*.gif	$RPM_BUILD_ROOT%{_phpdir}/img

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- phpip
if [ -f /home/httpd/html/phpip/includes/config_inc.php.rpmsave ]; then
	mv -f /home/httpd/html/phpip/includes/config_inc.php.rpmsave %{_phpdir}/includes/config_inc.php

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO sql/*
%dir %{_phpdir}
%dir %{_phpdir}/img
%dir %{_phpdir}/style
%dir %{_phpdir}/includes
%{_phpdir}/*.php
%{_phpdir}/img/*.gif
%{_phpdir}/style/*.css
%config(noreplace) %verify(not md5 size mtime) %{_phpdir}/includes/config_inc.php
%{_phpdir}/includes/[!c]*.php
