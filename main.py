# This is a sample Python script.

from MagneticMaterial import *
from Structure import *
from Utils import plot
from gamma_int import *
from constants import *

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Ms = 160e3
    Hi = 240e3
    nu = 0.01
    R = 0.002
    z_0=50
    #
    B1_eta_1 = np.zeros(N)
    B1_eta_2 = np.zeros(N)
    B1_eta_3 = np.zeros(N)

    print('B1_eta_1++++++++++++++++++++++++')
    print(B1_eta_1)

    freq = np.linspace(2, 8, 200)
    X_M13 = []
    X_M11 = []
    X_M12 = []


    for f in freq:
        magnetiqueMaterial = MagneticMaterial(f)
        # magnetiqueMaterial.printMu()
        # magnetiqueMaterial.plot(magnetiqueMaterial.mu_eff,'mueff')
        # magnetiqueMaterial.plot(magnetiqueMaterial.keff,'keff')
        gumn = gammaint(f, R, Hi, Ms, nu, magnetiqueMaterial)
        # Calculate A1_eta_1
        A1_eta_1 = -B1_eta_1 + (1/np.sqrt((z_0)))* E_stat_1
        print('B1_eta_1')
        print(B1_eta_1)

        print('H_M')
        print(H_M)
        print('E_stat_1')
        print(E_stat_1)
        a1_eta_1 = np.fft.fft(A1_eta_1)
        b1_eta_1 = gumn * a1_eta_1
        B1_eta_1 = np.fft.ifft(b1_eta_1)

        # Calculate A1_eta_2
        A1_eta_2 = -B1_eta_2 * H_M + (1/np.sqrt((z_0)))*E_stat_2
        a1_eta_2 = np.fft.fft(A1_eta_2)
        b1_eta_2 = gumn * a1_eta_2
        B1_eta_2 = np.fft.ifft(b1_eta_2)

        # Calculate A1_eta_3
        A1_eta_3 = -B1_eta_3 * H_M + (1/np.sqrt((z_0)))* E_stat_3
        a1_eta_3 = np.fft.fftshift(np.fft.fft(A1_eta_3))
        b1_eta_3 = gumn * a1_eta_3
        B1_eta_3 = np.fft.ifft(np.fft.fftshift(b1_eta_3))

        # ****champ electrique pour l'?tat1
        E1_eta1 =(np.sqrt((z_0)))*(A1_eta_1 + B1_eta_1)
        # densit? du courant pour l'?tat1
        J1_eta1 = (1/np.sqrt((z_0)))*(A1_eta_1 - B1_eta_1)
        # ********************************************
        # champ electrique pour l'?tat2
        E1_eta2 = (np.sqrt((z_0)))* (A1_eta_2 + B1_eta_2)
        # densit? du courant pour l'?tat2
        J1_eta2 = (1/np.sqrt((z_0)))* (A1_eta_2 - B1_eta_2)
        # ********************************************
        # champ electrique pour l'?tat3
        E1_eta3 = (np.sqrt((z_0)))*(A1_eta_3 + B1_eta_3)
        # densit? du courant pour l'?tat2
        J1_eta3 = (1/np.sqrt((z_0)))*(A1_eta_3 - B1_eta_3)

        # /////////calcul des admmittances vue par la source pour chaque ?tats
        # admittance modal pour l'?ta_1
        y_in_eta_1 = np.sum(np.conj(E1_eta1) * J1_eta1 * H_s) / np.sum(np.conj(E1_eta1) * E1_eta1 * H_s)
        # calcul de S1
        S1 = (-1 + z_0*y_in_eta_1) / (1 + z_0*y_in_eta_1)
        # admittance modal pour l'?ta_2
        y_in_eta_2 = np.sum(np.conj(E1_eta2) * J1_eta2 * H_s) / np.sum(np.conj(E1_eta2) * E1_eta2 * H_s)
        # calcul de S2
        S2 = (-1 + z_0*y_in_eta_2) / (1 +  z_0*y_in_eta_2)
        # admittance modal pour l'?ta_3
        y_in_eta_3 = np.sum(np.conj(E1_eta3) * J1_eta3 * H_s) / np.sum(np.conj(E1_eta3) * E1_eta3 * H_s)
        # calcul de S2
        S3 = (-1 + z_0*y_in_eta_3) / (1 + z_0* y_in_eta_3)
        # *******somme moyenne de S_M1=1/3(S1+S2+S3)

        S_M = (S1 + S2 + S3)
        S_M12 = (S1 + conjK * S2 + K * S3)
        S_M13 = (S1 + K * S2 + conjK * S3)

        # % *****Vecteur S_M en fonction de la fr?quence
        X_M13.append(S_M13)
        X_M12.append(S_M12)
        X_M11.append(S_M)


    # Create figure
    np.savetxt('vector.txt', X_M11)

    # Create axes
    plt.figure(figsize=(8, 6))
    plt.plot(freq,np.log10(np.abs(X_M13)) , label='imag')
    plt.plot(freq,np.log10(np.abs(X_M11)) , label='ff')
    plt.plot(freq,np.log10(np.abs(X_M12)) , label='12')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Magnetique Material ')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Show the plot

    # plot(Circulator,E1,'source1')
    # plot(Circulator,E2,'source2')
    # plot(Circulator,E3,'source3')
    # V_ar_METAL()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
