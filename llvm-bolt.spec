#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : llvm-bolt
Version  : 14.0.0
Release  : 431
URL      : file:///insilications/apps/llvm-bolt-14.0.0.tar.gz
Source0  : file:///insilications/apps/llvm-bolt-14.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: llvm-bolt-bin = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : asciidoctor
BuildRequires : asciidoctor-bin
BuildRequires : asciidoctor-dev
BuildRequires : autoconf-archive-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cmake
BuildRequires : curl-bin
BuildRequires : curl-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : elfutils-dev
BuildRequires : expect
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : graphviz
BuildRequires : guile
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : llvm
BuildRequires : llvm-bin
BuildRequires : llvm-data
BuildRequires : llvm-lib
BuildRequires : llvm-libexec
BuildRequires : llvm-staticdev
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-bin
BuildRequires : ncurses-data
BuildRequires : ncurses-dev
BuildRequires : ncurses-staticdev
BuildRequires : ninja
BuildRequires : ninja-bin
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pcre
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : perl
BuildRequires : pkgconfig(libedit)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(zlib)
BuildRequires : procps-ng
BuildRequires : protobuf-dev
BuildRequires : pypi(absl_py)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(dataclasses)
BuildRequires : pypi(deprecated)
BuildRequires : pypi(gitdb)
BuildRequires : pypi(gitpython)
BuildRequires : pypi(graphviz)
BuildRequires : pypi(humanize)
BuildRequires : pypi(idna)
BuildRequires : pypi(psutil)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pygithub)
BuildRequires : pypi(pyjwt)
BuildRequires : pypi(pynacl)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(ruamel.yaml)
BuildRequires : pypi(ruamel.yaml.clib)
BuildRequires : pypi(seaborn)
BuildRequires : pypi(smmap)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(wrapt)
BuildRequires : pypi-pygments
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : ruby
BuildRequires : sed
BuildRequires : swig
BuildRequires : tcl
BuildRequires : termcolor
BuildRequires : texinfo
BuildRequires : time
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : valgrind-dev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : yaml-cpp-staticdev
BuildRequires : yaml-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the llvm-bolt package.
Group: Binaries

%description bin
bin components for the llvm-bolt package.


%package staticdev
Summary: staticdev components for the llvm-bolt package.
Group: Default

%description staticdev
staticdev components for the llvm-bolt package.


%prep
%setup -q -n llvm-bolt-14.0.0
cd %{_builddir}/llvm-bolt-14.0.0

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651737532
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1f content
export VERBOSE=1
unset ASFLAGS
unset LDFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
# export CFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie"
# export ASMFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie"
# export CXXFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie"
# export LDFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie -Wl,-mllvm,-x86-use-vzeroupper=0"
export CC=clang
export CXX=clang++
export AR=/usr/bin/llvm-ar
export RANLIB=/usr/bin/llvm-ranlib
export NM=/usr/bin/llvm-nm
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags %{nil}
%global _disable_maintainer_mode %{nil}
export CCACHE_DISABLE=true
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
## altflags1f end
cmake -G Ninja ../llvm \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DLIB_INSTALL_DIR=/usr/lib64 \
    -DLIB_SUFFIX=64 \
    -DLLVM_LIBDIR_SUFFIX=64 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib64 \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SBINDIR=/usr/bin \
    -DLLVM_PARALLEL_COMPILE_JOBS:STRING=12 \
    -DLLVM_PARALLEL_LINK_JOBS:STRING=1 \
    -DCMAKE_AR=/usr/bin/llvm-ar \
    -DCMAKE_NM=/usr/bin/llvm-nm \
    -DCMAKE_RANLIB=/usr/bin/llvm-ranlib \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DENABLE_LINKER_BUILD_ID:BOOL=ON \
    -DCLANG_DEFAULT_LINKER=lld \
    -DLLVM_ENABLE_LIBCXX:BOOL=OFF \
    -DLLVM_STATIC_LINK_CXX_STDLIB:BOOL=ON \
    -DCLANG_DEFAULT_CXX_STDLIB:STRING=libstdc++ \
    -DCLANG_LINK_CLANG_DYLIB:BOOL=OFF \
    -DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
    -DLLVM_BUILD_LLVM_DYLIB:BOOL=OFF \
    -DLIBCLANG_BUILD_STATIC:BOOL=ON \
    -DLLVM_BINUTILS_INCDIR=/usr/include \
    -DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
    -DLLVM_ENABLE_NEW_PASS_MANAGER:BOOL=ON \
    -DLLVM_ENABLE_PIC:BOOL=OFF \
    -DLLVM_TARGETS_TO_BUILD="X86" \
    -DLLVM_USE_LINKER:STRING=lld \
    -DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3 \
    -DLLVM_INCLUDE_EXAMPLES:BOOL=OFF \
    -DLLVM_INCLUDE_BENCHMARKS:BOOL=OFF \
    -DLLVM_BUILD_EXAMPLES:BOOL=OFF \
    -DLLVM_BUILD_DOCS:BOOL=OFF \
    -DLLVM_BUILD_RUNTIME:BOOL=OFF \
    -DLLVM_BUILD_TOOLS:BOOL=OFF \
    -DCLANG_BUILD_TOOLS:BOOL=OFF \
    -DLLVM_BUILD_UTILS:BOOL=OFF \
    -DCOMPILER_RT_BUILD_SANITIZERS:BOOL=OFF \
    -DCOMPILER_RT_BUILD_XRAY:BOOL=OFF \
    -DCOMPILER_RT_BUILD_CRT:BOOL=OFF \
    -DCOMPILER_RT_BUILD_LIBFUZZER:BOOL=OFF \
    -DLLVM_INSTALL_BINUTILS_SYMLINKS:BOOL=OFF \
    -DLLVM_INSTALL_UTILS:BOOL=OFF \
    -DLLVM_ENABLE_UNWIND_TABLES:BOOL=ON \
    -DLLVM_ENABLE_EH:BOOL=ON \
    -DLLVM_ENABLE_RTTI:BOOL=ON \
    -DLLVM_ENABLE_THREADS:BOOL=ON \
    -DLLVM_ENABLE_Z3_SOLVER:BOOL=OFF \
    -DLLVM_ENABLE_LIBEDIT:BOOL=OFF \
    -DLLVM_ENABLE_TERMINFO:BOOL=OFF \
    -DLLVM_ENABLE_ZLIB:BOOL=ON \
    -DLLVM_ENABLE_FFI:BOOL=ON \
    -DLLVM_ENABLE_ASSERTIONS:BOOL=OFF \
    -DLLVM_ENABLE_PROJECTS="bolt" \
    -DCMAKE_C_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie" \
    -DCMAKE_CXX_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie" \
    -DCMAKE_EXE_LINKER_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie -Wl,-mllvm,-x86-use-vzeroupper=0" \
    -DCMAKE_MODULE_LINKER_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie -Wl,-mllvm,-x86-use-vzeroupper=0" \
    -DCMAKE_SHARED_LINKER_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie -Wl,-mllvm,-x86-use-vzeroupper=0" \
    -DCMAKE_ASM_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie" \
    -DCMAKE_Fortran_FLAGS_RELEASE="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie" \
    -DGCC_INSTALL_PREFIX="/usr" \
    -Wno-dev
## make_prepend content
sd "/usr/lib64/libffi\.so" "/usr/lib64/libffi.a" $(fd -uu --glob *.ninja)
sd "/usr/lib64/libz\.so" "/usr/lib64/libz.a" $(fd -uu --glob *.ninja)
sd "/usr/lib64/libxml2\.so" "/usr/lib64/libxml2.a /usr/lib64/liblzma.a /usr/lib64/libz.a" $(fd -uu --glob *.ninja)
sd "/usr/lib64/libffi\.so" "/usr/lib64/libffi.a" $(fd -uu --glob *.ninja)
sd "/usr/lib64/libz\.so" "/usr/lib64/libz.a" $(fd -uu --glob *.ninja)
sd "/usr/lib64/libxml2\.so" "/usr/lib64/libxml2.a /usr/lib64/liblzma.a /usr/lib64/libz.a" $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s/usr/lib64/libz\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s/usr/lib64/libxml2\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s/usr/lib64/libz\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s/usr/lib64/libxml2\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s\-lz)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s\-lxml2)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s\-lz)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_LIBRARIES.+)(\s\-lxml2)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s/usr/lib64/libz\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s/usr/lib64/libxml2\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s/usr/lib64/libz\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s/usr/lib64/libxml2\.so)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s\-lz)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s\-lxml2)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s\-lz)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
sd '(LINK_FLAGS.+)(\s\-lxml2)' -- '$1 -Wl,--whole-archive,--allow-multiple-definition,/usr/lib64/libxml2.a,/usr/lib64/liblzma.a,/usr/lib64/libz.a,-lpthread,-lrt,-ldl,-lm,-lmvec,--no-allow-multiple-definition,--no-whole-archive' $(fd -uu --glob *.ninja)
## make_prepend end
## make_macro content
ninja --verbose all
## make_macro end
popd

%install
export SOURCE_DATE_EPOCH=1651737532
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
## altflags1f content
export VERBOSE=1
unset ASFLAGS
unset LDFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
# export CFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie"
# export ASMFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie"
# export CXXFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie"
# export LDFLAGS="-Wno-unused-command-line-argument -DNDEBUG -O3 -falign-functions=32 -fasynchronous-unwind-tables -fexceptions -fno-lto -fno-plt -fno-semantic-interposition -fno-stack-protector -fomit-frame-pointer -fuse-ld=lld -march=native -mcpu=native -mno-vzeroupper -mprefer-vector-width=256 -mtune=native -pipe -pthread -static-libgcc -static-libstdc++ -Wno-error -Wp,-D_REENTRANT -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,-Bsymbolic-functions -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wl,--emit-relocs -fno-PIC -fno-PIE -fno-pic -fno-pie -Wl,-mllvm,-x86-use-vzeroupper=0"
export CC=clang
export CXX=clang++
export AR=/usr/bin/llvm-ar
export RANLIB=/usr/bin/llvm-ranlib
export NM=/usr/bin/llvm-nm
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags %{nil}
%global _disable_maintainer_mode %{nil}
export CCACHE_DISABLE=true
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
## altflags1f end
## install_macro start
install -dm 0755 %{buildroot}/usr/lib64/
install -dm 0755 %{buildroot}/usr/lib/
install -dm 0755 %{buildroot}/usr/bin/
pushd clr-build
pushd bin/
install -m 0755 llvm-bolt %{buildroot}/usr/bin/llvm-bolt
install -m 0755 llvm-bolt-heatmap %{buildroot}/usr/bin/llvm-bolt-heatmap || :
cp -P llvm-boltdiff %{buildroot}/usr/bin/llvm-boltdiff
cp -P perf2bolt %{buildroot}/usr/bin/perf2bolt
popd
pushd lib
install -m 0755 libbolt_rt_instr.a %{buildroot}/usr/lib/libbolt_rt_instr.a
install -m 0755 libbolt_rt_instr.a %{buildroot}/usr/lib64/libbolt_rt_instr.a
install -m 0755 libbolt_rt_hugify.a %{buildroot}/usr/lib/libbolt_rt_hugify.a
install -m 0755 libbolt_rt_hugify.a %{buildroot}/usr/lib64/libbolt_rt_hugify.a
popd
popd
## install_macro end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/llvm-bolt
/usr/bin/llvm-boltdiff
/usr/bin/perf2bolt

%files staticdev
%defattr(-,root,root,-)
/usr/lib/libbolt_rt_hugify.a
/usr/lib/libbolt_rt_instr.a
/usr/lib64/libbolt_rt_hugify.a
/usr/lib64/libbolt_rt_instr.a
