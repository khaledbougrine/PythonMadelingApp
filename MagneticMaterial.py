import math

import numpy as np
from matplotlib import pyplot as plt


class MagneticMaterial:
    def __init__(self, freq):
        """

        :rtype: MagneticMaterial: 
        """
        self.alpha = 0.001
        self.omegaM = 28 * (1288E-4) / 4 * math.pi
        self.omegaO = 1.28 * self.omegaM + 1j * self.alpha * freq
        self.omega = freq
        self.Ms = (1288E-4)
        self.Ho = 1
        self.freq = freq
        self.k = 4E-7 * math.pi*self.calculate_k()
        self.mu = 4E-7 * math.pi*self.calculate_mu()
        self.epslon = 12
        self.mu_eff = (np.square(self.mu) - np.square(self.k)) / self.mu
        self.keff = (self.k * np.sqrt(self.epslon*np.abs(self.mu_eff)))



    def surface__impedance(self, mode):
        return

    def calculate_mu(self):
        return 1 + (self.omegaO * self.omegaM / (np.square(self.omegaO) - np.square(self.omega)))

    def calculate_k(self):
        return (self.omega * self.omegaM) / (np.square(self.omegaO) - np.square(self.omega))

    def printMu(self):
        plt.plot(self.freq, np.real(self.mu))
        plt.plot(self.freq, np.imag(self.mu))
        plt.show()

    def plot(self,y,name):
        plt.figure(figsize=(8, 6))
        plt.plot(self.freq, np.real(y), label='real')
        plt.plot(self.freq, np.imag(y), label='imag')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Magnetique Material '+name)
        plt.legend()
        plt.grid(True)
        plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
