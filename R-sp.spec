#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sp
Version  : 1.2
Release  : 25
URL      : https://cran.r-project.org/src/contrib/sp_1.2-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sp_1.2-3.tar.gz
Summary  : Classes and Methods for Spatial Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-sp-lib
BuildRequires : R-RColorBrewer
BuildRequires : R-maptools
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-sp package.
Group: Libraries

%description lib
lib components for the R-sp package.


%prep
%setup -q -c -n sp

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484549410

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1484549410
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sp
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sp || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sp/CITATION
/usr/lib64/R/library/sp/DESCRIPTION
/usr/lib64/R/library/sp/INDEX
/usr/lib64/R/library/sp/Meta/Rd.rds
/usr/lib64/R/library/sp/Meta/data.rds
/usr/lib64/R/library/sp/Meta/demo.rds
/usr/lib64/R/library/sp/Meta/hsearch.rds
/usr/lib64/R/library/sp/Meta/links.rds
/usr/lib64/R/library/sp/Meta/nsInfo.rds
/usr/lib64/R/library/sp/Meta/package.rds
/usr/lib64/R/library/sp/Meta/vignette.rds
/usr/lib64/R/library/sp/NAMESPACE
/usr/lib64/R/library/sp/NEWS.Rd
/usr/lib64/R/library/sp/R/sp
/usr/lib64/R/library/sp/R/sp.rdb
/usr/lib64/R/library/sp/R/sp.rdx
/usr/lib64/R/library/sp/data/Rlogo.rda
/usr/lib64/R/library/sp/data/meuse.area.rda
/usr/lib64/R/library/sp/data/meuse.grid.rda
/usr/lib64/R/library/sp/data/meuse.grid_ll.rda
/usr/lib64/R/library/sp/data/meuse.rda
/usr/lib64/R/library/sp/data/meuse.riv.rda
/usr/lib64/R/library/sp/demo/depend.R
/usr/lib64/R/library/sp/demo/fib.R
/usr/lib64/R/library/sp/demo/gallery.R
/usr/lib64/R/library/sp/demo/meuse.R
/usr/lib64/R/library/sp/demo/mp.R
/usr/lib64/R/library/sp/demo/polar.R
/usr/lib64/R/library/sp/demo/webmap.R
/usr/lib64/R/library/sp/doc/csdacm.R
/usr/lib64/R/library/sp/doc/csdacm.Rnw
/usr/lib64/R/library/sp/doc/csdacm.pdf
/usr/lib64/R/library/sp/doc/index.html
/usr/lib64/R/library/sp/doc/intro_sp.R
/usr/lib64/R/library/sp/doc/intro_sp.Rnw
/usr/lib64/R/library/sp/doc/intro_sp.pdf
/usr/lib64/R/library/sp/doc/over.R
/usr/lib64/R/library/sp/doc/over.Rnw
/usr/lib64/R/library/sp/doc/over.pdf
/usr/lib64/R/library/sp/external/seamap105_mod.csv
/usr/lib64/R/library/sp/external/simple.ag
/usr/lib64/R/library/sp/external/test.ag
/usr/lib64/R/library/sp/help/AnIndex
/usr/lib64/R/library/sp/help/aliases.rds
/usr/lib64/R/library/sp/help/paths.rds
/usr/lib64/R/library/sp/help/sp.rdb
/usr/lib64/R/library/sp/help/sp.rdx
/usr/lib64/R/library/sp/html/00Index.html
/usr/lib64/R/library/sp/html/R.css
/usr/lib64/R/library/sp/include/sp.h
/usr/lib64/R/library/sp/include/sp_xports.c
/usr/lib64/R/library/sp/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sp/libs/sp.so
