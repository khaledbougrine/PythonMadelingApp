import numpy as np
import matplotlib.pyplot as plt
from hysteresis import Hysteresis

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt


    def jiles_atherton_model(H, M_prev, alpha, a, Ms, k):
        """Jiles-Atherton model for hysteresis simulation."""
        delta_M = 2 * alpha * np.tanh((H - a * M_prev) / (2 * k))
        M = M_prev + delta_M
        return M


    # Material properties
    alpha = 0.1
    a = 1.0
    Ms = 1.2
    k = 0.2

    # Magnetic field range
    H = np.linspace(-1.5, 1.5, 100)  # Tesla

    # Initialize magnetization
    M_prev = np.zeros_like(H)

    # Calculate magnetization (M) using Jiles-Atherton model
    M = np.zeros_like(H)
    for i in range(len(H)):
        M[i] = jiles_atherton_model(H[i], M_prev[i], alpha, a, Ms, k)
        M_prev[i] = M[i]

    # Plotting the hysteresis loop
    plt.plot(H, M)
    plt.xlabel('Magnetic Field (H) [T]')
    plt.ylabel('Magnetization (M) [T]')
    plt.title('Magnetic Hysteresis Loop (Jiles-Atherton Model)')
    plt.grid(True)
    plt.show()



