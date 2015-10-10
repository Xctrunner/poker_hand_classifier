"""
helpers.py
**********

A suite of useful helper functions for random number generation,
matrix and vector oprations, etc.

"""

import numpy

# Returns an array of x arrays with y random numbers from normal
# distribution
def randn(x, y):
    return numpy.random.randn(x, y)

# Temporary filler for numpy dot product
def dot(x,y):
    return numpy.dot(x, y)

# Temporary filler for numpy zeros function
# "Return a new array of given shape and type, filled with zeros"
def zeros(shape, dtype=float, order='C'):
    return numpy.zeros(shape, dtype, order)

# Placeholder for numpy argmax
# "Indices of the maximum values along an axis"
def argmax(a, axis=None):
    return numpy.argmax(a, axis)

# Placeholder for numpy vectorize
# "Define a vectorized function...blah"
def vectorize (pyfunc, otypes='', doc=None, excluded=None, 
               cache=False):
    return numpy.vectorize(pyfunc, otypes, doc, excluded, cache)






