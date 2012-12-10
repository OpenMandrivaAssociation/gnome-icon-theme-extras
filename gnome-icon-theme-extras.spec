Summary: GNOME default extra icons
Name: gnome-icon-theme-extras
Version: 3.6.2
Release: %mkrel 1
License: CC-BY-SA
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
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
%makeinstall_std

%files
%doc README COPYING NEWS AUTHORS
%{_datadir}/icons/gnome/*x*
