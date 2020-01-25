# TODO:
# - build
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
%bcond_without	tests		# don't build and run tests
%define		srcname		jaxen
Summary:	Jaxen
Name:		java-jaxen
Version:	1.1.1
Release:	0.1
License:	BSD-like
Group:		Libraries/Java
Source0:	http://dist.codehaus.org/jaxen/distributions/jaxen-%{version}-src.tar.gz
# Source0-md5:	b598ae6b7e765a92e13667b0a80392f4
URL:		http://jaxen.codehaus.org/
BuildRequires:	java-dom4j
BuildRequires:	jdk
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
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%package examples
Summary:	Examples for %{srcname}
Summary(pl.UTF-8):	Przykłady dla pakietu %{name}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Demonstrations and samples for %{srcname}.

%description examples -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

%build
CLASSPATH=$(build-classpath dom4j)
#export CLASSPATH
export JAVA_HOME="%{java_home}"

install -d build
#%javac -classpath $CLASSPATH -source 1.5 -target 1.5 -d build $(find -name '*.java')

%if %{with javadoc}
%javadoc -d apidocs \
	%{?with_java_sun:org.jaxen} \
	$(find src/java/main/org/jaxen/ -name '*.java')
%endif

%jar -cf %{srcname}-%{version}.jar -C build .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/%{srcname}.jar
%doc LICENSE.txt

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
