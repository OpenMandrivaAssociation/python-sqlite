%define realname pysqlite

Name:		python-sqlite
Version:        1.0.1
Release:        %mkrel 3
License:	GPL
Group:		Development/Python
Summary:	Python bindings for sqlite
Source0:    %{realname}-%{version}.tar.bz2
Url:		http://pysqlite.sourceforge.net/
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
sed -e 's///' -i examples/*.py
sed -e 's///' -i doc/rest/manual.txt 
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


