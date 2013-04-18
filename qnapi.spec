%define		prel	rc2

Summary:	Subtitle Downloader
Name:		qnapi
Version:	0.1.6
Release:	0.%{prel}.2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/qnapi/%{name}-%{version}-%{prel}.tar.gz
# Source0-md5:	84daa5dea51e8612bda26bdc4361ea62
URL:		http://krzemin.iglu.cz/qnapi/
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt-build
BuildRequires:	qt-qmake
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	p7zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QNapi is free, Qt4-based application designed for automatically
downloading and matching subtitles for your movie files. It uses
NapiProjekt (http://www.napiprojekt.pl) and OpenSubtitles
(http://www.opensubtitles.com) databases.

%prep
%setup -qn %{name}-%{version}-%{prel}

%build
qmake -o Makefile %{name}.pro
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -p qnapi $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/apps/{22x22,32x32,48x48,128x128}
#cp -p res/%{name}-128.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/apps/128x128/qnapi.png
#cp -p res/%{name}-32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/apps/32x32/qnapi.png
#cp -p res/%{name}-48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/apps/48x48/qnapi.png
#cp -p res/%{name}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/apps/22x22/qnapi.png

install -d $RPM_BUILD_ROOT%{_desktopdir}
#cp -p doc/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ChangeLog doc/README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
#%{_iconsdir}/hicolor/apps/*/qnapi.png
#%{_desktopdir}/%{name}.desktop

