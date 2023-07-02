import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jvp


def surface__impedance(mode, manetiqueMaterial):
    freq = manetiqueMaterial.freq
    n=mode

    # Calculate the Bessel function values
    bessel = jv(mode, freq)

    # Calculate the derivative of the Bessel function
    Dbessel = jvp(mode, freq)

    Zn=()


    # Plot the Bessel function and its derivative

