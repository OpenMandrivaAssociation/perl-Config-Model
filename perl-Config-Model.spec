%define upstream_name       Config-Model
%define upstream_version    0.636

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Framework for config validation and edition
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Using Config::Model, a typical configuration validation tool will be made
of 3 parts :

* 1

  The user interface

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog LICENSE
%{_bindir}/config-edit
%{perl_vendorlib}/Config
%{_mandir}/man1/config-edit.1*
%{_mandir}/man3/*

