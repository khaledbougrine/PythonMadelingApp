import math

import numpy as np
from numpy import zeros, ones

from Utils import plot
from constants import *

Circulator = np.linspace(1, P, P)
z_0 = 50
R = 0.002
FONT_SIZE_PIXEL = 30
METAL_SIZE_PIXEL = int(((P / 3) - (FONT_SIZE_PIXEL)))
FONT = np.linspace(1, FONT_SIZE_PIXEL, FONT_SIZE_PIXEL)
METAL = np.linspace(1, METAL_SIZE_PIXEL, METAL_SIZE_PIXEL)

FONT_SIZE_RAD = FONT_SIZE_PIXEL * DELTA_PHI


def V_ar_SOURCE():
    V_ar_S = np.sqrt(R * DELTA_PHI) * np.sin((PI * FONT * DELTA_PHI) / FONT_SIZE_RAD) * np.sinc(
        PI * DELTA_PHI / (2 * FONT_SIZE_RAD))
    return V_ar_S


def V_ar_METAL():
    # print(0*METAL)
    # print(V_ar_SOURCE())
    return 0 * METAL


H_s = np.concatenate((0 * V_ar_SOURCE() + 1, 0 * V_ar_METAL(), 0 * V_ar_SOURCE() + 1, 0 * V_ar_METAL(),
                      0 * V_ar_SOURCE() + 1, V_ar_METAL() * 0), axis=0)
H_M = np.concatenate((0 * V_ar_SOURCE(), 0 * V_ar_METAL() + 1, 0 * V_ar_SOURCE(), 0 * V_ar_METAL() + 1,
                      0 * V_ar_SOURCE(), 0 * V_ar_METAL() + 1), axis=0)

E_stat_1 = (1 / math.sqrt((z_0))) * np.concatenate(
    (V_ar_SOURCE(), V_ar_METAL(), V_ar_SOURCE(), V_ar_METAL(), V_ar_SOURCE(), V_ar_METAL()), axis=0)
E_stat_2 = (1 / math.sqrt((z_0))) * np.concatenate(
    (V_ar_SOURCE(), V_ar_METAL(), KVar * V_ar_SOURCE(), V_ar_METAL(), conjK * V_ar_SOURCE(), V_ar_METAL()),
    axis=0)
E_stat_3 = (1 / math.sqrt((z_0))) * np.concatenate(
    (V_ar_SOURCE(), V_ar_METAL(), conjK * V_ar_SOURCE(), V_ar_METAL(), KVar * V_ar_SOURCE(), V_ar_METAL()),
    axis=0)

if __name__ == '__main__':
    print(V_ar_SOURCE())
    print(E_stat_2)
