#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: 5424026
#
Name     : pypi-timm
Version  : 1.0.12
Release  : 5
URL      : https://files.pythonhosted.org/packages/8b/d9/7382e27b379d4b791811396e05c9421703bbb21b2f726ff3e78469b5b194/timm-1.0.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/d9/7382e27b379d4b791811396e05c9421703bbb21b2f726ff3e78469b5b194/timm-1.0.12.tar.gz
Summary  : PyTorch Image Models
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-timm-license = %{version}-%{release}
Requires: pypi-timm-python = %{version}-%{release}
Requires: pypi-timm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_backend)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PyTorch Image Models
- [What's New](#whats-new)
- [Introduction](#introduction)
- [Models](#models)
- [Features](#features)
- [Results](#results)
- [Getting Started (Documentation)](#getting-started-documentation)
- [Train, Validation, Inference Scripts](#train-validation-inference-scripts)
- [Awesome PyTorch Resources](#awesome-pytorch-resources)
- [Licenses](#licenses)
- [Citing](#citing)

%package license
Summary: license components for the pypi-timm package.
Group: Default

%description license
license components for the pypi-timm package.


%package python
Summary: python components for the pypi-timm package.
Group: Default
Requires: pypi-timm-python3 = %{version}-%{release}

%description python
python components for the pypi-timm package.


%package python3
Summary: python3 components for the pypi-timm package.
Group: Default
Requires: python3-core
Provides: pypi(timm)
Requires: pypi(huggingface_hub)
Requires: pypi(pyyaml)
Requires: pypi(safetensors)
Requires: pypi(torch)
Requires: pypi(torchvision)

%description python3
python3 components for the pypi-timm package.


%prep
%setup -q -n timm-1.0.12
cd %{_builddir}/timm-1.0.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1733322128
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-timm
cp %{_builddir}/timm-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-timm/aed587b35618c7622a02c43cf3ebabb2adf43794 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-timm/aed587b35618c7622a02c43cf3ebabb2adf43794

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
