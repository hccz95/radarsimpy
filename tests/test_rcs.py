"""
    A Python module for radar simulation

    ----------
    RadarSimPy - A Radar Simulator Built with Python
    Copyright (C) 2018 - PRESENT  Zhengyu Peng
    E-mail: zpeng.me@gmail.com
    Website: https://zpeng.me

    `                      `
    -:.                  -#:
    -//:.              -###:
    -////:.          -#####:
    -/:.://:.      -###++##:
    ..   `://:-  -###+. :##:
           `:/+####+.   :##:
    .::::::::/+###.     :##:
    .////-----+##:    `:###:
     `-//:.   :##:  `:###/.
       `-//:. :##:`:###/.
         `-//:+######/.
           `-/+####/.
             `+##+.
              :##:
              :##:
              :##:
              :##:
              :##:
               .+:

"""

import numpy as np
import numpy.testing as npt

from radarsimpy.rt import rcs_sbr


def test_rcs_momostatic():
    phi = 0
    theta = 90
    freq = np.array([1e9, 3e9])
    pol = np.array([0, 0, 1])
    density = 1
    rcs = np.zeros_like(freq)
    for f_idx, f in enumerate(freq):
        rcs[f_idx] = 10*np.log10(
            rcs_sbr('./models/plate5x5.stl', f,
                    phi, theta, pol=pol, density=density))

    npt.assert_almost_equal(rcs, np.array([48.3, 59.2]), decimal=1)


def test_rcs_bistatic():
    phi = np.array([-30, -24, 65])
    theta = 90

    inc_phi = 30
    inc_theta = 90

    freq = 1e9
    pol = np.array([0, 0, 1])
    density = 1
    rcs = np.zeros_like(phi)
    for phi_idx, phi_ang in enumerate(phi):
        rcs[phi_idx] = 10*np.log10(
            rcs_sbr('./models/plate5x5.stl', freq,
                    phi_ang, theta, inc_phi=inc_phi, inc_theta=inc_theta,
                    pol=pol, density=density))

    npt.assert_almost_equal(rcs, np.array([47, 34, 6]), decimal=0)