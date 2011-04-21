%define upstream_name       Config-Model
%define upstream_version 1.235
%define _requires_exceptions perl(AptPkg::.*)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Framework for config validation and edition
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Carp::Assert::More)
BuildRequires: perl(Config::Tiny)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Probe::Perl)
BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Singleton)
BuildRequires: perl(MooseX::StrictConstructor)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(Test::Command)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Text::Template)
BuildRequires: perl(YAML::Any)
Requires: perl(Parse::RecDescent)
Requires: perl(Exception::Class)
Requires: perl(Carp::Assert::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}


%description
Using Config::Model, a typical configuration validation tool will be made
of 3 parts :

 - The user interface
 - The validation engine which is in charge of validating all the configuration
   information provided by the user.
 - The storage facility that store the configuration information

Config::Model provides a validation engine according to a set of rules.

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
%{_bindir}/config-edit*
%{perl_vendorlib}/Config
%{_mandir}/man1/*
%{_mandir}/man3/*
