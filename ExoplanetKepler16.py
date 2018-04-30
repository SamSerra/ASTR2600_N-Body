"""
Part 4.
==================
This file calculates the orbital trajectories of the Kepler-16ABb system.
The input data is read from a .txt file

The system is evolved for 500 days with a timestep of .5 days

=================
Output
=================

Output/Part 4

==================
Dependencies
==================

Standard: 
    numpy
    matplotlib.pyplot
    os
    sys
    matplotlib.animation.FuncAnimation

Non-standard:
    main
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
import os

from main import calculateTrajectories

# Question 7.
# load data
#------------------------------------------------------------------------------

# load data
simDir = os.path.dirname(os.path.abspath(__file__))
outputDir = '/Output/Part 4'
dataDir = '/Data'

initPos, initVel = np.zeros((3,3)), np.zeros((3,3))
masses, initPos[0,:],initPos[1,:],initPos[2,:], initVel[0,:], initVel[1,:], initVel[2,:] = np.loadtxt(simDir+dataDir+'/kepler16.txt', delimiter=' ',unpack=True)

# Question 8.
# plot initial positions
#------------------------------------------------------------------------------

# plot initial positions/velocities in x-z plane
maxMass = np.max(masses) #scale size of particles by mass
gain = 50
colorArray = ['red','green','blue']

fig, ax = plt.subplots()
ax.scatter(initPos[0,:],initPos[2,:],marker='o',s=gain*masses/maxMass, c=colorArray) #initial positions
ax.quiver(initPos[0,:],initPos[2,:],initVel[0,:],initVel[2,:], color=colorArray)    #initial velocities

ax.set_xlabel('Position [m]')
ax.set_ylabel('Position [m]')
ax.set_title('X-Z Plane of Kepler-16ABb System')

ax.set_ylim(-.3e11,1.0e11)

fig.savefig(simDir+outputDir+'/kepler16InitialConditions.png')

# Question 9.
# evolve
#----------------------------------------------------------------------------

# set constants
secInDay = 3600*24  #seconds in day

# set up simulation parameters
timeEvol = 500 #days 
timeStep = .5  #days

timeEvol *= secInDay #convert to seconds
timeStep *= secInDay

# format initial data
initPos = initPos.T
initVel = initVel.T

# run sim
times, positionArray, velocityArray = calculateTrajectories(masses,initPos,initVel,timeEvol,timeStep)

# Question 10.
# animate
#----------------------------------------------------------------------------

# set up figure
fig,ax = plt.subplots()
ax.set(xlim=(-1.3e11,1.3e11), ylim=(-1.4e11,1.0e11))
ax.set_xlabel('Position [m]')
ax.set_ylabel('Position [m]')

# initial frame

#markers for planets
ax.scatter(positionArray[:,0,0],positionArray[:,2,0], marker='o', s=gain*masses/maxMass, c=colorArray)       

#trajectories
for i in np.arange(len(masses)):  
    ax.plot(positionArray[:,0,0].T,positionArray[:,2,0].T, c=colorArray[i]) 
    
#velocities
ax.quiver(positionArray[:,0,0],positionArray[:,2,0], velocityArray[:,0,0],velocityArray[:,2,0], color = colorArray)

# animation function
def animate(fnum):
    # progress bar
    sys.stdout.write('\rdrawing frame {}/{}'.format(fnum,int((timeEvol/timeStep))))
    sys.stdout.flush()

    # delete previous trajectory, markers, and velocity arrow
    ax.clear()

    # update title and axis 
    ax.set_title('X-Z Plane of Kepler-16ABb System: {} Days'.format(times[fnum]/secInDay))
    ax.set(xlim=(-1.3e11,1.3e11), ylim=(-1.4e11,1.0e11))
    ax.set_xlabel('Position [m]')
    ax.set_ylabel('Position [m]')

    # update trajectories, markers, and velocity vectors
    ax.scatter(positionArray[:,0,fnum],positionArray[:,2,fnum], marker='o', s=gain*masses/maxMass, c=colorArray)
    
    for i in np.arange(len(masses)):
        ax.plot(positionArray[i,0,0:fnum].T,positionArray[i,2,0:fnum].T, c=colorArray[i])
        
    ax.quiver(positionArray[:,0,fnum],positionArray[:,2,fnum], velocityArray[:,0,fnum],velocityArray[:,2,fnum], color = colorArray)

# animate
anim = FuncAnimation(fig, animate, interval=50, frames = int((timeEvol/timeStep) + 1))
anim.save(simDir+outputDir+'/kepler16Animation.mp4')
