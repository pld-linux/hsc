Summary:	HTML Sucks Completely
Name:		hsc
Version:	0.917
Release:	0.2
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.aminet.net/text/hyper/%{name}-source.lha
Source1:	http://www.aminet.net/text/hyper/%{name}-ps.lha
Source2:	hsc-html-40.prefs
Patch0:		hsc-datadir.patch
BuildRequires:	lha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://www.giga.or.at/~agi/hsc/

%description
HSC is HTML preprocessor with syntax checking.

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
%{__make} all CC=gcc CFLAGS="$RPM_OPT_FLAGS" SYS=-DUNIX

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
%doc hsc/CHANGES hsc/COPYING hsc/IMPORTANT hsc/NEWS hsc/README hsc/docs
%doc hsc/docs-source hsc/examples hsc/grafflwerk hsc/hsc-html-40.prefs
%doc hsc/hsc.prefs hsc/hsc.ps hsc/readme hsc/starter-project
%attr(755,root,root) %{_bindir}/hsc
%attr(755,root,root) %{_bindir}/hscdepp
%attr(755,root,root) %{_bindir}/hscpitt
%attr(644,root,root) %{_datadir}/hsc.prefs
