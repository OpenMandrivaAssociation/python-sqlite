%define realname pysqlite

Name:		python-sqlite
Version:        1.0.1
Release:        10
License:	GPL
Group:		Development/Python
Summary:	Python bindings for sqlite
Source0:	%{realname}-%{version}.tar.bz2
Url:		https://pysqlite.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel sqlite-devel 
%description
This packages allows you to use sqlite with python.
sqliite is a simple database engine.

%prep
%setup -q -n %{realname}
rm -f doc/rest/.*swp
for i in examples doc; do
	find $i -name CVS -type d | xargs rm -Rf 
done;
sed -e 's///' -i examples/*.py
sed -e 's///' -i doc/rest/manual.txt 
%build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc  LICENSE README doc examples
%py_platsitedir/*




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-9mdv2010.0
+ Revision: 442490
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.1-8mdv2009.1
+ Revision: 319473
- rebuild with python 2.6

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2009.0
+ Revision: 259819
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 247655
- rebuild

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 139215
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-3mdv2007.0
+ Revision: 96485
- Rebuild against new python

* Wed Nov 15 2006 Lenny Cartier <lenny@mandriva.com> 1.0.1-2mdv2007.1
+ Revision: 84353
- Import python-sqlite

* Mon Apr 24 2006 Michael Scherer <misc@mandriva.org> 1.0.1-2mdk
- Use new python macro
- Use mkrel
- Correct rpmlint warning about encoding

* Fri Jan 21 2005 Michael Scherer <misc@mandrake.org> 1.0.1-1mdk
- New release 1.0.1

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.0-2mdk
- Rebuild for new python

* Fri Oct 15 2004 Michael Scherer <misc@mandrake.org> 1.0-1mdk
- New release 1.0

* Wed Aug 18 2004 Michael Scherer <misc@mandrake.org> 0.5.1-1mdk
- New release 0.5.1

* Wed Mar 24 2004 Michael Scherer <mscherer@mandrakesoft.com> 0.5.0-1mdk 
- First Mandrakesoft Package

