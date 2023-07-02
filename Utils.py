import numpy as np
from matplotlib import pyplot as plt


def plot( x,y, name):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='real')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Magnetique Material ' + name)
    plt.legend()
    plt.grid(True)
    plt.show()