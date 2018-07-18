"""
Test Extra seawater functions
=============================

"""

from __future__ import (absolute_import, division, print_function)

import numpy as np

from oceans.sw_extras import kdpar


def test_kdpar():
    PAR = np.array([389.26, 386.87, 290.69, 255.38, 205.28, 190.75,
                    147.05, 132.05, 112.98, 94.934, 78.192, 66.81,
                    61.349, 55.656, 51.565, 47.069, 42.757, 38.276,
                    34.579, 32.528, 30.307, 27.983, 25.576, 23.55,
                    21.878, 20.429, 19.056, 17.693, 16.243, 14.972,
                    13.858, 12.878, 12.006, 11.184, 10.433, 9.7273,
                    9.1282, 8.5659, 7.971, 7.4218, 6.9186, 6.4537,
                    6.0647, 5.7409, 5.45, 5.1376, 4.8125, 4.5047,
                    4.205, 3.945, 3.7025, 3.5075, 3.32, 3.1387,
                    2.9669, 2.8028, 2.6287, 2.4715, 2.3288, 2.204,
                    2.109, 2.0086, 1.9032, 1.803, 1.7002, 1.6024,
                    1.519, 1.4352, 1.3614, 1.2887, 1.2239, 1.1609,
                    1.1003, 1.0465, 0.9971])

    press = np.array([5.,   6.,   7.,   8.,   9.,  10.,  11.,  12.,  13.,
                      14.,  15., 16.,  17.,  18.,  19.,  20.,  21.,  22.,
                      23.,  24.,  25.,  26., 27.,  28.,  29.,  30.,  31.,
                      32.,  33.,  34.,  35.,  36.,  37., 38.,  39.,  40.,
                      41.,  42.,  43.,  44.,  45.,  46.,  47.,  48., 49.,
                      50.,  51.,  52.,  53.,  54.,  55.,  56.,  57., 58.,
                      59., 60.,  61.,  62.,  63.,  64.,  65.,  66.,  67.,
                      68.,  69.,  70., 71.,  72.,  73.,  74.,  75.,  76.,
                      77.,  78.,  79.])

    kd, par_surface = kdpar(press, PAR,  boundary=25)
    np.testing.assert_almost_equal(kd, 0.13808412818017926)
    np.testing.assert_almost_equal(par_surface, 690.61656440966783)
