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

from radarsimpy import Transmitter, Receiver, Radar
from .test_transmitter import cw_tx, fmcw_tx, tdm_fmcw_tx, pmcw_tx
from .test_receiver import cw_rx, fmcw_rx, tdm_fmcw_rx, pmcw_rx

import scipy.constants as const
import numpy as np
import numpy.testing as npt


def cw_radar():
    return Radar(transmitter=cw_tx(), receiver=cw_rx())


def test_cw_radar():
    cw = cw_radar()

    assert cw.samples_per_pulse == 10 * 20
    assert cw.channel_size == 1
    assert np.array_equal(cw.virtual_array, np.array([[0, 0, 0]]))


def fmcw_radar():
    return Radar(
        transmitter=fmcw_tx(),
        receiver=fmcw_rx(),
        time=[0, 1])


def test_fmcw_radar():
    fmcw = fmcw_radar()

    assert fmcw.samples_per_pulse == 80e-6 * 2e6
    assert fmcw.channel_size == 1
    assert np.array_equal(fmcw.virtual_array, np.array([[0, 0, 0]]))


def tdm_fmcw_radar():
    return Radar(transmitter=tdm_fmcw_tx(),
                 receiver=tdm_fmcw_rx())


def test_tdm_fmcw_radar():
    half_wavelength = const.c / 24.125e9 / 2
    tdm = tdm_fmcw_radar()

    assert tdm.samples_per_pulse == 80e-6 * 2e6
    assert tdm.channel_size == 16
    npt.assert_almost_equal(tdm.virtual_array,
                            np.array([[0, -8*half_wavelength, 0],
                                      [0, -7*half_wavelength, 0],
                                      [0, -6*half_wavelength, 0],
                                      [0, -5*half_wavelength, 0],
                                      [0, -4*half_wavelength, 0],
                                      [0, -3*half_wavelength, 0],
                                      [0, -2*half_wavelength, 0],
                                      [0, -1*half_wavelength, 0],
                                      [0, 0*half_wavelength, 0],
                                      [0, 1*half_wavelength, 0],
                                      [0, 2*half_wavelength, 0],
                                      [0, 3*half_wavelength, 0],
                                      [0, 4*half_wavelength, 0],
                                      [0, 5*half_wavelength, 0],
                                      [0, 6*half_wavelength, 0],
                                      [0, 7*half_wavelength, 0]]))


def pmcw_radar():
    code1 = np.array(
        [1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1,
         1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1,
         1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1,
         -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1,
         1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1,
         1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1,
         1, 1, -1, -1, 1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1,
         -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1,
         -1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, 1,
         1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1,
         1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1,
         -1, -1, 1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1,
         -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1,
         -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1,
         1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1,
         1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1])
    code2 = np.array(
        [1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1,
         -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1,
         -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1,
         -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1,
         1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1,
         -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1,
         1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1,
         1, 1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1,
         -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1,
         -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1,
         1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1,
         1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1,
         -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1,
         -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1,
         1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1,
         -1, -1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1])
    return Radar(transmitter=pmcw_tx(code1, code2), receiver=pmcw_rx())


def test_pmcw_radar():
    pmcw = pmcw_radar()

    assert pmcw.samples_per_pulse == 2.1e-6 * 250e6
    assert pmcw.channel_size == 2
    assert np.array_equal(pmcw.virtual_array,
                          np.array([[0, 0, 0],
                                    [0, 0, 0]]))