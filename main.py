from numpy import sqrt
from numpy import pi
import constants

'''
Compute higher order low and high pass filters using 
Sallen Key Architecture.

Upto 10th order possible. Currently only allows even order filters.

Bessel, Butterworth and Chebyshev filters possible.
'''

# C2 > C1(4*b1)/a1^2
C2 = constants.C1*((4*constants.b)/(constants.a**2))

# C2 must be greater than C1(4*b1)/a1^2, so add 1nF
C2 += 10**-9

# Calculate R1 and R2
sqrt_term = sqrt(((constants.a**2)*(C2**2))-(4*constants.b*constants.C1*C2))
denominator = 4*pi*constants.fc*constants.C1*C2

R1 = ((constants.a*C2) - sqrt_term)/denominator
R2 = ((constants.a*C2) + sqrt_term)/denominator

print "Capacitors: ", constants.C1, C2
print "Resistors: ", R1, R2
