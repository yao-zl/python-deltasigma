# -*- coding: utf-8 -*-
# _config.py
# Module providing configuration switches
# Copyright 2013 Giuseppe Venturini
# This file is part of python-deltasigma.
#
# python-deltasigma is a 1:1 Python replacement of Richard Schreier's
# MATLAB delta sigma toolbox (aka "delsigma"), upon which it is heavily based.
# The delta sigma toolbox is (c) 2009, Richard Schreier.
#
# python-deltasigma is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE file for the licensing terms.

"""Module providing configuration switches.
"""

import sys

# should synthesizeNTF run the optimization routine?
optimize_NTF = True

# how many iterations should be allowed in NTF synthesis?
# see synthesizeNTF() for more
itn_limit = 500

# debug
_debug = False

# setup_args for pyximport.install
setup_args = {"script_args":(["--compiler=mingw32"]
                             if sys.platform == 'win32' else [])}
