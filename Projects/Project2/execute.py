'''
This file is a script that solves for the steady-state in the two-
period-lived overlapping generations model given some parameter values.
'''

# Put import commands below here
import numpy as np

import FirmsMC
import household
import euler


# Set parameter values

# Household parameters
n1 = 1.0
n2 = 0.2
nvec = np.array([n1, n2])
gamma = 2.2
beta_an = 0.96
beta = beta_an ** (30)

# Firm parameters
A = 1.0
alpha = 0.35
delta_an = 0.05
delta = delta_an ** (30)

b2_args = (nvec, alpha, A, delta, beta, gamma)

# Solve for b2 given parameters
b2 = euler.get_b2(b2_args)

# Solve for all the other endogenous variables given parameter values
# and optimal b

K = FirmsMC.get_K(b2)
L = FirmsMC.get_L(nvec)
w = FirmsMC.get_w(b2, b2_args)
r = FirmsMC.get_r(b2, b2_args)
c1 = household.get_c1(b2, b2_args)
c2 = household.get_c2(b2, b2_args)
c = c1 + c2





# Print steady-state equilibrium endogenous variables

print("Savings is %d" % b2)
print("Consumption in period 1 is %d" % c1)
print("Consumption in period 2 is %d" % c2)
print("Total Consumption is %d" % c)
print("Wage is %d" % w)
print("The itnerest rate is %d" % r)
print("Capital stock is %d" % K)
print("Labor stock is %d" % L)
