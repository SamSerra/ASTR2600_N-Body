"""
Part 2.
===========

This file tests to make sure the leapfrog and forces modules work as expected. It also
contains the "calculateTrajectories" function.

For testing:
    "forces" has a built-in test function
    For "leapfrog", we set up two particles of mass

See function doc string for information on "calculateTrajectories"

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
import sys
import numpy as np
import matplotlib.pyplot as plt
from leapfrog import updateParticles
from forces import test

'''
# Question 1.
# Test forces (works)
#------------------------------------------------------------------------#

test()

# Question 2.
# Test updateParticles (works)
#
# We set up two particles of mass 1kg and 2kg located at 
# (0,0,0) and (1,0,0) with initial velocities (1,0,0) and (-1,0,0). We 
# increment this by 1 second. We'd expect positions of (small pos. num, 1, 0) and
# (~1,-1, 0) with velocities (small pos. num, 1, 0) and (small neg. num, -1, 0)
#------------------------------------------------------------------------#

# initial conditions
initialMasses = np.array([1,2])
initialPos    = np.array([[0,0,0],[1,0,0]])
initialVel    = np.array([[0,1,0],[0,-1,0]])
dt = 1

endPos, endVel = updateParticles(initialMasses,initialPos,initialVel, dt)

print("\nThe ending positions are:")
print("{:>10} | {:>10} | {:>10}".format("Pos X", "Pos Y", "Pos Z"))
print("-"*36)
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endPos[0][0], endPos[0][1],  endPos[0][2]))
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endPos[1][0], endPos[1][1],  endPos[1][2]))

print("\nThe ending velocities are:")
print("{:>10} | {:>10} | {:>10}".format("Vel X", "Vel Y", "Vel Z"))
print("-"*36)
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endVel[0][0], endVel[0][1],  endVel[0][2]))
print("{:10.1e} | {:10.1e} | {:10.1e}".format(endVel[1][0], endVel[1][1],  endVel[1][2]))
'''
# Question 3.
# calculateTrajectories
#-----------------------------------------------------------------------#

def calculateTrajectories(masses, initPos, initVel, timeEvol, dt):
    """
    Calculates position and velocity of N particles in M dimensions for multiple
    times. 

    Inputs
    =========
    masses: N-element ordered array of masses, in kg
    initPos: (N,M) ordered array of initial positions for each mass, in meters
    initVel: (N,M) ordered array of initial velocities for each mass, in m/s
    timeEvol: amount of time to evolve system, in seconds
    dt: timestep, in seconds

    Return
    ==========
    times: numTimeSteps-element array with times evaluated at
    positionArray: (N,M,numTimeSteps)-array of positions for each N particles in M
                  dimensions for each time
    velocityArray:  (N,M,numTimeSteps)-array of velocities for each N particles in M
                  dimensions for each time
    """
    
    # create time array
    time = np.arange(0,timeEvol+dt,dt) #time array is end inclusive

    # create blank N by m by number of time steps arrays
    N = len(masses)
    M = len(initPos[0])
    numTimeSteps = len(time)

    positionArray = np.zeros((N,M,numTimeSteps))
    velocityArray = np.zeros((N,M,numTimeSteps))

    # load intial data into array
    positionArray[:,:,0] = initPos
    velocityArray[:,:,0] = initVel
    
    # calculate positions/velocities for each time, skipping t = 0
    for n in np.arange(numTimeSteps-1):
        pos, vel = updateParticles(masses, initPos, initVel, dt)
        initPos, initVel = pos, vel
        
        positionArray[:,:,n+1] = pos
        velocityArray[:,:,n+1] = vel

        # progress bar
        sys.stdout.write('\rcalculating time {}/{}'.format(n,numTimeSteps-1))
        sys.stdout.flush()

        
    return time, positionArray, velocityArray
