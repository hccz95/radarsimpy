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


import radarsimpy.processing as proc
import numpy as np
import numpy.testing as npt


def test_ca_cfar():
    sig = np.ones((2, 32))
    sig[0, 16] = 20
    sig[1, 10] = 30

    ca_cfar = proc.cfar_ca_1d(sig, guard=2, trailing=10, pfa=1e-2, axis=1)

    npt.assert_almost_equal(
        ca_cfar[0, :],
        np.array([
            2.58925412,  2.58925412,  2.58925412,  2.84817953,  8.02668777,
            8.28561318,  8.54453859,  8.803464,  9.06238941,  9.32131482,
            9.58024024,  9.83916565, 10.09809106, 10.09809106,  5.17850824,
            5.17850824,  5.17850824,  5.17850824,  5.17850824, 10.09809106,
            9.83916565,  9.58024024,  9.32131482,  9.06238941,  8.803464,
            8.54453859,  8.28561318,  8.02668777,  7.76776235,  2.58925412,
            2.58925412,  2.58925412]), decimal=3)
    npt.assert_almost_equal(
        ca_cfar[1, :],
        np.array([
            10.09809106, 10.09809106, 10.09809106, 10.35701647, 10.61594188,
            10.8748673, 11.13379271, 11.39271812,  4.14280659,  4.401732,
            4.66065741,  4.91958282,  5.17850824, 12.68734518, 12.68734518,
            12.68734518, 12.68734518, 12.68734518, 12.68734518, 12.68734518,
            12.42841977, 12.16949435, 11.91056894,  4.14280659,  3.88388118,
            3.62495577,  3.36603035,  3.10710494,  2.84817953,  2.58925412,
            2.58925412,  2.58925412]), decimal=3)

    sig = np.ones((32, 2))
    sig[16, 0] = 20
    sig[10, 1] = 30

    ca_cfar = proc.cfar_ca_1d(sig, guard=2, trailing=10, pfa=1e-2, axis=0)

    npt.assert_almost_equal(
        ca_cfar[:, 0],
        np.array([
            2.58925412,  2.58925412,  2.58925412,  2.84817953,  8.02668777,
            8.28561318,  8.54453859,  8.803464,  9.06238941,  9.32131482,
            9.58024024,  9.83916565, 10.09809106, 10.09809106,  5.17850824,
            5.17850824,  5.17850824,  5.17850824,  5.17850824, 10.09809106,
            9.83916565,  9.58024024,  9.32131482,  9.06238941,  8.803464,
            8.54453859,  8.28561318,  8.02668777,  7.76776235,  2.58925412,
            2.58925412,  2.58925412]), decimal=3)
    npt.assert_almost_equal(
        ca_cfar[:, 1],
        np.array([
            10.09809106, 10.09809106, 10.09809106, 10.35701647, 10.61594188,
            10.8748673, 11.13379271, 11.39271812,  4.14280659,  4.401732,
            4.66065741,  4.91958282,  5.17850824, 12.68734518, 12.68734518,
            12.68734518, 12.68734518, 12.68734518, 12.68734518, 12.68734518,
            12.42841977, 12.16949435, 11.91056894,  4.14280659,  3.88388118,
            3.62495577,  3.36603035,  3.10710494,  2.84817953,  2.58925412,
            2.58925412,  2.58925412]), decimal=3)


def test_os_cfar():
    sig = np.ones((2, 32))
    sig[0, 16] = 20
    sig[1, 10] = 30

    os_cfar = proc.cfar_os_1d(sig, guard=0, trailing=4, k=6, pfa=1e-2, axis=1)

    npt.assert_almost_equal(
        os_cfar[0, :],
        np.array([
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834]), decimal=3)
    npt.assert_almost_equal(
        os_cfar[1, :],
        np.array([
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834]), decimal=3)

    sig = np.ones((32, 2))
    sig[16, 0] = 20
    sig[10, 1] = 30

    os_cfar = proc.cfar_os_1d(sig, guard=0, trailing=4, k=6, pfa=1e-2, axis=0)

    npt.assert_almost_equal(
        os_cfar[:, 0],
        np.array([
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834]), decimal=3)
    npt.assert_almost_equal(
        os_cfar[:, 1],
        np.array([
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834, 5.86979834, 5.86979834, 5.86979834,
            5.86979834, 5.86979834]), decimal=3)
