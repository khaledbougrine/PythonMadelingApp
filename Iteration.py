from numpy.fft import fftshift, fft

 # The value of N is missing in your code, so please provide the value

from numpy import zeros
from Structure import E_stat_1,E_stat_2,E_stat_3
from constants import N

B1_eta_1 = zeros(1, N)
A1_eta_1 = zeros(1, N)
B1_eta_2 = zeros(1, N)
A1_eta_2 = zeros(1, N)
B1_eta_3 = zeros(1, N)
A1_eta_3 = zeros(1, N)

A1_eta_1 = -B1_eta_1 * H_M + E_stat_1
a1_eta_1 = fftshift(fft(A1_eta_1))
b1_eta_1 = gumn * a1_eta_1
B1_eta_1 = fft(fftshift(b1_eta_1))

