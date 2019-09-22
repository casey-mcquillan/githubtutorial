'''
This file is a script that solves for the steady-state in the two-
period-lived overlapping generations model given some parameter values.
'''

# Put import commands below here
<<<<<<< HEAD
import FirmsMC
import household
import euler
=======

import euler
import FirmsMC
import household
import numpy as np
>>>>>>> upstream/master

# Set parameter values

# Household parameters
n1 = 1.0
n2 = 0.2
nvec = np.array([n1, n2])
gamma = 2.2
beta_an = 0.96
<<<<<<< HEAD
beta = beta_an ** (30)

# Firm parameters
A = 1.0
alpha = 0.33
delta_an = 0.05
delta = delta_an ** (30)
=======
beta = beta_an ** 30

# Firm parameters
A = 1.0
alpha = 0.35
delta_an = 0.05
delta = 1 - (1 - delta_an) ** (30)
>>>>>>> upstream/master

args = nvec, alpha, A, delta, beta, gamma

args = 

<<<<<<< HEAD
# Solve for b2 given parameters
b2 = euler.get_b2(args)

=======
b2 = euler.get_b2(args)
>>>>>>> upstream/master


# Solve for all the other endogenous variables given parameter values
# and optimal b2

<<<<<<< HEAD

K = FirmsMC.get_K(b2)
L = FirmsMC.get_L(nvec)

w = FirmsMC.get_w(b2, args)
r = FirmsMC.get_r(b2, args)

c1 = household.get_c1(b2, args)
c2 = household.get_c2(b2, args)





=======
c1 = household.get_c1(b2, args)
c2 = household.get_c2(b2, args)
r = FirmsMC.get_r(b2, args)
w = FirmsMC.get_w(b2, args)
k = FirmsMC.get_K(b2)
l = FirmsMC.get_L(nvec)
c = c1 + c2
i = k - (1 - delta) * k
y = c + i
>>>>>>> upstream/master

# Print steady-state equilibrium endogenous variables
print("B2: " + str(b2))
print("C1: " + str(c1))
print("C2: " + str(c2))
print("R: " + str(r))
print("W: " + str(w))
print("K: " + str(k))
print("L: " + str(l))
print("C: " + str(c))
print("I: " + str(i))
print("Y: " + str(y))
