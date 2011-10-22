#
# TODO:
#	- package cabal separately, same as alex and happy
#
%define		pkgname	haskell-platform
Summary:	Comprehensive, robust development environment for programming in Haskell
Name:		ghc-%{pkgname}
Version:	2011.2.0.1
Release:	5
License:	BSD
Group:		Development/Languages
#Source0:	http://hackage.haskell.org/platform/%{version}/%{pkgname}-%{version}.tar.gz
Source0:	http://lambda.galois.com/hp-tmp/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	97fd42f169a426d043368cec342745ef
# TEMP
Source100:	http://hackage.haskell.org/packages/archive/syb/0.3.3/syb-0.3.3.tar.gz
# Source100-md5:	4bc2ef44a86c9182f9768c6cc0a96c3a
Source101:	http://hackage.haskell.org/packages/archive/HTTP/4000.1.2/HTTP-4000.1.2.tar.gz
# Source101-md5:	0871666457aeabe4ed8ebce0acb424b7
Source102:	http://hackage.haskell.org/packages/archive/network/2.3.0.5/network-2.3.0.5.tar.gz
# Source102-md5:	716fbe9e01059582503d2920d2618ef3
Patch0:		%{name}-install.patch
Patch1:		%{name}-ghc72.patch
URL:		http://hackage.haskell.org/platform/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-prof
BuildRequires:	ghc-random
BuildRequires:	ghc-random-prof
BuildRequires:	zlib-devel
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
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
Provides:	ghc-syb
Provides:	ghc-text
Provides:	ghc-transformers
Provides:	ghc-xhtml
Provides:	ghc-zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# docs contai html files and haskell package definitions that should not be compressed
%define		no_install_post_compress_docs	1

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
%setup -q -n %{pkgname}-%{version} -a100 -a101 -a102
%patch0 -p1
%patch1 -p1

%{__rm} -r packages/syb-0.3 packages/HTTP-4000.1.1 packages/network-2.3.0.2
mv syb-0.3.3 HTTP-4000.1.2 network-2.3.0.5 packages/
%{__sed} -i -e 's|syb-0.3|syb-0.3.3|g' \
	-e 's|HTTP-4000.1.1|HTTP-4000.1.2|g' \
	-e 's|network-2.3.0.2|network-2.3.0.5|g' packages/platform.packages

%build

%configure \
	--enable-unsupported-ghc-version

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

%{__rm} $RPM_BUILD_ROOT%{_bindir}/{alex,happy}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*-tests
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
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString
%{_libdir}/%{ghcdir}/parsec-*/Text/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/*.hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString/*.hi
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
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding
%{_libdir}/%{ghcdir}/text-*/Data/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/IO/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/*.hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding/*.hi
%{_libdir}/%{ghcdir}/text-*/HStext-*.o
%{_libdir}/%{ghcdir}/text-*/libHStext-*.a
%dir %{_libdir}/%{ghcdir}/transformers-*
%dir %{_libdir}/%{ghcdir}/transformers-*/Control
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer
%dir %{_libdir}/%{ghcdir}/transformers-*/Data
%dir %{_libdir}/%{ghcdir}/transformers-*/Data/Functor
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer/*.hi
%{_libdir}/%{ghcdir}/transformers-*/Data/Functor/*.hi
%{_libdir}/%{ghcdir}/transformers-*/HStransformers-*.o
%{_libdir}/%{ghcdir}/transformers-*/libHStransformers-*.a

%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/cgi-*/libHScgi-*_p.a
%{_libdir}/%{ghcdir}/cgi-*/Network/CGI/*.p_hi
%{_libdir}/%{ghcdir}/cgi-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/deepseq-*/Control/*.p_hi
%{_libdir}/%{ghcdir}/deepseq-*/libHSdeepseq-*_p.a
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/libHSfgl-*_p.a
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-*_p.a
%{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell/*.p_hi
%{_libdir}/%{ghcdir}/haskell-src-*/libHShaskell-src-*_p.a
%{_libdir}/%{ghcdir}/html-*/libHShtml-*_p.a
%{_libdir}/%{ghcdir}/html-*/Text/Html/*.p_hi
%{_libdir}/%{ghcdir}/html-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/libHSHTTP-*_p.a
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.p_hi
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
%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-*_p.a
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
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/*.p_hi
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
