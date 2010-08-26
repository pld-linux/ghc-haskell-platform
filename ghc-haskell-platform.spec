%define	pkgname	haskell-platform
Summary:	Comprehensive, robust development environment for programming in Haskell
Name:		ghc-%{pkgname}
Version:	2010.2.0.0
Release:	0.1
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/platform/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	9d1dd22a86bf2505591e6375f7dbe18e
URL:		http://hackage.haskell.org/platform/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	ghc >= 6.12.3
BuildRequires:	zlib-devel
%requires_eq	ghc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libsubdir	ghc-%(/usr/bin/ghc --numeric-version)/%{pkgname}-%{version}

%description
The Haskell Platform is a comprehensive, robust development
environment for programming in Haskell. For new users the platform
makes it trivial to get up and running with a full Haskell
development environment. For experienced developers, the platform
provides a comprehensive, standard base for commercial and open
source Haskell development that maximises interoperability and
stability of your code.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
rm -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc

runhaskell Setup.hs register \
	--gen-pkg-config=$RPM_BUILD_ROOT/%{_libdir}/%{libsubdir}/%{pkgname}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/ghc-pkg update %{_libdir}/%{libsubdir}/%{pkgname}.conf

%postun
if [ "$1" = "0" ]; then
	/usr/bin/ghc-pkg unregister %{pkgname}-%{version}
fi

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}-doc/html
%{_libdir}/%{libsubdir}
