# TODO: webapps?
Summary:	phpIP Manager - Management of IP Addresses
Summary(pl):	phpIP Manager - zarz±dzanie adresami IP
Name:		phpIP
Version:	3.2
Release:	3
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

%define		_phpdir		%{_datadir}/%{name}
%define		_sysconfdir	/etc/%{name}

%description
phpIP Management is tool to manage IP addresses. It features
authentication for accessing the IP database, form validity checks,
and customizable searches.

%description -l pl
phpIP Management jest narzêdziem do zarz±dzania adresami IP. Ma
mo¿liwo¶æ uwierzytelniania przy dostêpie do bazy IP, sprawdzanie
poprawno¶ci danych w formularzach oraz konfigurowalne opcje szukania.

%prep
%setup -q -n phpip-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}/{img,includes,style} \
	   $RPM_BUILD_ROOT{%{_sysconfdir},/etc/httpd}

install *.php		$RPM_BUILD_ROOT%{_phpdir}
install includes/*.php	$RPM_BUILD_ROOT%{_phpdir}/includes
install style/*.css	$RPM_BUILD_ROOT%{_phpdir}/style
install img/*.gif	$RPM_BUILD_ROOT%{_phpdir}/img

cp includes/config_inc.php $RPM_BUILD_ROOT%{_sysconfdir}

ln -sf %{_sysconfdir}/config_inc.php $RPM_BUILD_ROOT%{_phpdir}/includes/config_inc.php

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf


%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- phpip
if [ -f %{_sysconfdir}/config_inc.php.rpmsave ]; then
	mv -f %{_sysconfdir}/config_inc.php.rpmsave %{_sysconfdir}/config_inc.php
fi

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO INSTALL sql/*
%dir %{_sysconfdir}
%dir %{_phpdir}
%dir %{_phpdir}/img
%dir %{_phpdir}/style
%dir %{_phpdir}/includes
%{_sysconfdir}/*.php
%{_phpdir}/*.php
%{_phpdir}/img/*.gif
%{_phpdir}/style/*.css
%config(noreplace) %verify(not md5 mtime size) %{_phpdir}/includes/config_inc.php
%{_phpdir}/includes/[!c]*.php

%attr(640,http,http) /etc/httpd/%{name}.conf
