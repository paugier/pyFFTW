#!/usr/bin/env python
# The pyfftw namespace

''' The core of ``pyfftw`` consists of the :class:`FFTW` class, 
:ref:`wisdom functions <wisdom_functions>` and a couple of
:ref:`utility functions <utility_functions>` for dealing with aligned
arrays.

This module represents the full interface to the underlying `FFTW
library <http://www.fftw.org/>`_. However, users may find it easier to
use the helper routines provided in :mod:`pyfftw.builders`.
'''

from pyfftw import (
        FFTW,
        export_wisdom,
        import_wisdom,
        forget_wisdom,
        n_byte_align_empty,
        n_byte_align,)

import builders

# clean up the namespace
del builders.builders
del builders._utils

#from np_fft import *
