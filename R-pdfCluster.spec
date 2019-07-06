#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pdfCluster
Version  : 1.0.3
Release  : 20
URL      : https://cran.r-project.org/src/contrib/pdfCluster_1.0-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pdfCluster_1.0-3.tar.gz
Summary  : Cluster Analysis via Nonparametric Density Estimation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-pdfCluster-lib = %{version}-%{release}
BuildRequires : R-geometry
BuildRequires : R-magic
BuildRequires : R-sm
BuildRequires : R-spdep
BuildRequires : buildreq-R

%description
estimation is performed. Operationally, the kernel method is used throughout to estimate
   the density. Diagnostics methods for evaluating the quality of the clustering 
   are available. The package includes also a routine to estimate the 
   probability density function obtained by the kernel method, given a set of
   data with arbitrary dimensions.

%package lib
Summary: lib components for the R-pdfCluster package.
Group: Libraries

%description lib
lib components for the R-pdfCluster package.


%prep
%setup -q -c -n pdfCluster

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552893766

%install
export SOURCE_DATE_EPOCH=1552893766
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdfCluster
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdfCluster
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdfCluster
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  pdfCluster || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pdfCluster/CITATION
/usr/lib64/R/library/pdfCluster/ChangeLog
/usr/lib64/R/library/pdfCluster/DESCRIPTION
/usr/lib64/R/library/pdfCluster/INDEX
/usr/lib64/R/library/pdfCluster/Meta/Rd.rds
/usr/lib64/R/library/pdfCluster/Meta/data.rds
/usr/lib64/R/library/pdfCluster/Meta/features.rds
/usr/lib64/R/library/pdfCluster/Meta/hsearch.rds
/usr/lib64/R/library/pdfCluster/Meta/links.rds
/usr/lib64/R/library/pdfCluster/Meta/nsInfo.rds
/usr/lib64/R/library/pdfCluster/Meta/package.rds
/usr/lib64/R/library/pdfCluster/NAMESPACE
/usr/lib64/R/library/pdfCluster/R/pdfCluster
/usr/lib64/R/library/pdfCluster/R/pdfCluster.rdb
/usr/lib64/R/library/pdfCluster/R/pdfCluster.rdx
/usr/lib64/R/library/pdfCluster/data/oliveoil.rda
/usr/lib64/R/library/pdfCluster/data/wine.rda
/usr/lib64/R/library/pdfCluster/help/AnIndex
/usr/lib64/R/library/pdfCluster/help/aliases.rds
/usr/lib64/R/library/pdfCluster/help/paths.rds
/usr/lib64/R/library/pdfCluster/help/pdfCluster.rdb
/usr/lib64/R/library/pdfCluster/help/pdfCluster.rdx
/usr/lib64/R/library/pdfCluster/html/00Index.html
/usr/lib64/R/library/pdfCluster/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pdfCluster/libs/pdfCluster.so
/usr/lib64/R/library/pdfCluster/libs/pdfCluster.so.avx2
/usr/lib64/R/library/pdfCluster/libs/pdfCluster.so.avx512
