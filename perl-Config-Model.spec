%define upstream_name    Config-Model
%define upstream_version 2.041

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Framework for config validation and edition
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-Model-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(AnyEvent)
BuildRequires:	perl(Carp::Assert::More)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(Hash::Merge) >= 0.120.0
BuildRequires:	perl(IO::File)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Log::Log4perl) >= 1.110.0
BuildRequires:	perl(Module::Build) >= 0.340.0
BuildRequires:	perl(Mouse)
BuildRequires:	perl(MouseX::NativeTraits)
BuildRequires:	perl(MouseX::StrictConstructor)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Pod::POM)
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Term::ReadLine)
BuildRequires:	perl(Test::Command) >= 0.80.0
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::File::Contents)
BuildRequires:	perl(Test::Memory::Cycle)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn) >= 0.110.0
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(YAML::Any) >= 0.303.0
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

Requires:	perl(Parse::RecDescent)
Requires:	perl(Exception::Class)
Requires:	perl(Carp::Assert::More)

%description
Config::Model provides a validation engine according to a set of rules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Build.PL installdirs=vendor
./Build

#%check
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc  LICENSE META.yml MODELS MYMETA.yml  TODO examples
%{_bindir}/cme
%{_bindir}/config-edit*
%{perl_vendorlib}/Config
%{_mandir}/man1/*
%{_mandir}/man3/*



