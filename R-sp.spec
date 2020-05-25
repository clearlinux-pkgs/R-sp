#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sp
Version  : 1.4.2
Release  : 70
URL      : https://cran.r-project.org/src/contrib/sp_1.4-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sp_1.4-2.tar.gz
Summary  : Classes and Methods for Spatial Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-sp-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
data; the classes document where the spatial location information
  resides, for 2D or 3D data. Utility functions are provided, e.g. for
  plotting data as maps, spatial selection, as well as methods for
  retrieving coordinates, for subsetting, print, summary, etc.

%package lib
Summary: lib components for the R-sp package.
Group: Libraries

%description lib
lib components for the R-sp package.


%prep
%setup -q -c -n sp
cd %{_builddir}/sp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590375861

%install
export SOURCE_DATE_EPOCH=1590375861
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sp/CITATION
/usr/lib64/R/library/sp/DESCRIPTION
/usr/lib64/R/library/sp/INDEX
/usr/lib64/R/library/sp/Meta/Rd.rds
/usr/lib64/R/library/sp/Meta/data.rds
/usr/lib64/R/library/sp/Meta/demo.rds
/usr/lib64/R/library/sp/Meta/features.rds
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
/usr/lib64/R/library/sp/tests/agg.R
/usr/lib64/R/library/sp/tests/agg.Rout.save
/usr/lib64/R/library/sp/tests/base.R
/usr/lib64/R/library/sp/tests/base.Rout.save
/usr/lib64/R/library/sp/tests/fail1.R
/usr/lib64/R/library/sp/tests/fail1.Rout.save
/usr/lib64/R/library/sp/tests/grid.R
/usr/lib64/R/library/sp/tests/grid.Rout.save
/usr/lib64/R/library/sp/tests/mp.Rout.save
/usr/lib64/R/library/sp/tests/nc.Rout.save
/usr/lib64/R/library/sp/tests/over.Rout.save
/usr/lib64/R/library/sp/tests/over2.R
/usr/lib64/R/library/sp/tests/over2.Rout.save
/usr/lib64/R/library/sp/tests/pass1.R
/usr/lib64/R/library/sp/tests/pass1.Rout.save
/usr/lib64/R/library/sp/tests/point.in.polygon.R
/usr/lib64/R/library/sp/tests/point.in.polygon.Rout.save
/usr/lib64/R/library/sp/tests/sel.R
/usr/lib64/R/library/sp/tests/sel.Rout.save
/usr/lib64/R/library/sp/tests/sp1.R
/usr/lib64/R/library/sp/tests/sp1.Rout.save
/usr/lib64/R/library/sp/tests/spDists.R
/usr/lib64/R/library/sp/tests/spDists.Rout.save
/usr/lib64/R/library/sp/tests/spplot.R
/usr/lib64/R/library/sp/tests/spplot.Rout.save
/usr/lib64/R/library/sp/tests/zerodist.R
/usr/lib64/R/library/sp/tests/zerodist.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sp/libs/sp.so
/usr/lib64/R/library/sp/libs/sp.so.avx2
/usr/lib64/R/library/sp/libs/sp.so.avx512
