# TODO:
# - package docs (not javadoc)
# - use source... ech... BR loops...
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_without	tests		# don't build and run tests
#
%include	/usr/lib/rpm/macros.java
#
%define		srcname		jaxen
Summary:	Jaxen
Name:		java-jaxen
Version:	1.1.1
Release:	0.1
License:	BSD-like
Group:		Libraries/Java
Source0:	http://dist.codehaus.org/jaxen/distributions/jaxen-%{version}.tar.gz
# Source0-md5:	6bb10007f84f65ac6db4d1794f3e9d63
URL:		http://jaxen.codehaus.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jaxen is an open source XPath library written in Java. It is adaptable
to many different object models, including DOM, XOM, dom4j, and JDOM.
Is it also possible to write adapters that treat non-XML trees such as
compiled Java byte code or Java beans as XML, thus enabling you to
query these trees with XPath too.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%package examples
Summary:	Examples for %{name}
Summary(pl.UTF-8):	Przykłady dla pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Demonstrations and samples for %{srcname}.

%description examples -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -a %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
%doc LICENSE.txt

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
