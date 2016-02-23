%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name fill-range

Summary:       Fill in a range of numbers or letters
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.2.3
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/fill-range
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Fill in a range of numbers or letters, 
optionally passing an increment or multiplier to use.

%prep
%setup -q -n package
chmod 644 *

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.3-3
- rebuilt

* Wed Jan 13 2016 Tomas Hrcka <thrcka@redhat.com> - 2.2.3-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.2.3-1
- Initial package