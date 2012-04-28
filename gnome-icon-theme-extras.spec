Summary: GNOME default extra icons
Name: gnome-icon-theme-extras
Version: 3.4.0
Release: %mkrel 1
License: CC-BY-SA
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: icon-naming-utils >= 0.8.1
BuildRequires: git-core
#BuildRequires: inkscape
BuildArch: noarch
Requires: gnome-icon-theme
Requires(post): gtk+2.0
Requires(postun): gtk+2.0

%description
GNOME default extra icons

%prep
%setup -q

%build

./configure --prefix=%_prefix --enable-icon-mapping

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING NEWS AUTHORS
%{_datadir}/icons/gnome/*x*
