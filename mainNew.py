import numpy as np
import matplotlib.pyplot as plt

from Rf.newGamma import gammaint

if __name__ == '__main__':

    # Definition of variables
    N = 360
    P = 360
    Ms = 330e3
    Hi = 350e3
    nu = 0.01
    n_pixel_s1 = 30
    Pixel_metal = int((P / 3) - n_pixel_s1)
    Hi = 350e3
    R = 0.0008
    delt_phi = 2 * np.pi / P
    largeur_source = n_pixel_s1 * delt_phi
    k = np.exp(1j * 2 * np.pi / 3)

    # Etat1
    E01_eta_1 = 1
    E02_eta_1 = 1
    E03_eta_1 = 1

    # Etat2
    E01_eta_2 = 1
    E02_eta_2 = k
    E03_eta_2 = np.conj(k)

    # Etat3
    E01_eta_3 = 1
    E02_eta_3 = np.conj(k)
    E03_eta_3 = k

    # Definition of the source
    larg_source1 = n_pixel_s1 * delt_phi
    p1 = np.arange(1, n_pixel_s1 + 1)
    V_ar_S = np.sqrt(R * delt_phi) * np.sin((np.pi * p1 * delt_phi) / larg_source1) * np.sinc(
        (np.pi * delt_phi) / (2 * larg_source1))
    V_ar_S_1 = np.concatenate((np.flip(V_ar_S[n_pixel_s1 // 2:], axis=0), V_ar_S[n_pixel_s1 // 2:]))

    plt.figure(1)
    plt.plot(np.abs(V_ar_S))

    # Source one
    E_source1_eta_1 = E01_eta_1 * V_ar_S

    # Source two
    E_source2_eta_1 = E02_eta_1 * V_ar_S_1
    E_source2_eta_2 = E02_eta_2 * V_ar_S_1
    E_source2_eta_3 = E02_eta_3 * V_ar_S_1

    # Source three
    E_source3_eta_1 = E03_eta_1 * V_ar_S_1
    E_source3_eta_2 = E03_eta_2 * V_ar_S_1
    E_source3_eta_3 = E03_eta_3 * V_ar_S_1

    # Vector of sources for Etat 1
    H_s1_eta_1 = np.concatenate((E_source1_eta_1, np.zeros(Pixel_metal), E_source2_eta_1, np.zeros(Pixel_metal),
                                 E_source3_eta_1, np.zeros(Pixel_metal)))

    # Vector of sources for Etat 2
    H_s1_eta_2 = np.concatenate((E_source1_eta_1, np.zeros(Pixel_metal), E_source2_eta_2, np.zeros(Pixel_metal),
                                 E_source3_eta_2, np.zeros(Pixel_metal)))

    # Vector of sources for Etat 3
    H_s1_eta_3 = np.concatenate((E_source1_eta_1, np.zeros(Pixel_metal), E_source2_eta_3, np.zeros(Pixel_metal),
                                 E_source3_eta_3, np.zeros(Pixel_metal)))

    H_M = np.concatenate((np.zeros(n_pixel_s1), np.ones(Pixel_metal), np.zeros(n_pixel_s1), np.ones(Pixel_metal),
                          np.zeros(n_pixel_s1), np.ones(Pixel_metal)))
    H_s = np.concatenate((np.ones(n_pixel_s1), np.zeros(Pixel_metal), np.ones(n_pixel_s1), np.zeros(Pixel_metal),
                          np.ones(n_pixel_s1), np.zeros(Pixel_metal)))
    H = H_M + H_s

    X_M12 = []
    X_M13 = []

    # Main loop
    f = np.arange(0.1e9, 3e10 + 1e9 / 50, 1e9 / 50)
    X_M = []
    z_0_1 = 200 * np.pi
    epsf = 14.2

    for freq in f:
        gumn = gammaint(freq, R, N, Hi, Ms, nu)
        z_0 = 120 * np.pi / np.sqrt(epsf)

        B1_eta_1 = np.zeros(N)
        B1_eta_2 = np.zeros(N)
        B1_eta_3 = np.zeros(N)

        A1_eta_1 = -B1_eta_1 * H_M - B1_eta_1 * H_s + (1 / np.sqrt(z_0)) * H_s1_eta_1
        a1_eta_1 = np.fft.fft(A1_eta_1)
        b1_eta_1 = gumn * a1_eta_1
        B1_eta_1 = np.fft.ifft(b1_eta_1)

        A1_eta_2 = -B1_eta_2 * H_M - B1_eta_2 * H_s + (1 / np.sqrt(z_0)) * H_s1_eta_2
        a1_eta_2 = np.fft.fft(A1_eta_2)
        b1_eta_2 = gumn * a1_eta_2
        B1_eta_2 = np.fft.ifft(b1_eta_2)

        A1_eta_3 = -B1_eta_3 * H_M - B1_eta_3 * H_s + (1 / np.sqrt(z_0)) * H_s1_eta_3
        a1_eta_3 = np.fft.fft(A1_eta_3)
        b1_eta_3 = gumn * a1_eta_3
        B1_eta_3 = np.fft.ifft(b1_eta_3)

    E1_eta1 = np.sqrt(z_0) * (A1_eta_1 + B1_eta_1)
    J1_eta1 = (1 / np.sqrt(z_0)) * (A1_eta_1 - B1_eta_1)

    E1_eta2 = np.sqrt(z_0) * (A1_eta_2 + B1_eta_2)
    J1_eta2 = (1 / np.sqrt(z_0)) * (A1_eta_2 - B1_eta_2)

    E1_eta3 = np.sqrt(z_0) * (A1_eta_3 + B1_eta_3)
    J1_eta3 = (1 / np.sqrt(z_0)) * (A1_eta_3 - B1_eta_3)

    y_in_eta_1 = np.sum(np.conj(E1_eta1[:n_pixel_s1]) * J1_eta1[:n_pixel_s1]) / np.sum(
        np.conj(E1_eta1[:n_pixel_s1]) * E1_eta1[:n_pixel_s1])
    y_in_eta_2 = np.sum(np.conj(E1_eta2[:n_pixel_s1]) * J1_eta2[:n_pixel_s1]) / np.sum(
        np.conj(E1_eta2[:n_pixel_s1]) * E1_eta2[:n_pixel_s1])
    y_in_eta_3 = np.sum((np.conj(E1_eta3[:n_pixel_s1]) * J1_eta3[:n_pixel_s1]) / np.sum(
        np.conj(E1_eta3[:n_pixel_s1]) * E1_eta3[:n_pixel_s1]))

    Y_M_p = np.array([[y_in_eta_1, 0, 0], [0, y_in_eta_2, 0], [0, 0, y_in_eta_3]])
    P_M = np.array([[1, 1, 1], [1, k, np.conj(k)], [1, np.conj(k), k]])

    Y_M = np.linalg.inv(P_M) @ Y_M_p @ P_M
    S_M = (np.eye(3) - Y_M * z_0_1) @ np.linalg.inv(np.eye(3) + Y_M * z_0_1)

    X_M13.append(S_M[0, 2])
    X_M12.append(S_M[0, 1])
    X_M.append(S_M[0, 0])

plt.figure(4)
plt.plot(f, 20 * np.log10(np.abs(X_M)), 'g-', linewidth=2)
plt.hold(True)
plt.plot(f, 20 * np.log10(np.abs(X_M12)), 'r-', linewidth=2)
plt.hold(True)
plt.plot(f, 20 * np.log10(np.abs(X_M13)), 'b-.', linewidth=2)
plt.xlabel('Frequency (GHz)')
plt.legend(['S11(dB)', 'S21(dB)', 'S31(dB)'])
plt.show()
