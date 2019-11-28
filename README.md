python-deltasigma
=================

A port of the **MATLAB Delta Sigma Toolbox** based on free software and very little sleep


The **python-deltasigma** is a Python package to *synthesize, simulate, scale
and map to implementable topologies* **delta sigma modulators**.

It aims to provide **a 1:1 Python port** of Richard Schreier's ***excellent***
**[MATLAB Delta Sigma Toolbox](http://www.mathworks.com/matlabcentral/fileexchange/19-delta-sigma-toolbox)**,
the *de facto* standard tool for high-level delta sigma simulation, upon which
it is very heavily based.

***

**Homepage:** [python-deltasigma.io](http://python-deltasigma.io)

**Documentation:** [docs.python-deltasigma.io](http://docs.python-deltasigma.io)

**Latest version:** [0.2](https://pypi.python.org/pypi/deltasigma/)


[![Build Status](https://travis-ci.org/ggventurini/python-deltasigma.png?branch=master)](https://travis-ci.org/ggventurini/python-deltasigma) [![Coverage Status](https://coveralls.io/repos/ggventurini/python-deltasigma/badge.png?branch=master)](https://coveralls.io/r/ggventurini/python-deltasigma?branch=master)
[![PyPi version](http://img.shields.io/badge/version-0.2-brightgreen.png)](https://pypi.python.org/pypi/deltasigma/)
[![PyPi downloads](https://img.shields.io/pypi/dm/deltasigma.svg)](https://pypi.python.org/pypi/deltasigma/)
[![PyPi pythons](https://img.shields.io/pypi/pyversions/deltasigma.svg)](https://pypi.python.org/pypi/deltasigma/)
[![BSD 2 clause license](http://img.shields.io/badge/license-BSD-brightgreen.png)](https://raw.githubusercontent.com/ggventurini/python-deltasigma/master/LICENSE)
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.18529.svg)](http://dx.doi.org/10.5281/zenodo.18529)


***

## Status

The fundamental functionality is available and working.

Secondary features such as "native" quadrature modulator support,
PIS calculation or ESL are still work in progress. A list of functions
and files is included in [files.csv](https://github.com/ggventurini/python-deltasigma/blob/master/files.csv),
updated with the current status.

Further functionality is expected to be completed in the next versions
according to
[the ROADMAP](https://github.com/ggventurini/python-deltasigma/blob/master/ROADMAP.md).

## Install

`python-deltasigma` runs on Linux, Mac OS X and Windows.

Installing requires **Python 2.6+** or **3.3+**, **numpy**, **scipy**
(>= 0.16.0) and **matplotlib**.

Strongly recommended: **Cython** - for significantly faster delta sigma modulator simulations. 

They are packaged by virtually all
the major Linux distributions.

On Windows, need to compile **[blas](http://www.netlib.org/blas/blas-3.8.0.tgz)** and
**[cblas](http://www.netlib.org/blas/blast-forum/cblas.tgz)** by
**[Mingw-w64](http://mingw-w64.org)**:

    cd <blas_src_dir>
    make ARCH=gfortran ARCHFLAGS="-m[32|64] -shared -o" BLASLIB=libblas.dll RANLIB=echo OPTS="-O3 -m[32|64]" all
    cd <cblas_src_dir>
    make ARCH=gcc ARCHFLAGS="-lblas -L<blas_src_dir> -m[32|64] -shared -o" CBLIB=libcblas.dll RANLIB=echo CFLAGS="-O3 -DADD_ -m[32|64] -fPIC" FFLAGS="-O3 -m[32|64]" alllib

    mkdir <blas_cblas_install_dir>
    mkdir <blas_cblas_install_dir>\lib[32|64]
    cp <blas_src_dir>\libblas.dll <cblas_src_dir>\src\libcblas.dll <blas_cblas_install_dir>\lib[32|64]
    mkdir <blas_cblas_install_dir>\include
    cp <cblas_src_dir>\include\cblas.h <cblas_src_dir>\include\cblas_f77.h <blas_cblas_install_dir>\include

    echo [blas] >> <python_numpy_dir>\distutils\site.cfg
    echo library_dirs = <blas_cblas_install_dir(replace \ by /)>/lib[32|64] >> <python_numpy_dir>\distutils\site.cfg
    echo include_dirs = <blas_cblas_install_dir(replace \ by /)>/include >> <python_numpy_dir>\distutils\site.cfg
    echo libraries = blas, cblas >> <python_numpy_dir>\distutils\site.cfg

When the dependencies are satisfied, run:

    pip install deltasigma

to install the latest stable version from the [Python
Package Index (PYPI)](http://pypi.python.org), or:

    python setup.py install

if you're installing a development version from Git.

### Extras

Install the **[sphinx](http://sphinx-doc.org/)** package to build the
documentation yourself.

The test suite requires
**[setuptools](https://pypi.python.org/pypi/setuptools)**,
used to access the reference function outputs.

Testing can be automated with
**[nose](https://pypi.python.org/pypi/nose/)**, issuing:

    nosetests -v deltasigma

## Documentation


In addition to the notebooks found in the `examples/` directory,
ported from the MATLAB Delta Sigma toolbox:

1. You can find the included
   [package documentation online](http://python-deltasigma.readthedocs.org/en/latest/).

2. The original MATLAB Toolbox provides in-depth documentation, which
   is very useful to understand what the toolbox is capable of. See
   [DSToolbox.pdf](https://github.com/ggventurini/python-deltasigma/blob/master/delsig/DSToolbox.pdf?raw=true)
   and [OnePageStory.pdf](https://github.com/ggventurini/python-deltasigma/blob/master/delsig/OnePageStory.pdf?raw=true)
   (*PDF warning*).

3. The book:

    Richard Schreier, Gabor C. Temes, *Understanding Delta-Sigma Data Converters*,
    ISBN: 978-0-471-46585-0, November 2004, Wiley-IEEE Press

    is probably *the most authoritative resource on the topic*. Chapter 8-9 show
    how to use the MATLAB toolkit and the observations apply also to this Python
    port. Links
    [on amazon](http://www.amazon.com/Understanding-Delta-Sigma-Converters-Richard-Schreier/dp/0471465852),
    [on the Wiley-IEEE press](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-0471465852,miniSiteCd-IEEE2.html).

    *I am not affiliated with neither the sellers nor the authors.*

## How to contribute

I write this software in my free time, this is not funded research.

If you find this package useful, you are welcome to freely contribute
to its development in one of the following ways.

### Send a pull request my way

Pull requests are most gladly received!

There are only a few *guidelines*, which can be overridden every time
it is reasonable to do so:

* Please try to follow `PEP8`.

* Try to keep the functions signature identical. Parameters with
  `NaN`/`[]` as default values have their default value replaced with
  `None`.

* If a function has a varible number of return values, its Python port
  should implement the maximum number of return values.

### Support python-deltasigma with a donation

*I do not want your money.* I develop this software because I enjoy it and
because I use it myself.

If you wish to support the development of `python-deltasigma` and you wish
to contribute monetarily, ***please donate to cancer research instead:***

* **[Association for International Cancer Research *(eng)*](http://www.aicr.org.uk/donate.aspx)**,
  or
* **[Fond. IRCCS Istituto Nazionale dei Tumori *(it)*](http://www.istitutotumori.mi.it/modules.php?name=Content&pa=showpage&pid=24)**.

Consider [sending me a mail](http://tinymailto.com/5310) afterwards, ***it
makes for great motivation!***


## Licensing and copyright notice

All original MATLAB code is Copyright (c) 2009, Richard Schreier.
See the LICENSE file for the licensing terms.

The Python code here provided is a derivative work from the above toolkit and
subject to the same license terms.

This package contains some source code from `pydsm`, also based on the same
MATLAB toolbox. The `pydsm` package is copyright (c) 2012, Sergio Callegari.

When not otherwise specified, the Python code is Copyright 2013, Giuseppe
Venturini and the python-deltasigma contributors.

MATLAB is a registered trademark of The MathWorks, Inc.
