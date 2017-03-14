%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name fill-range

Summary:       Fill in a range of numbers or letters
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.2.3
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/fill-range
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch

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
%doc LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.3-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.3-3
- Rebuilt with updated metapackage

* Wed Jan 13 2016 Tomas Hrcka <thrcka@redhat.com> - 2.2.3-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.2.3-1
- Initial package
