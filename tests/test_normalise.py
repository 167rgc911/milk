# -*- coding: utf-8 -*-
# Copyright (C) 2008, Luís Pedro Coelho <lpc@cmu.edu>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

from __future__ import division
import numpy

import milk.supervised.normalise

def test_interval_normalise():
    I=milk.supervised.normalise.interval_normalise()
    numpy.random.seed(1234)
    features=numpy.random.rand(20,100)
    L=numpy.zeros(100)
    I.train(features,L)
    assert numpy.all(numpy.abs( ( I(features).max(0)-I(features).min(0) ) - 2) < 1e-4)

def test_zscore_normalise():
    I=milk.supervised.normalise.zscore_normalise()
    numpy.random.seed(1234)
    features=numpy.random.rand(20,100)
    L=numpy.zeros(100)
    I.train(features,L)
    assert numpy.all( I(features).mean(0)**2 < 1e-7 )
    assert numpy.all( I(features).std(0) - 1 < 1e-3 )

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
