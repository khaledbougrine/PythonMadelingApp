import numpy as np
from matplotlib import pyplot as plt
from scipy.special import jv, jvp
from MagneticMaterial import *
from Rf.newMagnetiqueMaterial import *
from constants import *


def gammaint(R, epsf, mu, k, mueff, beta):
    # Frequency
    n = np.linspace(-(N - 1) / 2, (N - 1) / 2, N)
    z = (1j * jv(n, beta * R)) / (
            np.sqrt(EPSr / mueff) * (jvp(n, beta * R) + n * (k / mu) * (jv(n, beta * R) / (beta * R))))
    # taux = ((z - z0) / (z + z0))

    # zp = (1j * w * mueff * jv(n, arg)) / (keff * derivbesselj - (n * alpha) / (r * mu) * jv(n, arg))

    # return np.diag(zp)
    # plt.figure(figsize=(8, 6))
    # plt.plot(np.linspace(0,303,303), n, label='real')
    # plt.plot(ferrite.freq, np.imag(zp), label='imag')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Magnetique Material ')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    return z

def gammainInFunctionOfTheta(R, epsf, mu, k, mueff, beta,theta):
    # Frequency
    n = np.linspace(-(N - 1) / 2, (N - 1) / 2, N)
    z = ((1j * jv(n, beta * R)) / (
            np.sqrt(EPSr / mueff) * (jvp(n, beta * R) + n * (k / mu) * (jv(n, beta * R) / (beta * R))))) *np.exp(-1j*n*theta)
    taux = ((z - z0) / (z + z0))

    # zp = (1j * w * mueff * jv(n, arg)) / (keff * derivbesselj - (n * alpha) / (r * mu) * jv(n, arg))


    return taux


if __name__ == '__main__':
    # freq = np.linspace(2.5, 4.5, 200)

    taux = []

    # R = 250
    for fi in range(f.size):
        # for n in np.linspace(-(N - 1) / 2, (N - 1) / 2, N):
        gumn = gammainInFunctionOfTheta(R, EPSr, mu[fi], k[fi], mu_eff[fi], beta[fi],0)
        # gumn =  gammaint(R, EPSr, mu, k, mu_eff, k_eff, beta)
        taux.append(np.sum(gumn))

    np.savetxt('tauxImg.txt', np.real(taux))
    plt.plot(f, -20*np.log(np.abs(taux)), label='Treal')
    # plt.plot(f, np.imag(taux), label='im')
    result_resitance = [max(0, x) for x in np.real(taux)]

    # plt.plot(f, result_resitance, label='real')

    # plt.ylim(-1,1)
    plt.show()
