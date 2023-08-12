# This is a sample Python script.
import cmath
import math
from xml.etree.ElementTree import PI

# Import math Library
import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
from scipy.special import jv, jvp


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def material():
    #  // val gamma = 1.12 // C/kg,
    # //val gamma = (28*U0)/1000;
    PI = m.pi
    EPSr = 15.3
    Ms = 0.175 / (4 * PI)  # // T
    omegaM = 25 * Ms  # // Ghg / Tesladerive
    alpha = 0.003
    omegaO = 1.25 * omegaM
    # omega = np.arange(0.1, 6, 0.001)
    omega = np.linspace(0.4, 1, 3000)  # Array of values at which to evaluate the function
    # omega = 2 * PI * freq
    print(omega)
    mu0 = 4 * m.pi * pow(10, 7)
    mu = mu0 * (1 + ((omegaO - 1j * alpha * omega) * omegaM) / (
            np.square(omegaO - 1j * alpha * omega) - np.square((omega))))
    k = mu0 * (omegaO - 1j * alpha * omega) * omegaM / (np.square(omegaO - 1j * alpha * omega) - np.square(omega))

    mu_eff = (np.square(mu) - np.square(k)) / mu
    beta = omega * np.sqrt(mu_eff * EPSr)
    # n = 1
    R = 5
    z = 0 * omega
    taux = 0 * omega
    z0 = 120 * m.pi
    E = lambda n: pow((1j), n) * jv(n, beta * R)
    H = lambda n: (1j / (omega * (np.square(mu) - np.square(k)))) * (
                mu * beta * jvp(n, beta * R) + ((k / R) * jv(n, beta * R)))
    Enew=E(0)
    Hnew=H(0)

    z1 = Enew / Hnew
    z1[np.isnan(z1)]=-1

    # for n in range(-30, 30):
    #     zn=(1j * jv(n, beta * R)) / (
    #             np.sqrt(EPSr / mu_eff) * (jvp(n, beta * R) + n * (k / mu) * (jv(n, beta * R) / (beta * R))))
    #     z = z +zn
    #     tauxn = (zn - z0) / (zn + z0)
    #     taux=taux+tauxn

    # bessel_values = jv(0, x)
    #
    # Compute the derivative of the Bessel function of the first kind
    # derivative_values = jvp(0, x)
    #
    fig, axs = plt.subplots(1, 2)
    axs[0].plot(omega, Enew, label='Zreal')
    # axs[0].plot(omega, z1.imag, label='Zimag')
    # plt.plot(omega, taux.real, label='Treal')
    # plt.plot(omega, taux.imag, label='Timag')
    axs[0].legend()

    axs[1].plot(omega, mu.real, label='Zreal')
    axs[1].plot(omega, mu.imag, label='Zimag')
    # plt.plot(omega, taux.real, label='Treal')
    # plt.plot(omega, taux.imag, label='Timag')
    # axs[1].legend()
    plt.tight_layout()
    plt.show()

    # plt.plot(omega, derivative_values.imag)
    # plt.plot(omega, derivative_values.real)


def surface_impedance():
    """

    """
    x = np.linspace(0, 15, 300)
    for v in range(0, 6):
        plt.plot(x, sp.jv(v, x))
    plt.show()


# def print_hi(name):
#     P = 300;
#     R = 1.2;
#
#     # delt_phi = 2 * pie / P;
#     x = np.arange(0, 5 * np.pi,
#                   0.01)  # Range of x values from 0 to 2*pi with a step of 0.01    defsource = [m.cos(i) for i in range(0, 2 * m.pi)]
#     y = np.cos(x)
#     plt.plot(x, y)
#     plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # material()
    # surface_impedance()
    fo = 4.2
    fm = 2.8
    f = np.linspace(5, 12, 3000)
    alpha = 0.01
    f0 = fo - 1j * alpha * f
    mu0 = 4 * m.pi * pow(10, -7)
    EPSr = 1
    mu = mu0 * (1 + ((f0 * fm) / (np.square(f0) - np.square(f))))
    k = mu0 * (fo - 1j * alpha * f) * fm / (np.square(fo - 1j * alpha * f) - np.square(f))

    mu_eff = (np.square(mu) - np.square(k)) / mu
    beta = 2 * m.pi * f * np.sqrt(mu_eff * EPSr)

    R = 2500
    modelist = np.arange(-151, 151)
    z0 = 120* math.pi
    z0=0.0000001*z0
    # zn=((1j * jv(n, beta * R)) / (
    #         np.sqrt(EPSr / mu_eff) * (jvp(n, beta * R) + n * (k / mu) * (jv(n, beta * R) / (beta * R)))))
    # taux=(zn-z0)/(zn+z0)
    taux = 0 * f
    # print(z0)
    z=0*f
    for n in modelist:
        z = (1j * jv(n, beta * R)) / (
                np.sqrt(EPSr / mu_eff) * (jvp(n, beta * R) + n * (k / mu) * (jv(n, beta * R) / (beta * R))))
        taux = taux + ((z - z0) / (z +z0))

    # plt.plot(f, taux.real, label='Zreal')
    # plt.plot(f, taux.imag, label='Zimag')
    plt.plot(f, abs(z), label='Treal')
    plt.plot(f, z.imag, label='Timag')

    fig, axs = plt.subplots(1, 2)
    axs[0].plot(f, z.imag, label='Zreal')
    axs[0].plot(f, z.real, label='Zimag')
    # plt.plot(omega, taux.real, label='Treal')
    # plt.plot(omega, taux.imag, label='Timag')
    axs[0].legend()

    axs[1].plot(f, taux.real, label='Treal')
    axs[1].plot(f, taux.imag, label='Timag')
    # plt.plot(omega, taux.real, label='Treal')
    # plt.plot(omega, taux.imag, label='Timag')
    # axs[1].legend()
    plt.tight_layout()
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/