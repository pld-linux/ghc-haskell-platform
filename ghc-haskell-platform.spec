#
# TODO:
#	- package cabal separately, same as alex and happy
#
%define		pkgname	haskell-platform

# included ghc package versions, http://www.haskell.org/platform/changelog.html
%define		gpv_GLURaw			1.3.0.0
%define		gpv_GLUT			2.4.0.0
%define		gpv_HTTP			4000.2.8
%define		gpv_HUnit			1.2.5.2
%define		gpv_OpenGL			2.8.0.0
%define		gpv_OpenGLRaw			1.3.0.0
%define		gpv_QuickCheck			2.6
%define		gpv_async			2.0.1.4
%define		gpv_attoparsec			0.10.4.0
%define		gpv_case_insensitive		1.0.0.1
%define		gpv_cgi				3001.1.7.5
%define		gpv_fgl				5.4.2.4
%define		gpv_hashable			1.1.2.5
%define		gpv_haskell_src			1.0.1.5
%define		gpv_html			1.0.1.2
%define		gpv_mtl				2.1.2
%define		gpv_network			2.4.1.2
%define		gpv_parallel			3.2.0.3
%define		gpv_parsec			3.1.3
%define		gpv_primitive			0.5.0.1
%define		gpv_random			1.0.1.1
%define		gpv_regex_base			0.93.2
%define		gpv_regex_compat		0.95.1
%define		gpv_regex_posix			0.95.2
%define		gpv_split			0.2.2
%define		gpv_stm				2.4.2
%define		gpv_syb				0.4.0
%define		gpv_text			0.11.3.1
%define		gpv_transformers		0.3.0.0
%define		gpv_unordered_containers	0.2.3.0
%define		gpv_vector			0.10.0.1
%define		gpv_xhtml			3000.2.1
%define		gpv_zlib			0.5.4.1

Summary:	Comprehensive, robust development environment for programming in Haskell
Summary(pl.UTF-8):	Obszerne, bogate środowisko programistyczne dla Haskella
Name:		ghc-%{pkgname}
Version:	2013.2.0.0
Release:	4
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
BuildRequires:	ghc-prof >= 7.6.2
BuildRequires:	hscolour >= 1.8
BuildRequires:	zlib-devel
BuildRequires:	rpmbuild(macros) >= 1.608
%requires_eq	ghc
Provides:	ghc-GLURaw = %{gpv_GLURaw}
Provides:	ghc-GLUT = %{gpv_GLUT}
Provides:	ghc-HTTP = %{gpv_HTTP}
Provides:	ghc-HUnit = %{gpv_HUnit}
Provides:	ghc-OpenGL = %{gpv_OpenGL}
Provides:	ghc-OpenGLRaw = %{gpv_OpenGLRaw}
Provides:	ghc-QuickCheck = %{gpv_QuickCheck}
Provides:	ghc-async = %{gpv_async}
Provides:	ghc-attoparsec = %{gpv_attoparsec}
Provides:	ghc-case-insensitive = %{gpv_case_insensitive}
Provides:	ghc-cgi = %{gpv_cgi}
Provides:	ghc-fgl = %{gpv_fgl}
Provides:	ghc-hashable = %{gpv_hashable}
Provides:	ghc-haskell-src = %{gpv_haskell_src}
Provides:	ghc-html = %{gpv_html}
Provides:	ghc-mtl = %{gpv_mtl}
Provides:	ghc-network = %{gpv_network}
Provides:	ghc-parallel = %{gpv_parallel}
Provides:	ghc-parsec = %{gpv_parsec}
Provides:	ghc-primitive = %{gpv_primitive}
Provides:	ghc-random = %{gpv_random}
Provides:	ghc-regex-base = %{gpv_regex_base}
Provides:	ghc-regex-compat = %{gpv_regex_compat}
Provides:	ghc-regex-posix = %{gpv_regex_posix}
Provides:	ghc-split = %{gpv_split}
Provides:	ghc-stm = %{gpv_stm}
Provides:	ghc-syb = %{gpv_syb}
Provides:	ghc-text = %{gpv_text}
Provides:	ghc-transformers = %{gpv_transformers}
Provides:	ghc-unordered-containers = %{gpv_unordered_containers}
Provides:	ghc-vector = %{gpv_vector}
Provides:	ghc-xhtml = %{gpv_xhtml}
Provides:	ghc-zlib = %{gpv_zlib}
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

%description -l pl.UTF-8
Haskell Platform to obszerne, bogate środowisko programistyczne dla
Haskella. Nowym użytkownikom platforma ułatwia rozpoczęcie pracy z
pełnym środowiskiem programistycznym Haskella. Doświadczonym
użytkownikom zapewnia obszerną podstawę do komercyjnego lub otwartego
programowania w Haskellu, maksymalizując przenośność i stabilność
kodu.

%package prof
Summary:	Profiling haskell-platform libraries for GHC
Summary(pl.UTF-8):	Biblioteki profilujące haskell-platform dla GHC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	ghc-GLURaw-prof = %{gpv_GLURaw}
Provides:	ghc-GLUT-prof = %{gpv_GLUT}
Provides:	ghc-HTTP-prof = %{gpv_HTTP}
Provides:	ghc-HUnit-prof = %{gpv_HUnit}
Provides:	ghc-OpenGL-prof = %{gpv_OpenGL}
Provides:	ghc-OpenGLRaw-prof = %{gpv_OpenGLRaw}
Provides:	ghc-QuickCheck-prof = %{gpv_QuickCheck}
Provides:	ghc-async-prof = %{gpv_async}
Provides:	ghc-attoparsec-prof = %{gpv_attoparsec}
Provides:	ghc-case-insensitive-prof = %{gpv_case_insensitive}
Provides:	ghc-cgi-prof = %{gpv_cgi}
Provides:	ghc-fgl-prof = %{gpv_fgl}
Provides:	ghc-hashable-prof = %{gpv_hashable}
Provides:	ghc-haskell-src-prof = %{gpv_haskell_src}
Provides:	ghc-html-prof = %{gpv_html}
Provides:	ghc-mtl-prof = %{gpv_mtl}
Provides:	ghc-network-prof = %{gpv_network}
Provides:	ghc-parallel-prof = %{gpv_parallel}
Provides:	ghc-parsec-prof = %{gpv_parsec}
Provides:	ghc-primitive-prof = %{gpv_primitive}
Provides:	ghc-random-prof = %{gpv_random}
Provides:	ghc-regex-base-prof = %{gpv_regex_base}
Provides:	ghc-regex-compat-prof = %{gpv_regex_compat}
Provides:	ghc-regex-posix-prof = %{gpv_regex_posix}
Provides:	ghc-split-prof = %{gpv_split}
Provides:	ghc-stm-prof = %{gpv_stm}
Provides:	ghc-syb-prof = %{gpv_syb}
Provides:	ghc-text-prof = %{gpv_text}
Provides:	ghc-transformers-prof = %{gpv_transformers}
Provides:	ghc-unordered-containers-prof = %{gpv_unordered_containers}
Provides:	ghc-vector-prof = %{gpv_vector}
Provides:	ghc-xhtml-prof = %{gpv_xhtml}
Provides:	ghc-zlib-prof = %{gpv_zlib}

%description prof
Profiling haskell-platform libraries for Glorious Glasgow Haskell
Compilation System (GHC). They should be installed when GHC's
profiling subsystem is needed.

%description prof -l pl.UTF-8
Biblioteki profilujące haskell-platform dla systemu GHC (Glorious
Glasgow Haskell Compilation System). Powinny być zainstalowane, jeśli
potrzebny jest system profilujący GHC.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%{__sed} -i -e 's|/bin/sh|/bin/bash|' scripts/build.sh

%build
%configure
:>packages/installed.packages

%{__make} \
	VERBOSE="-v2" \
	EXTRA_CONFIGURE_OPTS="-v2 \
		--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--libexecdir=%{_libexecdir} \
		--docdir=%{_docdir}/%{name}-%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d

%{__make} install \
	VERBOSE="-v2" \
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

%dir %{_libdir}/%{ghcdir}/GLURaw-*
%{_libdir}/%{ghcdir}/GLURaw-*/HSGLURaw-%{gpv_GLURaw}.o
%{_libdir}/%{ghcdir}/GLURaw-*/libHSGLURaw-%{gpv_GLURaw}.a
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/*.hi
%dir %{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/Raw
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/Raw/*.hi

%dir %{_libdir}/%{ghcdir}/GLUT-*
%{_libdir}/%{ghcdir}/GLUT-*/HSGLUT-%{gpv_GLUT}.o
%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-%{gpv_GLUT}.a
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.hi
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.hi
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.hi
%dir %{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Raw
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Raw/*.hi

%dir %{_libdir}/%{ghcdir}/HTTP-*
%{_libdir}/%{ghcdir}/HTTP-*/HSHTTP-%{gpv_HTTP}.o
%{_libdir}/%{ghcdir}/HTTP-*/libHSHTTP-%{gpv_HTTP}.a
%{_libdir}/%{ghcdir}/HTTP-*/*.hi
%dir %{_libdir}/%{ghcdir}/HTTP-*/Network
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.hi
%dir %{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.hi

%dir %{_libdir}/%{ghcdir}/HUnit-*
%{_libdir}/%{ghcdir}/HUnit-*/HSHUnit-%{gpv_HUnit}.o
%{_libdir}/%{ghcdir}/HUnit-*/libHSHUnit-%{gpv_HUnit}.a
%dir %{_libdir}/%{ghcdir}/HUnit-*/Test
%{_libdir}/%{ghcdir}/HUnit-*/Test/*.hi
%dir %{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit
%{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit/*.hi

%dir %{_libdir}/%{ghcdir}/OpenGL-*
%{_libdir}/%{ghcdir}/OpenGL-*/HSOpenGL-%{gpv_OpenGL}.o
%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-%{gpv_OpenGL}.a
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/FramebufferObjects
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/FramebufferObjects/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/QueryUtils
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/QueryUtils/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Shaders
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Shaders/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU/*.hi

%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*
%{_libdir}/%{ghcdir}/OpenGLRaw-*/HSOpenGLRaw-%{gpv_OpenGLRaw}.o
%{_libdir}/%{ghcdir}/OpenGLRaw-*/libHSOpenGLRaw-%{gpv_OpenGLRaw}.a
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/Compatibility
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/Compatibility/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/Core31
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/Core31/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/EXT
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/EXT/*.hi
%dir %{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/NV
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/NV/*.hi

%dir %{_libdir}/%{ghcdir}/QuickCheck-*
%{_libdir}/%{ghcdir}/QuickCheck-*/HSQuickCheck-%{gpv_QuickCheck}.o
%{_libdir}/%{ghcdir}/QuickCheck-*/libHSQuickCheck-%{gpv_QuickCheck}.a
%dir %{_libdir}/%{ghcdir}/QuickCheck-*/Test
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/*.hi
%dir %{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck/*.hi

%dir %{_libdir}/%{ghcdir}/async-*
%{_libdir}/%{ghcdir}/async-*/HSasync-%{gpv_async}.o
%{_libdir}/%{ghcdir}/async-*/libHSasync-%{gpv_async}.a
%dir %{_libdir}/%{ghcdir}/async-*/Control
%dir %{_libdir}/%{ghcdir}/async-*/Control/Concurrent
%{_libdir}/%{ghcdir}/async-*/Control/Concurrent/*.hi

%dir %{_libdir}/%{ghcdir}/attoparsec-*
%{_libdir}/%{ghcdir}/attoparsec-*/HSattoparsec-%{gpv_attoparsec}.o
%{_libdir}/%{ghcdir}/attoparsec-*/libHSattoparsec-%{gpv_attoparsec}.a
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data
%{_libdir}/%{ghcdir}/attoparsec-*/Data/*.hi
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/*.hi
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/ByteString
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/ByteString/*.hi
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Internal
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Internal/*.hi
%dir %{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Text
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Text/*.hi

%dir %{_libdir}/%{ghcdir}/case-insensitive-*
%{_libdir}/%{ghcdir}/case-insensitive-*/HScase-insensitive-%{gpv_case_insensitive}.o
%{_libdir}/%{ghcdir}/case-insensitive-*/libHScase-insensitive-%{gpv_case_insensitive}.a
%dir %{_libdir}/%{ghcdir}/case-insensitive-*/Data
%{_libdir}/%{ghcdir}/case-insensitive-*/Data/*.hi

%dir %{_libdir}/%{ghcdir}/cgi-*
%{_libdir}/%{ghcdir}/cgi-*/HScgi-%{gpv_cgi}.o
%{_libdir}/%{ghcdir}/cgi-*/libHScgi-%{gpv_cgi}.a
%dir %{_libdir}/%{ghcdir}/cgi-*/Network
%{_libdir}/%{ghcdir}/cgi-*/Network/*.hi
%dir %{_libdir}/%{ghcdir}/cgi-*/Network/CGI
%{_libdir}/%{ghcdir}/cgi-*/Network/CGI/*.hi

%dir %{_libdir}/%{ghcdir}/fgl-*
%{_libdir}/%{ghcdir}/fgl-*/HSfgl-%{gpv_fgl}.o
%{_libdir}/%{ghcdir}/fgl-*/libHSfgl-%{gpv_fgl}.a
%dir %{_libdir}/%{ghcdir}/fgl-*/Data
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/*.hi
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/*.hi
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal/*.hi
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad/*.hi
%dir %{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query/*.hi

%dir %{_libdir}/%{ghcdir}/hashable-*
%{_libdir}/%{ghcdir}/hashable-*/HShashable-%{gpv_hashable}.o
%{_libdir}/%{ghcdir}/hashable-*/libHShashable-%{gpv_hashable}.a
%dir %{_libdir}/%{ghcdir}/hashable-*/Data
%{_libdir}/%{ghcdir}/hashable-*/Data/*.hi

%dir %{_libdir}/%{ghcdir}/haskell-src-*
%{_libdir}/%{ghcdir}/haskell-src-*/HShaskell-src-%{gpv_haskell_src}.o
%{_libdir}/%{ghcdir}/haskell-src-*/libHShaskell-src-%{gpv_haskell_src}.a
%dir %{_libdir}/%{ghcdir}/haskell-src-*/Language
%dir %{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell
%{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell/*.hi

%dir %{_libdir}/%{ghcdir}/html-*
%{_libdir}/%{ghcdir}/html-*/HShtml-%{gpv_html}.o
%{_libdir}/%{ghcdir}/html-*/libHShtml-%{gpv_html}.a
%dir %{_libdir}/%{ghcdir}/html-*/Text
%{_libdir}/%{ghcdir}/html-*/Text/*.hi
%dir %{_libdir}/%{ghcdir}/html-*/Text/Html
%{_libdir}/%{ghcdir}/html-*/Text/Html/*.hi

%dir %{_libdir}/%{ghcdir}/mtl-*
%{_libdir}/%{ghcdir}/mtl-*/HSmtl-%{gpv_mtl}.o
%{_libdir}/%{ghcdir}/mtl-*/libHSmtl-%{gpv_mtl}.a
%dir %{_libdir}/%{ghcdir}/mtl-*/Control
%dir %{_libdir}/%{ghcdir}/mtl-*/Control/Monad
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/*.hi
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

%dir %{_libdir}/%{ghcdir}/network-*
%{_libdir}/%{ghcdir}/network-*/HSnetwork-%{gpv_network}.o
%{_libdir}/%{ghcdir}/network-*/libHSnetwork-%{gpv_network}.a
%{_libdir}/%{ghcdir}/network-*/include
%dir %{_libdir}/%{ghcdir}/network-*/Network
%{_libdir}/%{ghcdir}/network-*/Network/*.hi
%dir %{_libdir}/%{ghcdir}/network-*/Network/Socket
%{_libdir}/%{ghcdir}/network-*/Network/Socket/*.hi
%dir %{_libdir}/%{ghcdir}/network-*/Network/Socket/ByteString
%{_libdir}/%{ghcdir}/network-*/Network/Socket/ByteString/*.hi
%{_libdir}/%{ghcdir}/network-*/*.hi

%dir %{_libdir}/%{ghcdir}/parallel-*
%{_libdir}/%{ghcdir}/parallel-*/HSparallel-%{gpv_parallel}.o
%{_libdir}/%{ghcdir}/parallel-*/libHSparallel-%{gpv_parallel}.a
%dir %{_libdir}/%{ghcdir}/parallel-*/Control
%{_libdir}/%{ghcdir}/parallel-*/Control/*.hi
%dir %{_libdir}/%{ghcdir}/parallel-*/Control/Parallel
%{_libdir}/%{ghcdir}/parallel-*/Control/Parallel/*.hi

%dir %{_libdir}/%{ghcdir}/parsec-*
%{_libdir}/%{ghcdir}/parsec-*/HSparsec-%{gpv_parsec}.o
%{_libdir}/%{ghcdir}/parsec-*/libHSparsec-%{gpv_parsec}.a
%dir %{_libdir}/%{ghcdir}/parsec-*/Text
%{_libdir}/%{ghcdir}/parsec-*/Text/*.hi
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/*.hi
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString/*.hi
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/Text
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/Text/*.hi
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/*.hi
%dir %{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec/*.hi

%dir %{_libdir}/%{ghcdir}/primitive-*
%{_libdir}/%{ghcdir}/primitive-*/HSprimitive-%{gpv_primitive}.o
%{_libdir}/%{ghcdir}/primitive-*/libHSprimitive-%{gpv_primitive}.a
%{_libdir}/%{ghcdir}/primitive-*/include
%dir %{_libdir}/%{ghcdir}/primitive-*/Control
%dir %{_libdir}/%{ghcdir}/primitive-*/Control/Monad
%{_libdir}/%{ghcdir}/primitive-*/Control/Monad/*.hi
%dir %{_libdir}/%{ghcdir}/primitive-*/Data
%{_libdir}/%{ghcdir}/primitive-*/Data/*.hi
%dir %{_libdir}/%{ghcdir}/primitive-*/Data/Primitive
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/*.hi
%dir %{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/Internal
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/Internal/*.hi

%dir %{_libdir}/%{ghcdir}/random-*
%{_libdir}/%{ghcdir}/random-*/HSrandom-%{gpv_random}.o
%{_libdir}/%{ghcdir}/random-*/libHSrandom-%{gpv_random}.a
%dir %{_libdir}/%{ghcdir}/random-*/System
%{_libdir}/%{ghcdir}/random-*/System/*.hi

%dir %{_libdir}/%{ghcdir}/regex-base-*
%{_libdir}/%{ghcdir}/regex-base-*/HSregex-base-%{gpv_regex_base}.o
%{_libdir}/%{ghcdir}/regex-base-*/libHSregex-base-%{gpv_regex_base}.a
%dir %{_libdir}/%{ghcdir}/regex-base-*/Text
%dir %{_libdir}/%{ghcdir}/regex-base-*/Text/Regex
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/*.hi
%dir %{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base/*.hi

%dir %{_libdir}/%{ghcdir}/regex-posix-*
%{_libdir}/%{ghcdir}/regex-posix-*/HSregex-posix-%{gpv_regex_posix}.o
%{_libdir}/%{ghcdir}/regex-posix-*/libHSregex-posix-%{gpv_regex_posix}.a
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/*.hi
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/*.hi
%dir %{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString/*.hi

%dir %{_libdir}/%{ghcdir}/regex-compat-*
%{_libdir}/%{ghcdir}/regex-compat-*/HSregex-compat-%{gpv_regex_compat}.o
%{_libdir}/%{ghcdir}/regex-compat-*/libHSregex-compat-%{gpv_regex_compat}.a
%dir %{_libdir}/%{ghcdir}/regex-compat-*/Text
%{_libdir}/%{ghcdir}/regex-compat-*/Text/*.hi

%dir %{_libdir}/%{ghcdir}/split-*
%{_libdir}/%{ghcdir}/split-*/HSsplit-%{gpv_split}.o
%{_libdir}/%{ghcdir}/split-*/libHSsplit-%{gpv_split}.a
%dir %{_libdir}/%{ghcdir}/split-*/Data
%dir %{_libdir}/%{ghcdir}/split-*/Data/List
%{_libdir}/%{ghcdir}/split-*/Data/List/*.hi
%dir %{_libdir}/%{ghcdir}/split-*/Data/List/Split
%{_libdir}/%{ghcdir}/split-*/Data/List/Split/*.hi

%dir %{_libdir}/%{ghcdir}/stm-*
%{_libdir}/%{ghcdir}/stm-*/HSstm-%{gpv_stm}.o
%{_libdir}/%{ghcdir}/stm-*/libHSstm-%{gpv_stm}.a
%dir %{_libdir}/%{ghcdir}/stm-*/Control
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Concurrent
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/*.hi
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM/*.hi
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Monad
%{_libdir}/%{ghcdir}/stm-*/Control/Monad/*.hi
%dir %{_libdir}/%{ghcdir}/stm-*/Control/Sequential
%{_libdir}/%{ghcdir}/stm-*/Control/Sequential/*.hi

%dir %{_libdir}/%{ghcdir}/syb-*
%{_libdir}/%{ghcdir}/syb-*/HSsyb-%{gpv_syb}.o
%{_libdir}/%{ghcdir}/syb-*/libHSsyb-%{gpv_syb}.a
%dir %{_libdir}/%{ghcdir}/syb-*/Data
%{_libdir}/%{ghcdir}/syb-*/Data/*.hi
%dir %{_libdir}/%{ghcdir}/syb-*/Data/Generics
%{_libdir}/%{ghcdir}/syb-*/Data/Generics/*.hi
%dir %{_libdir}/%{ghcdir}/syb-*/Generics
%{_libdir}/%{ghcdir}/syb-*/Generics/*.hi
%dir %{_libdir}/%{ghcdir}/syb-*/Generics/SYB
%{_libdir}/%{ghcdir}/syb-*/Generics/SYB/*.hi

%dir %{_libdir}/%{ghcdir}/text-*
%{_libdir}/%{ghcdir}/text-*/HStext-%{gpv_text}.o
%{_libdir}/%{ghcdir}/text-*/libHStext-%{gpv_text}.a
%dir %{_libdir}/%{ghcdir}/text-*/Data
%{_libdir}/%{ghcdir}/text-*/Data/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text
%{_libdir}/%{ghcdir}/text-*/Data/Text/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion
%{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/IO
%{_libdir}/%{ghcdir}/text-*/Data/Text/IO/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/Int
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/Int/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/RealFloat
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/RealFloat/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding/*.hi
%dir %{_libdir}/%{ghcdir}/text-*/Data/Text/Unsafe
%{_libdir}/%{ghcdir}/text-*/Data/Text/Unsafe/*.hi

%dir %{_libdir}/%{ghcdir}/transformers-*
%{_libdir}/%{ghcdir}/transformers-*/HStransformers-%{gpv_transformers}.o
%{_libdir}/%{ghcdir}/transformers-*/libHStransformers-%{gpv_transformers}.a
%dir %{_libdir}/%{ghcdir}/transformers-*/Control
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Applicative
%{_libdir}/%{ghcdir}/transformers-*/Control/Applicative/*.hi
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO/*.hi
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/*.hi
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS/*.hi
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State/*.hi
%dir %{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer/*.hi
%dir %{_libdir}/%{ghcdir}/transformers-*/Data
%dir %{_libdir}/%{ghcdir}/transformers-*/Data/Functor
%{_libdir}/%{ghcdir}/transformers-*/Data/Functor/*.hi

%dir %{_libdir}/%{ghcdir}/unordered-containers-*
%{_libdir}/%{ghcdir}/unordered-containers-*/HSunordered-containers-%{gpv_unordered_containers}.o
%{_libdir}/%{ghcdir}/unordered-containers-*/libHSunordered-containers-%{gpv_unordered_containers}.a
%dir %{_libdir}/%{ghcdir}/unordered-containers-*/Data
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/*.hi
%dir %{_libdir}/%{ghcdir}/unordered-containers-*/Data/HashMap
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/HashMap/*.hi

%dir %{_libdir}/%{ghcdir}/vector-*
%{_libdir}/%{ghcdir}/vector-*/HSvector-%{gpv_vector}.o
%{_libdir}/%{ghcdir}/vector-*/libHSvector-%{gpv_vector}.a
%{_libdir}/%{ghcdir}/vector-*/include
%dir %{_libdir}/%{ghcdir}/vector-*/Data
%{_libdir}/%{ghcdir}/vector-*/Data/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/Stream
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/Stream/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Generic
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Generic/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Internal
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Internal/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Primitive
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Primitive/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Storable
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Storable/*.hi
%dir %{_libdir}/%{ghcdir}/vector-*/Data/Vector/Unboxed
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Unboxed/*.hi

%dir %{_libdir}/%{ghcdir}/xhtml-*
%{_libdir}/%{ghcdir}/xhtml-*/HSxhtml-%{gpv_xhtml}.o
%{_libdir}/%{ghcdir}/xhtml-*/libHSxhtml-%{gpv_xhtml}.a
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text
%{_libdir}/%{ghcdir}/xhtml-*/Text/*.hi
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/*.hi
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict/*.hi
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset/*.hi
%dir %{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional/*.hi

%dir %{_libdir}/%{ghcdir}/zlib-*
%{_libdir}/%{ghcdir}/zlib-*/HSzlib-%{gpv_zlib}.o
%{_libdir}/%{ghcdir}/zlib-*/libHSzlib-%{gpv_zlib}.a
%dir %{_libdir}/%{ghcdir}/zlib-*/Codec
%dir %{_libdir}/%{ghcdir}/zlib-*/Codec/Compression
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/*.hi
%dir %{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib/*.hi

%{_libdir}/%{ghcdir}/package.conf.d/GLURaw-%{gpv_GLURaw}.conf
%{_libdir}/%{ghcdir}/package.conf.d/GLUT-%{gpv_GLUT}.conf
%{_libdir}/%{ghcdir}/package.conf.d/HTTP-%{gpv_HTTP}.conf
%{_libdir}/%{ghcdir}/package.conf.d/HUnit-%{gpv_HUnit}.conf
%{_libdir}/%{ghcdir}/package.conf.d/OpenGL-%{gpv_OpenGL}.conf
%{_libdir}/%{ghcdir}/package.conf.d/OpenGLRaw-%{gpv_OpenGLRaw}.conf
%{_libdir}/%{ghcdir}/package.conf.d/QuickCheck-%{gpv_QuickCheck}.conf
%{_libdir}/%{ghcdir}/package.conf.d/async-%{gpv_async}.conf
%{_libdir}/%{ghcdir}/package.conf.d/attoparsec-%{gpv_attoparsec}.conf
%{_libdir}/%{ghcdir}/package.conf.d/case-insensitive-%{gpv_case_insensitive}.conf
%{_libdir}/%{ghcdir}/package.conf.d/cgi-%{gpv_cgi}.conf
%{_libdir}/%{ghcdir}/package.conf.d/fgl-%{gpv_fgl}.conf
%{_libdir}/%{ghcdir}/package.conf.d/hashable-%{gpv_hashable}.conf
%{_libdir}/%{ghcdir}/package.conf.d/haskell-platform-%{version}.conf
%{_libdir}/%{ghcdir}/package.conf.d/haskell-src-%{gpv_haskell_src}.conf
%{_libdir}/%{ghcdir}/package.conf.d/html-%{gpv_html}.conf
%{_libdir}/%{ghcdir}/package.conf.d/mtl-%{gpv_mtl}.conf
%{_libdir}/%{ghcdir}/package.conf.d/network-%{gpv_network}.conf
%{_libdir}/%{ghcdir}/package.conf.d/parallel-%{gpv_parallel}.conf
%{_libdir}/%{ghcdir}/package.conf.d/parsec-%{gpv_parsec}.conf
%{_libdir}/%{ghcdir}/package.conf.d/primitive-%{gpv_primitive}.conf
%{_libdir}/%{ghcdir}/package.conf.d/random-%{gpv_random}.conf
%{_libdir}/%{ghcdir}/package.conf.d/regex-base-%{gpv_regex_base}.conf
%{_libdir}/%{ghcdir}/package.conf.d/regex-compat-%{gpv_regex_compat}.conf
%{_libdir}/%{ghcdir}/package.conf.d/regex-posix-%{gpv_regex_posix}.conf
%{_libdir}/%{ghcdir}/package.conf.d/split-%{gpv_split}.conf
%{_libdir}/%{ghcdir}/package.conf.d/stm-%{gpv_stm}.conf
%{_libdir}/%{ghcdir}/package.conf.d/syb-%{gpv_syb}.conf
%{_libdir}/%{ghcdir}/package.conf.d/text-%{gpv_text}.conf
%{_libdir}/%{ghcdir}/package.conf.d/transformers-%{gpv_transformers}.conf
%{_libdir}/%{ghcdir}/package.conf.d/unordered-containers-%{gpv_unordered_containers}.conf
%{_libdir}/%{ghcdir}/package.conf.d/vector-%{gpv_vector}.conf
%{_libdir}/%{ghcdir}/package.conf.d/xhtml-%{gpv_xhtml}.conf
%{_libdir}/%{ghcdir}/package.conf.d/zlib-%{gpv_zlib}.conf

%files prof
%defattr(644,root,root,755)

%{_libdir}/%{ghcdir}/GLURaw-*/libHSGLURaw-%{gpv_GLURaw}_p.a
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/*.p_hi
%{_libdir}/%{ghcdir}/GLURaw-*/Graphics/Rendering/GLU/Raw/*.p_hi

%{_libdir}/%{ghcdir}/GLUT-*/libHSGLUT-%{gpv_GLUT}_p.a
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Raw/*.p_hi
%{_libdir}/%{ghcdir}/GLUT-*/Graphics/UI/GLUT/Callbacks/*.p_hi

%{_libdir}/%{ghcdir}/HTTP-*/libHSHTTP-%{gpv_HTTP}_p.a
%{_libdir}/%{ghcdir}/HTTP-*/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/HTTP-*/Network/HTTP/*.p_hi

%{_libdir}/%{ghcdir}/HUnit-*/libHSHUnit-%{gpv_HUnit}_p.a
%{_libdir}/%{ghcdir}/HUnit-*/Test/*.p_hi
%{_libdir}/%{ghcdir}/HUnit-*/Test/HUnit/*.p_hi

%{_libdir}/%{ghcdir}/OpenGL-*/libHSOpenGL-%{gpv_OpenGL}_p.a
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/PixelRectangles/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Texturing/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GLU/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/FramebufferObjects/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/QueryUtils/*.p_hi
%{_libdir}/%{ghcdir}/OpenGL-*/Graphics/Rendering/OpenGL/GL/Shaders/*.p_hi

%{_libdir}/%{ghcdir}/OpenGLRaw-*/libHSOpenGLRaw-%{gpv_OpenGLRaw}_p.a
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/ARB/Compatibility/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/Core31/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/EXT/*.p_hi
%{_libdir}/%{ghcdir}/OpenGLRaw-*/Graphics/Rendering/OpenGL/Raw/NV/*.p_hi

%{_libdir}/%{ghcdir}/QuickCheck-*/libHSQuickCheck-%{gpv_QuickCheck}_p.a
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/*.p_hi
%{_libdir}/%{ghcdir}/QuickCheck-*/Test/QuickCheck/*.p_hi

%{_libdir}/%{ghcdir}/async-*/libHSasync-%{gpv_async}_p.a
%{_libdir}/%{ghcdir}/async-*/Control/Concurrent/*.p_hi

%{_libdir}/%{ghcdir}/attoparsec-*/libHSattoparsec-%{gpv_attoparsec}_p.a
%{_libdir}/%{ghcdir}/attoparsec-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Internal/*.p_hi
%{_libdir}/%{ghcdir}/attoparsec-*/Data/Attoparsec/Text/*.p_hi

%{_libdir}/%{ghcdir}/case-insensitive-*/libHScase-insensitive-%{gpv_case_insensitive}_p.a
%{_libdir}/%{ghcdir}/case-insensitive-*/Data/*.p_hi

%{_libdir}/%{ghcdir}/cgi-*/libHScgi-%{gpv_cgi}_p.a
%{_libdir}/%{ghcdir}/cgi-*/Network/CGI/*.p_hi
%{_libdir}/%{ghcdir}/cgi-*/Network/*.p_hi

%{_libdir}/%{ghcdir}/fgl-*/libHSfgl-%{gpv_fgl}_p.a
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Internal/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Monad/*.p_hi
%{_libdir}/%{ghcdir}/fgl-*/Data/Graph/Inductive/Query/*.p_hi

%{_libdir}/%{ghcdir}/hashable-*/libHShashable-%{gpv_hashable}_p.a
%{_libdir}/%{ghcdir}/hashable-*/Data/*.p_hi

%{_libdir}/%{ghcdir}/haskell-src-*/libHShaskell-src-%{gpv_haskell_src}_p.a
%{_libdir}/%{ghcdir}/haskell-src-*/Language/Haskell/*.p_hi

%{_libdir}/%{ghcdir}/html-*/libHShtml-%{gpv_html}_p.a
%{_libdir}/%{ghcdir}/html-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/html-*/Text/Html/*.p_hi

%{_libdir}/%{ghcdir}/mtl-*/libHSmtl-%{gpv_mtl}_p.a
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Cont/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Error/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Reader/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/RWS/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/State/*.p_hi
%{_libdir}/%{ghcdir}/mtl-*/Control/Monad/Writer/*.p_hi

%{_libdir}/%{ghcdir}/network-*/libHSnetwork-%{gpv_network}_p.a
%{_libdir}/%{ghcdir}/network-*/*.p_hi
%{_libdir}/%{ghcdir}/network-*/Network/*.p_hi
%{_libdir}/%{ghcdir}/network-*/Network/Socket/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/network-*/Network/Socket/*.p_hi

%{_libdir}/%{ghcdir}/parallel-*/libHSparallel-%{gpv_parallel}_p.a
%{_libdir}/%{ghcdir}/parallel-*/Control/*.p_hi
%{_libdir}/%{ghcdir}/parallel-*/Control/Parallel/*.p_hi

%{_libdir}/%{ghcdir}/parsec-*/libHSparsec-%{gpv_parsec}_p.a
%{_libdir}/%{ghcdir}/parsec-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/ByteString/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/Parsec/Text/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/*.p_hi
%{_libdir}/%{ghcdir}/parsec-*/Text/ParserCombinators/Parsec/*.p_hi

%{_libdir}/%{ghcdir}/primitive-*/libHSprimitive-%{gpv_primitive}_p.a
%{_libdir}/%{ghcdir}/primitive-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/*.p_hi
%{_libdir}/%{ghcdir}/primitive-*/Data/Primitive/Internal/*.p_hi

%{_libdir}/%{ghcdir}/random-*/libHSrandom-%{gpv_random}_p.a
%{_libdir}/%{ghcdir}/random-*/System/*.p_hi

%{_libdir}/%{ghcdir}/regex-base-*/libHSregex-base-%{gpv_regex_base}_p.a
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/*.p_hi
%{_libdir}/%{ghcdir}/regex-base-*/Text/Regex/Base/*.p_hi

%{_libdir}/%{ghcdir}/regex-compat-*/libHSregex-compat-%{gpv_regex_compat}_p.a
%{_libdir}/%{ghcdir}/regex-compat-*/Text/*.p_hi

%{_libdir}/%{ghcdir}/regex-posix-*/libHSregex-posix-%{gpv_regex_posix}_p.a
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/*.p_hi
%{_libdir}/%{ghcdir}/regex-posix-*/Text/Regex/Posix/ByteString/*.p_hi

%{_libdir}/%{ghcdir}/split-*/libHSsplit-%{gpv_split}_p.a
%{_libdir}/%{ghcdir}/split-*/Data/List/*.p_hi
%{_libdir}/%{ghcdir}/split-*/Data/List/Split/*.p_hi

%{_libdir}/%{ghcdir}/stm-*/libHSstm-%{gpv_stm}_p.a
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Concurrent/STM/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Monad/*.p_hi
%{_libdir}/%{ghcdir}/stm-*/Control/Sequential/*.p_hi

%{_libdir}/%{ghcdir}/syb-*/libHSsyb-%{gpv_syb}_p.a
%{_libdir}/%{ghcdir}/syb-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/syb-*/Data/Generics/*.p_hi
%{_libdir}/%{ghcdir}/syb-*/Generics/*.p_hi
%{_libdir}/%{ghcdir}/syb-*/Generics/SYB/*.p_hi

%{_libdir}/%{ghcdir}/text-*/libHStext-%{gpv_text}_p.a
%{_libdir}/%{ghcdir}/text-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Encoding/Fusion/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Fusion/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/IO/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/Int/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Builder/RealFloat/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Lazy/Encoding/*.p_hi
%{_libdir}/%{ghcdir}/text-*/Data/Text/Unsafe/*.p_hi

%{_libdir}/%{ghcdir}/transformers-*/libHStransformers-%{gpv_transformers}_p.a
%{_libdir}/%{ghcdir}/transformers-*/Control/Applicative/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/IO/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/RWS/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/State/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Control/Monad/Trans/Writer/*.p_hi
%{_libdir}/%{ghcdir}/transformers-*/Data/Functor/*.p_hi

%{_libdir}/%{ghcdir}/unordered-containers-*/libHSunordered-containers-%{gpv_unordered_containers}_p.a
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/unordered-containers-*/Data/HashMap/*.p_hi

%{_libdir}/%{ghcdir}/vector-*/libHSvector-%{gpv_vector}_p.a
%{_libdir}/%{ghcdir}/vector-*/Data/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Fusion/Stream/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Generic/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Internal/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Primitive/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Storable/*.p_hi
%{_libdir}/%{ghcdir}/vector-*/Data/Vector/Unboxed/*.p_hi

%{_libdir}/%{ghcdir}/xhtml-*/libHSxhtml-%{gpv_xhtml}_p.a
%{_libdir}/%{ghcdir}/xhtml-*/Text/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Frameset/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Strict/*.p_hi
%{_libdir}/%{ghcdir}/xhtml-*/Text/XHtml/Transitional/*.p_hi

%{_libdir}/%{ghcdir}/zlib-*/libHSzlib-%{gpv_zlib}_p.a
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/*.p_hi
%{_libdir}/%{ghcdir}/zlib-*/Codec/Compression/Zlib/*.p_hi
