"""
Part 3.
=================

This file calculates earth's trajectory around the sun in 2d assuming
newtonian gravity.

The input data is:

Particle | mass (kg) | x (au) | y (au) | z (au) | Vx (m/s) | Vy (m/s) | Vz
------------------------------------------------------------------------
Sun      | 1.989e30  | -3e-6  | 0.0    | 0.0    | 0.0      | -8.94e-2 | 0.0
Earth    | 5.972e24  | .999997| 0.0    | 0.0    | 0.0      | 2.98e4   | 0.0

The calculation is run for 1000 days at a timestep of .1 days

==================
Output
=================

Output/Part 3/Question 5
OUtput/Part 3/Question 6

==================
Dependencies
==================

Standard: 
    numpy
    matplotlib
    os

Non-standard:
    main
"""
import numpy as np
import matplotlib.pyplot as plt
import os
from main import calculateTrajectories

# Question 5.
#-------------------------------------------------------------------------------

# set constants
mInAu    = 1.496e11 # meters in AU
secInDay = 3600*24  #seconds in day

# set simulation parameters
timeEvol = 1000 #days
timeStep = .1   #days

# set intial data
masses = np.array([1.989e30, 5.972e24])                   #kg
initPos = np.array([[-3e-6, 0.0, 0.0],[.999997,0.0,0.0]]) #AU
initVel = np.array([[0.0,-8.94e-2,0.0],[0.0,2.98e4,0.0]]) #m/s

# unit conversion
initPos *= mInAu     #meters
timeEvol *= secInDay #seconds
timeStep *= secInDay #seconds

# run simulation
#-------------------------------------------------------------
times, positionArray, velocityArray = calculateTrajectories(masses,initPos,initVel,timeEvol,timeStep)

# convert back to AU and days
positionArray /= mInAu
times /= secInDay

# plotting
#------------------------------------------------------------

simDir = os.path.dirname(os.path.abspath(__file__))
outputDir = '/Output/Part 3/Question 5'

# plot time vs x 
fig, ax = plt.subplots()
ax.plot(times, positionArray[0,0,:], label='Sun',color = 'green')      #sun
ax.plot(times, positionArray[1,0,:], label='Earth', color='blue')      #earth
ax.axvline(times[3640], 0,1, color='r', ls='-', label='t = 365 days')  #line at 365 days

ax.set_xlabel('Time [days]')
ax.set_ylabel('Position [AU]')
ax.set_title('Earth/Sun System: X component of position')
ax.legend()

fig.savefig(simDir + outputDir + '/timeVSxposition.png')

#plot x-y plane
fig, ax = plt.subplots()
ax.plot(positionArray[0,0,:], positionArray[0,1,:], label='Sun', c='green')  #sun
ax.plot(positionArray[1,0,:], positionArray[1,1,:], label='Earth', c='blue') #earth

initPos /= mInAu
ax.scatter(initPos[0,0],initPos[0,1], s=100, c='green', marker = '*') #dot for sun and earth
ax.scatter(initPos[1,0],initPos[1,1], s=50, c='blue', marker = 'o')

ax.set_xlabel('Position [AU]')
ax.set_ylabel('Position [AU]')
ax.set_title('Top Down View of Earth/Sun System')
ax.legend()

plt.tight_layout()
ax.axis('equal')
fig.savefig(simDir + outputDir + '/xyPlane.png')

# x-velocities of sun
fig, ax = plt.subplots()
ax.plot(times, velocityArray[0,0,:])

ax.set_xlabel('Time [AU]')
ax.set_ylabel('Radial Velocity [m/s]')
ax.set_title('RV Plot of Sun')

plt.tight_layout()
fig.savefig(simDir + outputDir + '/sunXvelocity.png')

