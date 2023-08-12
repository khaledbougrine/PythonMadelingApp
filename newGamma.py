import numpy as np
from matplotlib import pyplot as plt
from scipy.special import jv, jvp

from Rf.constants import f


def gammaint(f, R, N, Hi, Ms, nu):
    c = 3e8
    w = 2 * np.pi * f
    mu0 = 4 * np.pi * 1e-7
    gamma = 2 * np.pi * 28 * 1e9
    wm = gamma * Ms * mu0
    w0 = gamma * mu0 * Hi + 1j * w * nu
    mu = mu0 * (1 + (wm * w0) / (w0 ** 2 - w ** 2))
    alpha = mu0 * (wm * w) / (w0 ** 2 - w ** 2)
    eps0 = 8.854 * 1e-12
    epsf = 14.6
    lamda = c / f
    mueff = (mu ** 2 - alpha ** 2) / mu
    keff = w * np.sqrt(eps0 * epsf * mueff)
    z0 = 120 * np.pi
    r = R
    arg = keff * r
    n = np.arange(-N / 2, N / 2)
    derivbesselj = jvp(n, arg, 1)
    zp = (1j * w * mueff * jv(n, arg)) / (keff * derivbesselj - ((n * alpha) / (r * mu)) * jv(n, arg))
    gumn_1 = (zp - z0) / (zp + z0)

    gumn_2 = np.isnan(gumn_1)
    gumn_I = np.zeros_like(gumn_1)
    for p in range(len(gumn_1)):
        if gumn_2[p] == 1:
            gumn_I[p] = -1
        else:
            gumn_I[p] = gumn_1[p]

    gumn = gumn_I

    return gumn

