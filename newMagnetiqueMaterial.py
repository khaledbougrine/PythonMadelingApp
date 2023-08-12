# Import math Library
import math as m
import numpy as np
import matplotlib.pyplot as plt
from constants import f
import scipy.special as sp
from scipy.special import jv, jvp

fo = 4.2       #  Ghz
fm = 2.8
alpha = 0.035
f0 = fo - 1j * alpha * f
mu0 = 4 * m.pi * pow(10, -7)
EPSr = 16
mu = mu0 * (1 + ((f0 * fm) / (np.square(f0) - np.square(f))))
k = mu0 * (fo - 1j * alpha * f) * fm / (np.square(fo - 1j * alpha * f) - np.square(f))
mu_eff = (np.square(mu) - np.square(k)) / mu
beta = 2 * m.pi * f * np.sqrt(mu_eff * EPSr)
k_eff = (k * np.sqrt(EPSr * np.abs(mu_eff)))


def printMu():
    plt.plot(f, np.real(mu))
    plt.plot(f, np.imag(mu))
    plt.show()


def plot(y, name):
    plt.figure(figsize=(8, 6))
    plt.plot(f, np.real(y), label='real')
    plt.plot(f, np.imag(y), label='imag')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Magnetique Material ' + name)
    plt.legend()
    plt.grid(True)
    plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    plot(mu,"k")


    # Ms = 160e3
    # Hi = 240e3
    # nu = 0.01
    # R = 0.002
    # gumn = gammaint(freq, R, Hi, Ms, nu, magnetiqueMaterial)
