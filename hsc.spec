Summary: HTML Sucks Completely
Name: hsc
Version: 0.916
Release: 1
Copyright: GPL
Group: Applications/Publishing
Source0: http://www.aminet.net/text/hyper/hsc-source.lha
Source1: http://www.aminet.net/text/hyper/hsc-ps.lha
BuildRoot: /tmp/%{name}-%{version}-root
URL: http://www.giga.or.at/~agi/hsc/

%description
HSC is HTML preprocessor with syntax checking.

%changelog

* Sat Aug 15 1998 Robert Richard George 'reptile' Wal <reptile@reptile.eu.org>

- Initial realease.

%prep

rm -rf hsc
lha -xf $RPM_SOURCE_DIR/hsc-source.lha
cd hsc
lha -xf $RPM_SOURCE_DIR/hsc-ps.lha

%build

cd hsc/source
make all CC=gcc CFLAGS='-s -O2' SYS=-DUNIX

%install

rm -rf $RPM_BUILD_ROOT

cd hsc/source
install -d -m 755 $RPM_BUILD_ROOT/usr/lib
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
make install INSTALL=install INSTDIR=$RPM_BUILD_ROOT/usr/

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file_id.diz $RPM_BUILD_DIR/hsc

%files
%defattr(-,root,root)
%doc hsc/CHANGES hsc/COPYING hsc/IMPORTANT hsc/NEWS hsc/README hsc/docs
%doc hsc/docs-source hsc/examples hsc/grafflwerk hsc/hsc-html-40.prefs
%doc hsc/hsc.prefs hsc/hsc.ps hsc/readme hsc/starter-project
/usr/bin/hsc
/usr/bin/hscdepp
/usr/bin/hscpitt
/usr/lib/hsc.prefs
