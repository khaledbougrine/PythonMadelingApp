import numpy as np
from matplotlib import pyplot as plt
from scipy.special import jv, jvp
from MagneticMaterial import *
from constants import N


def gammaint(f, R, Hi, Ms, nu, ferrite):
    # Frequency
    c = 3e8
    w = 2 * np.pi * f

    # Permeability
    mu0 = 4 * np.pi * 1e-7

    # Magnetization and fields
    gamma = 2 * np.pi * 28e9
    wm = ferrite.omegaM
    w0 = ferrite.omegaO
    mu = ferrite.mu
    alpha = ferrite.k

    # Permittivity
    eps0 = 8.854e-12
    epsf = 14.6

    # Radius
    lamda = c / f

    # Coefficients
    mueff = ferrite.mu_eff
    keff = ferrite.keff
    print( keff)
    print(mueff)


    z0 = 120 * np.pi*pow(10,-12)
    # zo=50
    r = R
    arg = keff * r

    # n = np.arange(-(N // 2), N // 2)
    # n = np.ones(N)
    n=np.linspace(-(N-1)/2,(N-1)/2,N)
    derivbesselj = jvp(n, arg)
    besselj = jv(n, arg)
    # zp = (1j * w * mueff * jv(n, arg)) / (keff * derivbesselj - (n * alpha) / (r * mu) * jv(n, arg))
    zp1 = (1j * besselj)
    zp2= (np.sqrt(epsf / mueff) * (derivbesselj * n * (alpha / mu) * (besselj / arg)))
    zp=(zp1)/(zp2)
    # return np.diag(zp)
    print(zp)
    # plt.figure(figsize=(8, 6))
    # plt.plot(np.linspace(0,303,303), n, label='real')
    # plt.plot(ferrite.freq, np.imag(zp), label='imag')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Magnetique Material ')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    gamma=(50-zp)/(50+zp)
    return gamma

    # gumn_2 = np.isnan(gumn_1)

    # gumn_I = np.where(gumn_2, -1, gumn_1)
    #
    # gumn = gumn_I
if __name__ == '__main__':
    # freq = np.linspace(2.5, 4.5, 200)
    freq=2.5
    magnetiqueMaterial = MagneticMaterial(freq)
    Ms = 160e3
    Hi = 240e3
    nu = 0.01
    R = 0.002
    gumn = gammaint(freq, R, Hi, Ms, nu, magnetiqueMaterial)



