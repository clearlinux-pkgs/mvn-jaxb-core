#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jaxb-core
Version  : 2.2.11
Release  : 1
URL      : https://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11-sources.jar
Source0  : https://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11-sources.jar
Source1  : https://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11.jar
Source2  : https://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.1 GPL-2.0
Requires: mvn-jaxb-core-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-jaxb-core package.
Group: Data

%description data
data components for the mvn-jaxb-core package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11-sources.jar
/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11.jar
/usr/share/java/.m2/repository/com/sun/xml/bind/jaxb-core/2.2.11/jaxb-core-2.2.11.pom
