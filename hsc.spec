Summary:	HTML Sucks Completely
Summary(pl):	HTML Ssie Ca³kowicie
Name:		hsc
Version:	0.917
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://www.aminet.net/text/hyper/%{name}-source.lha
Source1:	http://www.aminet.net/text/hyper/%{name}-ps.lha
Source2:	hsc-html-40.prefs
Patch0:		hsc-datadir.patch
BuildRequires:	lha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://www.giga.or.at/~agi/hsc/

%define         _noautocompressdoc	*.hsc *.prefs

%description
HSC is HTML preprocessor with syntax checking.

%description -l pl
HSC to preprocesor HTML z kontrol± sk³adni.

%prep
cd %{_builddir}
rm -rf hsc
lha -xq2f %{SOURCE0}
cd hsc
lha -xq2f %{SOURCE1}
cp %{SOURCE2} .
%patch0 -p1

%build
cd hsc/source
%{__make} all CC=%{__cc} CFLAGS="%{rpmcflags}" SYS=-DUNIX

%install
rm -rf $RPM_BUILD_ROOT

cd hsc/source
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
%{__make} install INSTALL=install INSTDIR=$RPM_BUILD_ROOT%{_prefix}/

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file_id.diz $RPM_BUILD_DIR/hsc

%files
%defattr(644,root,root,755)
%doc hsc/CHANGES hsc/IMPORTANT hsc/NEWS hsc/README hsc/docs
%doc hsc/docs-source hsc/examples hsc/grafflwerk hsc/hsc-html-40.prefs
%doc hsc/hsc.prefs hsc/hsc.ps hsc/readme hsc/starter-project
%attr(755,root,root) %{_bindir}/hsc
%attr(755,root,root) %{_bindir}/hscdepp
%attr(755,root,root) %{_bindir}/hscpitt
%attr(644,root,root) %{_datadir}/hsc.prefs
