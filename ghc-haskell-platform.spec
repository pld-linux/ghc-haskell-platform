#
# TODO:
#	- package cabal separately, same as alex and happy
#
%define		pkgname	haskell-platform
Summary:	Comprehensive, robust development environment for programming in Haskell
Name:		ghc-%{pkgname}
Version:	2013.2.0.0
Release:	3
License:	BSD
Group:		Development/Languages
Source0:	http://lambda.haskell.org/platform/download/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	36d02a889ad57a6345b167f5c7a6c164
Patch0:		%{name}-install.patch
URL:		http://hackage.haskell.org/platform/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	bash
BuildRequires:	ghc >= 7.6.2
BuildRequires:	ghc-prof
BuildRequires:	hscolour >= 1.8
BuildRequires:	zlib-devel
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
# http://www.haskell.org/platform/changelog.html
Provides:	ghc-GLUT = 2.4.0.0
Provides:	ghc-GLURaw = 1.3.0.0
Provides:	ghc-HTTP = 4000.2.8
Provides:	ghc-HUnit = 1.2.5.2
Provides:	ghc-OpenGL = 2.8.0.0
Provides:	ghc-OpenGLRaw = 1.3.0.0
Provides:	ghc-QuickCheck = 2.6
Provides:	ghc-async = 2.0.1.4
Provides:	ghc-attoparsec = 0.10.4.0
Provides:	ghc-case-insensitive = 1.0.0.1
Provides:	ghc-cgi = 3001.1.7.5
Provides:	ghc-fgl = 5.4.2.4
Provides:	ghc-hashable = 1.1.2.5
Provides:	ghc-haskell-src = 1.0.1.5
Provides:	ghc-html = 1.0.1.2
Provides:	ghc-mtl = 2.1.2
Provides:	ghc-network = 2.4.1.2
Provides:	ghc-parallel = 3.2.0.3
Provides:	ghc-parsec = 3.1.3
Provides:	ghc-random = 1.0.1.1
Provides:	ghc-regex-base = 0.93.2
Provides:	ghc-regex-compat = 0.95.1
Provides:	ghc-regex-posix = 0.95.2
Provides:	ghc-split = 0.2.2
Provides:	ghc-stm = 2.4.2
Provides:	ghc-syb = 0.4.0
Provides:	ghc-text = 0.11.3.1
Provides:	ghc-transformers = 0.3.0.0
Provides:	ghc-unordered-containers = 0.2.3.0
Provides:	ghc-vector = 0.10.0.1
Provides:	ghc-xhtml = 3000.2.1
Provides:	ghc-zlib = 0.5.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddoc files
%define		_noautocompressdoc	*.haddock

%description
The Haskell Platform is a comprehensive, robust development
environment for programming in Haskell. For new users the platform
makes it trivial to get up and running with a full Haskell
development environment. For experienced developers, the platform
provides a comprehensive, standard base for commercial and open
source Haskell development that maximises interoperability and
stability of your code.

%package prof
Summary:	Profiling haskell-platform libraries for GHC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	ghc-GLUT-prof = 2.4.0.0
Provides:	ghc-GLURaw-prof = 1.3.0.0
Provides:	ghc-HTTP-prof = 4000.2.8
Provides:	ghc-HUnit-prof = 1.2.5.2
Provides:	ghc-OpenGL-prof = 2.8.0.0
Provides:	ghc-OpenGLRaw-prof = 1.3.0.0
Provides:	ghc-QuickCheck-prof = 2.6
Provides:	ghc-async-prof = 2.0.1.4
Provides:	ghc-attoparsec-prof = 0.10.4.0
Provides:	ghc-case-insensitive-prof = 1.0.0.1
Provides:	ghc-cgi-prof = 3001.1.7.5
Provides:	ghc-fgl-prof = 5.4.2.4
Provides:	ghc-hashable-prof = 1.1.2.5
Provides:	ghc-haskell-src-prof = 1.0.1.5
Provides:	ghc-html-prof = 1.0.1.2
Provides:	ghc-mtl-prof = 2.1.2
Provides:	ghc-network-prof = 2.4.1.2
Provides:	ghc-parallel-prof = 3.2.0.3
Provides:	ghc-parsec-prof = 3.1.3
Provides:	ghc-random-prof = 1.0.1.1
Provides:	ghc-regex-base-prof = 0.93.2
Provides:	ghc-regex-compat-prof = 0.95.1
Provides:	ghc-regex-posix-prof = 0.95.2
Provides:	ghc-split-prof = 0.2.2
Provides:	ghc-stm-prof = 2.4.2
Provides:	ghc-syb-prof = 0.4.0
Provides:	ghc-text-prof = 0.11.3.1
Provides:	ghc-transformers-prof = 0.3.0.0
Provides:	ghc-unordered-containers-prof = 0.2.3.0
Provides:	ghc-vector-prof = 0.10.0.1
Provides:	ghc-xhtml-prof = 3000.2.1
Provides:	ghc-zlib-prof = 0.5.4.1

%description prof
Profiling haskell-platform libraries for Glorious Glasgow Haskell
Compilation System (GHC).
They should be installed when GHC's profiling subsystem is needed.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%{__sed} -i -e 's|/bin/sh|/bin/bash|' scripts/build.sh

%build
%configure
:>packages/installed.packages

%{__make} VERBOSE="-v2" \
	EXTRA_CONFIGURE_OPTS="-v2 \
		--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--libexecdir=%{_libexecdir} \
		--docdir=%{_docdir}/%{name}-%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d

%{__make} install VERBOSE="-v2" \
	ghcdir=%{ghcdir} \
	DESTDIR=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_bindir}/{alex,happy}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{alex,happy}*
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/HUnit*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%ghc_pkg_recache

%postun
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}-doc/html
%attr(755,root,root) %{_bindir}/cabal
%dir %{_libdir}/%{ghcdir}/mtl-*
%dir %{_libdir}/%{ghcdir}/mtl-*/Control
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Cont
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Cont/*.hi
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Error
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Error/*.hi
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad/RWS
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/RWS/*.hi
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Reader
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Reader/*.hi
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad/State
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/State/*.hi
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Writer
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Writer/*.hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/*.hi
%{_libdir}/%{ghcdir}/mtl-*/libHSmtl-*.a
%{_libdir}/%{ghcdir}/mtl-*/HSmtl-*.o
%dir %{_libdir}/%{ghcdir}/HUnit-*
%dir %{_libdir}/%{ghcdir}/HUnit-*/Test
%dir %{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit
%{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit/*.hi
%{_libdir}/%{ghcdir}/HUnit-*/Test/*.hi
%{_libdir}/%{ghcdir}/HUnit-*/libHSHUnit-*.a
%{_libdir}/%{ghcdir}/HUnit-*/HSHUnit-*.o
%dir %{_libdir}/%{ghcdir}/OpenGL-*
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/FramebufferObjects
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/QueryUtils
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Shaders
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/FramebufferObjects/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/QueryUtils/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Shaders/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-*.a
%{_libdir}/%{ghcdir}/OpenGL-*/HSOpenGL-*.o
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/Compatibility
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/Core31
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/EXT
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/NV
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/Compatibility/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/Core31/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/EXT/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/NV/*.hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/HSOpenGLRaw-*.o
%{_libdir}/%{ghcdir}/OpenGLRaw-*/libHSOpenGLRaw-*.a
%dir %{_libdir}/%{ghcdir}/GLURaw-*
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/Raw
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/*.hi
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/Raw/*.hi
%{_libdir}/%{ghcdir}/GLURaw-*/HSGLURaw-*.o
%{_libdir}/%{ghcdir}/GLURaw-*/libHSGLURaw-*.a
%dir %{_libdir}/%{ghcdir}/GLUT-*
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Raw
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Raw/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-*.a
%{_libdir}/%{ghcdir}/GLUT-*/HSGLUT-*.o
%dir %{_libdir}/%{ghcdir}/haskell-src-*
%dir %{_libdir}/%{ghcdir}/haskell-src-*/Language
%dir %{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell
%{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell/*.hi
%{_libdir}/%{ghcdir}/haskell-src-*/libHShaskell-src-*.a
%{_libdir}/%{ghcdir}/haskell-src-*/HShaskell-src-*.o
%dir %{_libdir}/%{ghcdir}/html-*
%dir %{_libdir}/%{ghcdir}/html-*/Text
%dir %{_libdir}/%{ghcdir}/html-*/Text/Html
%{_libdir}/%{ghcdir}/html-*/Text/Html/*.hi
%{_libdir}/%{ghcdir}/html-*/Text/*.hi
%{_libdir}/%{ghcdir}/html-*/libHShtml-*.a
%{_libdir}/%{ghcdir}/html-*/HShtml-*.o
%dir %{_libdir}/%{ghcdir}/QuickCheck-*
%dir %{_libdir}/%{ghcdir}/QuickCheck-*/Test
%dir %{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck/*.hi
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/*.hi
%{_libdir}/%{ghcdir}/QuickCheck-*/libHSQuickCheck-*.a
%{_libdir}/%{ghcdir}/QuickCheck-*/HSQuickCheck-*.o
%dir %{_libdir}/%{ghcdir}/fgl-*
%dir %{_libdir}/%{ghcdir}/fgl-*/Data
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal/*.hi
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad/*.hi
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query/*.hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/*.hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/*.hi
%{_libdir}/%{ghcdir}/fgl-*/libHSfgl-*.a
%{_libdir}/%{ghcdir}/fgl-*/HSfgl-*.o
%dir %{_libdir}/%{ghcdir}/parallel-*
%dir %{_libdir}/%{ghcdir}/parallel-*/Control
%dir %{_libdir}/%{ghcdir}/parallel-*/Control/Parallel
%{_libdir}/%{ghcdir}/parallel-*/Control/Parallel/*.hi
%{_libdir}/%{ghcdir}/parallel-*/Control/*.hi
%{_libdir}/%{ghcdir}/parallel-*/libHSparallel-*.a
%{_libdir}/%{ghcdir}/parallel-*/HSparallel-*.o
%dir %{_libdir}/%{ghcdir}/parsec-*
%dir %{_libdir}/%{ghcdir}/parsec-*/Text
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/Text
%{_libdir}/%{ghcdir}/parsec-*/Text/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/Text/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/*.hi
%{_libdir}/%{ghcdir}/parsec-*/libHSparsec-*.a
%{_libdir}/%{ghcdir}/parsec-*/HSparsec-*.o
%dir %{_libdir}/%{ghcdir}/network-*
%dir %{_libdir}/%{ghcdir}/network-*/include
%dir %{_libdir}/%{ghcdir}/network-*/include/HsNet.h
%dir %{_libdir}/%{ghcdir}/network-*/include/HsNetworkConfig.h
%dir %{_libdir}/%{ghcdir}/network-*/Network
%dir %{_libdir}/%{ghcdir}/network-*/Network/Socket
%dir %{_libdir}/%{ghcdir}/network-*/Network/Socket/ByteString
%{_libdir}/%{ghcdir}/network-*/Network/Socket/*.hi
%{_libdir}/%{ghcdir}/network-*/Network/Socket/ByteString/*.hi
%{_libdir}/%{ghcdir}/network-*/Network/*.hi
%{_libdir}/%{ghcdir}/network-*/*.hi
%{_libdir}/%{ghcdir}/network-*/libHSnetwork-*.a
%{_libdir}/%{ghcdir}/network-*/HSnetwork-*.o
%dir %{_libdir}/%{ghcdir}/HTTP-*
%dir %{_libdir}/%{ghcdir}/HTTP-*/Network
%dir %{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.hi
%{_libdir}/%{ghcdir}/HTTP-*/*.hi
%{_libdir}/%{ghcdir}/HTTP-*/libHSHTTP-*.a
%{_libdir}/%{ghcdir}/HTTP-*/HSHTTP-*.o
%dir %{_libdir}/%{ghcdir}/regex-base-*
%dir %{_libdir}/%{ghcdir}/regex-base-*/Text
%dir %{_libdir}/%{ghcdir}/regex-base-*/Text/Regex
%dir %{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base/*.hi
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/*.hi
%{_libdir}/%{ghcdir}/regex-base-*/libHSregex-base-*.a
%{_libdir}/%{ghcdir}/regex-base-*/HSregex-base-*.o
%dir %{_libdir}/%{ghcdir}/regex-posix-*
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString/*.hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/*.hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/*.hi
%{_libdir}/%{ghcdir}/regex-posix-*/libHSregex-posix-*.a
%{_libdir}/%{ghcdir}/regex-posix-*/HSregex-posix-*.o
%dir %{_libdir}/%{ghcdir}/regex-compat-*
%dir %{_libdir}/%{ghcdir}/regex-compat-*/Text
%{_libdir}/%{ghcdir}/regex-compat-*/Text/*.hi
%{_libdir}/%{ghcdir}/regex-compat-*/libHSregex-compat-*.a
%{_libdir}/%{ghcdir}/regex-compat-*/HSregex-compat-*.o
%dir %{_libdir}/%{ghcdir}/stm-*
%dir %{_libdir}/%{ghcdir}/stm-*/Control
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Concurrent
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM/*.hi
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/*.hi
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Monad
%{_libdir}/%{ghcdir}/stm-*/Control/Monad/*.hi
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Sequential
%{_libdir}/%{ghcdir}/stm-*/Control/Sequential/*.hi
%{_libdir}/%{ghcdir}/stm-*/libHSstm-*.a
%{_libdir}/%{ghcdir}/stm-*/HSstm-*.o
%dir %{_libdir}/%{ghcdir}/xhtml-*
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict/*.hi
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset/*.hi
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional/*.hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/*.hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/*.hi
%{_libdir}/%{ghcdir}/xhtml-*/libHSxhtml-*.a
%{_libdir}/%{ghcdir}/xhtml-*/HSxhtml-*.o
%dir %{_libdir}/%{ghcdir}/cgi-*
%dir %{_libdir}/%{ghcdir}/cgi-*/Network
%dir %{_libdir}/%{ghcdir}/cgi-*/Network/CGI
%{_libdir}/%{ghcdir}/cgi-*/Network/CGI/*.hi
%{_libdir}/%{ghcdir}/cgi-*/Network/*.hi
%{_libdir}/%{ghcdir}/cgi-*/libHScgi-*.a
%{_libdir}/%{ghcdir}/cgi-*/HScgi-*.o
%dir %{_libdir}/%{ghcdir}/zlib-*
%dir %{_libdir}/%{ghcdir}/zlib-*/Codec
%dir %{_libdir}/%{ghcdir}/zlib-*/Codec/Compression
%dir %{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib/*.hi
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/*.hi
%{_libdir}/%{ghcdir}/zlib-*/libHSzlib-*.a
%{_libdir}/%{ghcdir}/zlib-*/HSzlib-*.o
%exclude %{_libdir}/%{ghcdir}/*/*_p.a
%{_libdir}/%{ghcdir}/package.conf.d/*.conf
%dir %{_libdir}/%{ghcdir}/syb-*
%dir %{_libdir}/%{ghcdir}/syb-*/Data
%dir %{_libdir}/%{ghcdir}/syb-*/Data/Generics
%dir %{_libdir}/%{ghcdir}/syb-*/Generics
%dir %{_libdir}/%{ghcdir}/syb-*/Generics/SYB
%{_libdir}/%{ghcdir}/syb-*/Data/*.hi
%{_libdir}/%{ghcdir}/syb-*/Data/Generics/*.hi
%{_libdir}/%{ghcdir}/syb-*/Generics/*.hi
%{_libdir}/%{ghcdir}/syb-*/Generics/SYB/*.hi
%{_libdir}/%{ghcdir}/syb-*/HSsyb-*.o
%{_libdir}/%{ghcdir}/syb-*/libHSsyb-*.a
%dir %{_libdir}/%{ghcdir}/text-*
%dir %{_libdir}/%{ghcdir}/text-*/Data
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/IO
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/Int
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/RealFloat
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Unsafe
%{_libdir}/%{ghcdir}/text-*/Data/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/IO/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/Int/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/RealFloat/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Unsafe/*.hi
%{_libdir}/%{ghcdir}/text-*/HStext-*.o
%{_libdir}/%{ghcdir}/text-*/libHStext-*.a
%dir %{_libdir}/%{ghcdir}/transformers-*
%dir %{_libdir}/%{ghcdir}/transformers-*/Control
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Applicative
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer
%dir %{_libdir}/%{ghcdir}/transformers-*/Data
%dir %{_libdir}/%{ghcdir}/transformers-*/Data/Functor
%{_libdir}/%{ghcdir}/transformers-*/Control/Applicative/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Data/Functor/*.hi
%{_libdir}/%{ghcdir}/transformers-*/HStransformers-*.o
%{_libdir}/%{ghcdir}/transformers-*/libHStransformers-*.a
%dir %{_libdir}/%{ghcdir}/async-*
%dir %{_libdir}/%{ghcdir}/async-*/Control
%dir %{_libdir}/%{ghcdir}/async-*/Control/Concurrent
%{_libdir}/%{ghcdir}/async-*/Control/Concurrent/*.hi
%{_libdir}/%{ghcdir}/async-*/HSasync-*.o
%{_libdir}/%{ghcdir}/async-*/libHSasync-*.a
%dir %{_libdir}/%{ghcdir}/attoparsec-*
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/ByteString
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Internal
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Text
%{_libdir}/%{ghcdir}/attoparsec-*/Data/*.hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/*.hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/ByteString/*.hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Internal/*.hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Text/*.hi
%{_libdir}/%{ghcdir}/attoparsec-*/HSattoparsec-*.o
%{_libdir}/%{ghcdir}/attoparsec-*/libHSattoparsec-*.a
%dir %{_libdir}/%{ghcdir}/case-insensitive-*
%dir %{_libdir}/%{ghcdir}/case-insensitive-*/Data
%{_libdir}/%{ghcdir}/case-insensitive-*/Data/*.hi
%{_libdir}/%{ghcdir}/case-insensitive-*/HScase-insensitive-*.o
%{_libdir}/%{ghcdir}/case-insensitive-*/libHScase-insensitive-*.a
%dir %{_libdir}/%{ghcdir}/hashable-*
%dir %{_libdir}/%{ghcdir}/hashable-*/Data
%{_libdir}/%{ghcdir}/hashable-*/Data/*.hi
%{_libdir}/%{ghcdir}/hashable-*/HShashable-*.o
%{_libdir}/%{ghcdir}/hashable-*/libHShashable-*.a
%dir %{_libdir}/%{ghcdir}/primitive-*
%dir %{_libdir}/%{ghcdir}/primitive-*/Control
%dir %{_libdir}/%{ghcdir}/primitive-*/Control/Monad
%dir %{_libdir}/%{ghcdir}/primitive-*/Data
%dir %{_libdir}/%{ghcdir}/primitive-*/Data/Primitive
%dir %{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/Internal
%{_libdir}/%{ghcdir}/primitive-*/Control/Monad/*.hi
%{_libdir}/%{ghcdir}/primitive-*/Data/*.hi
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/*.hi
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/Internal/*.hi
%{_libdir}/%{ghcdir}/primitive-*/HSprimitive-*.o
%{_libdir}/%{ghcdir}/primitive-*/libHSprimitive-*.a
%dir %{_libdir}/%{ghcdir}/primitive-*/include
%{_libdir}/%{ghcdir}/primitive-*/include/primitive-memops.h
%{_libdir}/%{ghcdir}/random-*/System/*.hi
%dir %{_libdir}/%{ghcdir}/random-*
%dir %{_libdir}/%{ghcdir}/random-*/System
%{_libdir}/%{ghcdir}/random-*/HSrandom-*.o
%{_libdir}/%{ghcdir}/random-*/libHSrandom-*.a
%dir %{_libdir}/%{ghcdir}/split-*
%dir %{_libdir}/%{ghcdir}/split-*/Data
%dir %{_libdir}/%{ghcdir}/split-*/Data/List
%dir %{_libdir}/%{ghcdir}/split-*/Data/List/Split
%{_libdir}/%{ghcdir}/split-*/Data/List/*.hi
%{_libdir}/%{ghcdir}/split-*/Data/List/Split/*.hi
%{_libdir}/%{ghcdir}/split-*/HSsplit-*.o
%{_libdir}/%{ghcdir}/split-*/libHSsplit-*.a
%dir %{_libdir}/%{ghcdir}/unordered-containers-*
%dir %{_libdir}/%{ghcdir}/unordered-containers-*/Data
%dir %{_libdir}/%{ghcdir}/unordered-containers-*/Data/HashMap
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/*.hi
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/HashMap/*.hi
%{_libdir}/%{ghcdir}/unordered-containers-*/HSunordered-containers-*.o
%{_libdir}/%{ghcdir}/unordered-containers-*/libHSunordered-containers-*.a
%dir %{_libdir}/%{ghcdir}/vector-*
%dir %{_libdir}/%{ghcdir}/vector-*/Data
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/Stream
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Generic
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Internal
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Primitive
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Storable
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Unboxed
%{_libdir}/%{ghcdir}/vector-*/Data/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/Stream/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Generic/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Internal/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Primitive/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Storable/*.hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Unboxed/*.hi
%{_libdir}/%{ghcdir}/vector-*/HSvector-*.o
%{_libdir}/%{ghcdir}/vector-*/libHSvector-*.a
%dir %{_libdir}/%{ghcdir}/vector-*/include
%{_libdir}/%{ghcdir}/vector-*/include/vector.h

%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/cgi-*/libHScgi-*_p.a
%{_libdir}/%{ghcdir}/cgi-*/Network/CGI/*.p_hi
%{_libdir}/%{ghcdir}/cgi-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/libHSfgl-*_p.a
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Raw/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-*_p.a
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/*.p_hi
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/Raw/*.p_hi
%{_libdir}/%{ghcdir}/GLURaw-*/libHSGLURaw-*_p.a
%{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell/*.p_hi
%{_libdir}/%{ghcdir}/haskell-src-*/libHShaskell-src-*_p.a
%{_libdir}/%{ghcdir}/html-*/libHShtml-*_p.a
%{_libdir}/%{ghcdir}/html-*/Text/Html/*.p_hi
%{_libdir}/%{ghcdir}/html-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/libHSHTTP-*_p.a
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/*.p_hi
%{_libdir}/%{ghcdir}/HUnit-*/libHSHUnit-*_p.a
%{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit/*.p_hi
%{_libdir}/%{ghcdir}/HUnit-*/Test/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Cont/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Error/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Reader/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/RWS/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/State/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Writer/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/libHSmtl-*_p.a
%{_libdir}/%{ghcdir}/network-*/libHSnetwork-*_p.a
%{_libdir}/%{ghcdir}/network-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/network-*/Network/Socket/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/network-*/Network/Socket/*.p_hi
%{_libdir}/%{ghcdir}/network-*/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/FramebufferObjects/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/QueryUtils/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Shaders/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-*_p.a
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/Compatibility/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/Core31/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/EXT/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/NV/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/libHSOpenGLRaw-*_p.a
%{_libdir}/%{ghcdir}/parallel-*/Control/Parallel/*.p_hi
%{_libdir}/%{ghcdir}/parallel-*/Control/*.p_hi
%{_libdir}/%{ghcdir}/parallel-*/libHSparallel-*_p.a
%{_libdir}/%{ghcdir}/parsec-*/libHSparsec-*_p.a
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/QuickCheck-*/libHSQuickCheck-*_p.a
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/*.p_hi
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck/*.p_hi
%{_libdir}/%{ghcdir}/regex-base-*/libHSregex-base-*_p.a
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base/*.p_hi
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/*.p_hi
%{_libdir}/%{ghcdir}/regex-compat-*/libHSregex-compat-*_p.a
%{_libdir}/%{ghcdir}/regex-compat-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/libHSregex-posix-*_p.a
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Sequential/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/libHSstm-*_p.a
%{_libdir}/%{ghcdir}/syb-*/Data/Generics/*.p_hi
%{_libdir}/%{ghcdir}/syb-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/syb-*/Generics/*.p_hi
%{_libdir}/%{ghcdir}/syb-*/Generics/SYB/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/IO/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/RealFloat/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/Int/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Unsafe/*.p_hi
%{_libdir}/%{ghcdir}/text-*/libHStext-*_p.a
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Data/Functor/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/libHSxhtml-*_p.a
%{_libdir}/%{ghcdir}/xhtml-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional/*.p_hi
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/*.p_hi
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib/*.p_hi
%{_libdir}/%{ghcdir}/zlib-*/libHSzlib-*_p.a
%{_libdir}/%{ghcdir}/async-*/Control/Concurrent/*.p_hi
%{_libdir}/%{ghcdir}/async-*/libHSasync-*_p.a
%{_libdir}/%{ghcdir}/attoparsec-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Internal/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Text/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/libHSattoparsec-*_p.a
%{_libdir}/%{ghcdir}/case-insensitive-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/case-insensitive-*/libHScase-insensitive-*_p.a
%{_libdir}/%{ghcdir}/hashable-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/hashable-*/libHShashable-*_p.a
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/Text/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/Internal/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/libHSprimitive-*_p.a
%{_libdir}/%{ghcdir}/random-*/System/*.p_hi
%{_libdir}/%{ghcdir}/random-*/libHSrandom-*_p.a
%{_libdir}/%{ghcdir}/split-*/Data/List/*.p_hi
%{_libdir}/%{ghcdir}/split-*/Data/List/Split/*.p_hi
%{_libdir}/%{ghcdir}/split-*/libHSsplit-*_p.a
%{_libdir}/%{ghcdir}/syb-*/libHSsyb-*_p.a
%{_libdir}/%{ghcdir}/transformers-*/Control/Applicative/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/libHStransformers-*_p.a
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/HashMap/*.p_hi
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/unordered-containers-*/libHSunordered-containers-*_p.a
%{_libdir}/%{ghcdir}/vector-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/Stream/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Generic/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Internal/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Primitive/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Storable/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Unboxed/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/libHSvector-*_p.a
