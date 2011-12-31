Name:		qwt
Summary:	Qt Widgets for Technical Applications
Version:	5.1.1
Release:	4.1%{?dist}
BuildRequires:	qt4-devel
URL:		http://qwt.sourceforge.net
License:	LGPLv2 with exceptions
Group:          System Environment/Libraries
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		qwt-path.patch
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} > 4
%define epel5mode 1
%else
%define epel5mode 0
%endif

%package devel
Summary:        Development and doc files for %{name}
Requires:       %{name} = %{version}-%{release} qt4-devel
Group:          Development/Libraries

%description
The Qwt library contains GUI Components and utility classes which are primarily
useful for programs with a technical background.
Besides a 2D plot widget it provides scales, sliders, dials, compasses,
thermometers, wheels and knobs to control or display values, arrays
or ranges of type double.

%description devel
Contains the development files.

%prep
%setup -qn %{name}-%{version}
%patch0 -p1
sed -i "s\LIBPATH\ $RPM_BUILD_ROOT%{_libdir}\1" qwtconfig.pri
sed -i "s\HEADERPATH\ $RPM_BUILD_ROOT%{_includedir}/%{name}\1" qwtconfig.pri
sed -i "s\DOCKPATH\ $RPM_BUILD_ROOT%{_docdir}/%{name}\1" qwtconfig.pri
#sed -i "s\QTDESIGNERPATH\ $RPM_BUILD_ROOT%{_qt4_plugindir}/designer\1" designer/designer.pro
sed -i "s\QTDESIGNERPATH\ $RPM_BUILD_ROOT%{_libdir}/qt4/plugins/designer\1" designer/designer.pro

%build
%if %{epel5mode}
%{_libdir}/qt4/bin/qmake
%else
qmake-qt4
%endif
#parallel build fails sometime so I disable it
make

%install
rm -rf $RPM_BUILD_ROOT
make install
#remove unneeded stuff
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES
%doc COPYING
%doc README
%{_libdir}/libqwt.so.5
%{_libdir}/libqwt.so.5.1
%{_libdir}/libqwt.so.5.1.1

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/libqwt.so
#%{_qt4_plugindir}/designer/libqwt_designer_plugin.so
%{_libdir}/qt4/plugins/designer/libqwt_designer_plugin.so

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 5.1.1-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 04 2009 Frank Büttner <frank-buettner@gmx.net> - 5.1.1-2
 - modify path patch

* Sun Jan 04 2009 Frank Büttner <frank-buettner@gmx.net> - 5.1.1-1
 -update to 5.1.1

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0.2-6
- Autorebuild for GCC 4.3

* Sat Sep 29 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-5
 - add EPEL support
* Sat Sep 29 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-4
 - remove parallel build, because it will fail sometimes
* Fri Sep 28 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-3
 - fix some errors in the spec file
* Fri Jul 06 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-2
 - fix some errors in the spec file
* Mon Jun 11 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.2-1
 - update to 5.0.2
 - split doc
* Thu May 15 2007 Frank Büttner <frank-buettner@gmx.net> - 5.0.1-1
 - start
