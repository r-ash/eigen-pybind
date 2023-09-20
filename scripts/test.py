import example
import numpy as np

import pytest

# Note that this test uses pybind11 module example which is built
# into the "build" directory. If you want to run this test run it
# via ./scripts/test which will set up the location so that
# this can be run.
# I need to work out how to make this properly making the C++ module
# available to the rest of the python module but not quite sure how to do
# that yet.

def test_add():
    assert example.add(1, 2) == 3


def test_add_eigen():
    # Eigen tensors by default are column major
    # But numpy uses row major by default. Have to force them to use
    # column major to pass this as a reference

    a = np.array([[1., 2., 3.],
                  [4., 5., 6.]],
                 order = 'F')
    b = np.array([[9., 8., 7.],
                  [6., 5., 4.]],
                 order = 'F')
    res = np.array([[10., 10., 10.],
                    [10., 10., 10.]],
                   order = 'F')

    assert (example.add_tensor(a, b) == res).all()

