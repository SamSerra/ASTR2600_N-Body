"""
Part 2.
===========

This file tests to make sure the leapfrog and forces modules work as expected.

"forces" has a built-in test function

For "leapfrog", we set up two particles of mass 1kg and 2kg located at 
(0,0,0) and (1,0,0) with initial velocities (1,0,0) and (-1,0,0). We 
increment this by 1 second and see if the result agrees with an analytical
calculation

==================
Dependencies
===================

Standard:
    numpy
    matplotlib.pyplot

Non-standard (make sure on path):
    leapfrog
    forces
"""

import numpy as np
import matplotlib.pyplot as plt
import leapfrog
from forces import test

# Question 3.
# Test forces (works)
#------------------------------------------------------------------------#

test()

# Question 2.
# Test updateParticles
#------------------------------------------------------------------------#

# initial conditions
initialMasses = np.array([1,2])
initialPos    = np.array([[0,0,0],[1,0,0]])
initialVel    = np.array([[0,1,0],[0,-1,0]])
dt = 1

endVel, endPos = leapfrog.updateParticles(initialMasses,initialPos,initialVel, dt)

print("\nThe ending velocities are:")
print("{:>10} | {:>10} | {:>10}".format("Vel X", "Vel Y", "Vel Z"))
print("-"*49)
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endVel[0][0], endVel[0][1],  endVel[0][2]))
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endVel[1][0], endVel[1][1],  endVel[1][2]))

print("\nThe ending positions are:")
print("{:>10} | {:>10} | {:>10}".format("Pos X", "Pos Y", "Pos Z"))
print("-"*49)
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endPos[0][0], endPos[0][1],  endPos[0][2]))
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endPos[1][0], endPos[1][1],  endPos[1][2]))
