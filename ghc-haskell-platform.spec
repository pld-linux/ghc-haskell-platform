%define	pkgname	haskell-platform
Summary:	Comprehensive, robust development environment for programming in Haskell
Name:		ghc-%{pkgname}
Version:	2010.2.0.0
Release:	4
License:	BSD
Group:		Development/Languages
Source0:	http://hackage.haskell.org/platform/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	9d1dd22a86bf2505591e6375f7dbe18e
Patch0:		%{name}-install.patch
URL:		http://hackage.haskell.org/platform/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-prof
BuildRequires:	zlib-devel
%requires_releq	ghc
Provides:	ghc-GLUT
Provides:	ghc-HTTP
Provides:	ghc-HUnit
Provides:	ghc-OpenGL
Provides:	ghc-QuickCheck
Provides:	ghc-cgi
Provides:	ghc-deepseq
Provides:	ghc-fgl
Provides:	ghc-haskell-platform
Provides:	ghc-haskell-src
Provides:	ghc-html
Provides:	ghc-mtl
Provides:	ghc-network
Provides:	ghc-parallel
Provides:	ghc-parsec
Provides:	ghc-regex-base
Provides:	ghc-regex-compat
Provides:	ghc-regex-posix
Provides:	ghc-stm
Provides:	ghc-xhtml
Provides:	ghc-zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ghcdir		ghc-%(/usr/bin/ghc --numeric-version)

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

%description prof
Profiling haskell-platform libraries for Glorious Glasgow Haskell
Compilation System (GHC).
They should be installed when GHC's profiling subsystem is needed.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
%configure 

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

# apparently there is no documentation O.o
# work around automatic haddock docs installation
#rm -rf %{name}-%{version}-doc
#cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc

rm $RPM_BUILD_ROOT%{_bindir}/{alex,cabal,happy,*-tests}
rm -r $RPM_BUILD_ROOT%{_datadir}/{alex,happy,HUnit}*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/ghc-pkg recache

%postun
/usr/bin/ghc-pkg recache

%files
%defattr(644,root,root,755)
#doc %{name}-%{version}-doc/html
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
%dir %{_libdir}/%{ghcdir}/OpenGL-*/include
%dir %{_libdir}/%{ghcdir}/OpenGL-*/include/HsOpenGL.h
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/*.hi
%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-*.a
%{_libdir}/%{ghcdir}/OpenGL-*/HSOpenGL-*.o
%dir %{_libdir}/%{ghcdir}/GLUT-*
%dir %{_libdir}/%{ghcdir}/GLUT-*/include
%dir %{_libdir}/%{ghcdir}/GLUT-*/include/HsGLUT.h
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.hi
%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-*.a
%{_libdir}/%{ghcdir}/GLUT-*/HSGLUT-*.o
%dir %{_libdir}/%{ghcdir}/deepseq-*
%dir %{_libdir}/%{ghcdir}/deepseq-*/Control
%{_libdir}/%{ghcdir}/deepseq-*/Control/*.hi
%{_libdir}/%{ghcdir}/deepseq-*/libHSdeepseq-*.a
%{_libdir}/%{ghcdir}/deepseq-*/HSdeepseq-*.o
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
%{_libdir}/%{ghcdir}/network-*/Network/Socket/*.hi
%{_libdir}/%{ghcdir}/network-*/Network/*.hi
%{_libdir}/%{ghcdir}/network-*/*.hi
%{_libdir}/%{ghcdir}/network-*/libHSnetwork-*.a
%{_libdir}/%{ghcdir}/network-*/HSnetwork-*.o
%dir %{_libdir}/%{ghcdir}/HTTP-*
%dir %{_libdir}/%{ghcdir}/HTTP-*/Network
%dir %{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.hi
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

%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Cont/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Error/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/RWS/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Reader/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/State/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Writer/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/libHSmtl-*_p.a
%{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit/*.p_hi
%{_libdir}/%{ghcdir}/HUnit-*/Test/*.p_hi
%{_libdir}/%{ghcdir}/HUnit-*/libHSHUnit-*_p.a
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-*_p.a
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.p_hi
%{_libdir}/%{ghcdir}/deepseq-*/Control/*.p_hi
%{_libdir}/%{ghcdir}/deepseq-*/libHSdeepseq-*_p.a
%{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell/*.p_hi
%{_libdir}/%{ghcdir}/haskell-src-*/libHShaskell-src-*_p.a
%{_libdir}/%{ghcdir}/html-*/Text/Html/*.p_hi
%{_libdir}/%{ghcdir}/html-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/html-*/libHShtml-*_p.a
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck/*.p_hi
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/*.p_hi
%{_libdir}/%{ghcdir}/QuickCheck-*/libHSQuickCheck-*_p.a
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/libHSfgl-*_p.a
%{_libdir}/%{ghcdir}/parallel-*/Control/Parallel/*.p_hi
%{_libdir}/%{ghcdir}/parallel-*/Control/*.p_hi
%{_libdir}/%{ghcdir}/parallel-*/libHSparallel-*_p.a
%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-*_p.a
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/libHSparsec-*_p.a
%{_libdir}/%{ghcdir}/network-*/Network/Socket/*.p_hi
%{_libdir}/%{ghcdir}/network-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/network-*/*.p_hi
%{_libdir}/%{ghcdir}/network-*/libHSnetwork-*_p.a
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/libHSHTTP-*_p.a
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base/*.p_hi
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/*.p_hi
%{_libdir}/%{ghcdir}/regex-base-*/libHSregex-base-*_p.a
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/libHSregex-posix-*_p.a
%{_libdir}/%{ghcdir}/regex-compat-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/regex-compat-*/libHSregex-compat-*_p.a
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Sequential/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/libHSstm-*_p.a
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/libHSxhtml-*_p.a
%{_libdir}/%{ghcdir}/cgi-*/Network/CGI/*.p_hi
%{_libdir}/%{ghcdir}/cgi-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/cgi-*/libHScgi-*_p.a
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib/*.p_hi
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/*.p_hi
%{_libdir}/%{ghcdir}/zlib-*/libHSzlib-*_p.a
