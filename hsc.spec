Summary:	HTML Sucks Completely
Summary(pl):	HTML Ssie Ca³kowicie
Name:		hsc
Version:	0.917
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://www.aminet.net/text/hyper/%{name}-source.lha
# Source0-md5:	c7efe30e58ff02b7da08d1e26561b7b3
Source1:	http://www.aminet.net/text/hyper/%{name}-ps.lha
# Source1-md5:	4b74015060a3dafe1e0dde132ab5ae0f
Source2:	hsc-html-40.prefs
Patch0:		hsc-datadir.patch
URL:		http://www.giga.or.at/~agi/hsc/
BuildRequires:	lha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautocompressdoc	*.hsc *.prefs

%description
HSC is HTML preprocessor with syntax checking.

%description -l pl
HSC to preprocesor HTML z kontrol± sk³adni.

%prep
%setup -qcT
lha -xq2f %{SOURCE0}
cd hsc
lha -xq2f %{SOURCE1}
cp %{SOURCE2} .
%patch0 -p1

%build
%{__make} all -C hsc/source \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags}" \
	SYS=-DUNIX

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/misc}

%{__make} install -C hsc/source \
	INSTALL=install \
	INSTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc hsc/{CHANGES,IMPORTANT,NEWS,README,hsc.ps,readme,hsc-html-40.prefs,hsc.prefs}
%doc hsc/{docs,docs-source,examples,grafflwerk,starter-project}
%attr(755,root,root) %{_bindir}/hsc
%attr(755,root,root) %{_bindir}/hscdepp
%attr(755,root,root) %{_bindir}/hscpitt
%{_datadir}/misc/hsc.prefs
