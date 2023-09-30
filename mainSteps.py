# This is a sample Python script.

from MagneticMaterial import *
from Structure import *
from Utils import plot
from gamma_int import *
from constants import *
from Rf.newMagnetiqueMaterial import *
if __name__ == '__main__':
    # Ms = 160e3
    # Hi = 240e3
    # nu = 0.01
    # R = 0.002
    # z_0=50
    #
    B1_eta_1 = np.zeros(N)
    B1_eta_2 = np.zeros(N)
    B1_eta_3 = np.zeros(N)

    print('B1_eta_1++++++++++++++++++++++++')
    print(B1_eta_1)

    B_M1 = []

    z0 = 50
    z_0 = 50

    for fi in range(f.size):
        # magnetiqueMaterial = MagneticMaterial(f)
        # magnetiqueMaterial.printMu()
        # magnetiqueMaterial.plot(magnetiqueMaterial.mu_eff,'mueff')
        # magnetiqueMaterial.plot(magnetiqueMaterial.keff,'keff')
        # gumn = gammaint(f, R, Hi, Ms, nu, magnetiqueMaterial)
        gumn = gammaint( R, EPSr,mu[fi],k[fi],mu_eff[fi],beta[fi])

        # Calculate A1_eta_1
        A1_eta_1 = -B1_eta_1 + (1/np.sqrt((z_0)))* E_stat_1
        # print('B1_eta_1')
        # print(B1_eta_1)
        #
        # print('H_M')
        # print(H_M)
        # print('E_stat_1')
        # print(E_stat_1)
        a1_eta_1 = np.fft.fft(A1_eta_1)
        b1_eta_1 = gumn * a1_eta_1
        B1_eta_1 = np.fft.ifft(b1_eta_1)
        B_M1.append(np.sum(B1_eta_1))
    plot(B_M1,'')
