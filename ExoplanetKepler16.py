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
    matplotlib.animation.FuncAnimation

Non-standard:
    main
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
from main import calculateTrajectories

# Question 7.
# load data
#------------------------------------------------------------------------------

# load data
simDir =  '/home/samserra/Desktop/ASTR2600_FINAL/'
outputDir = 'Output/Part 4/'
dataDir = 'Data/'

initPos, initVel = np.zeros((3,3)), np.zeros((3,3))
masses, initPos[0,:],initPos[1,:],initPos[2,:], initVel[0,:], initVel[1,:], \
    initVel[2,:] = np.loadtxt(simDir+dataDir+'kepler16.txt', delimiter=' ',unpack=True)

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

xAxisLimits = ax.get_xlim() #save limits for later
yAxisLimits = ax.get_ylim()

fig.savefig(simDir+outputDir+'kepler16InitialConditions.png')

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
ax.set(xlim=(-1.3e11,.6e11), ylim=(-1.0e11,1.0e11))
ax.set_xlabel('Position [m]')
ax.set_ylabel('Position [m]')

# initial frame
scat = ax.scatter(positionArray[:,0,0],positionArray[:,2,0], marker='o',s=gain*masses/maxMass, c=colorArray)

#qax = ax.quiver(initPos[0,:],initPos[2,:],initVel[0,:],initVel[2,:], color=colorArray)

# animation function
def animate(fnum):
    # progress bar
    sys.stdout.write('\rdrawing frame {}/{}'.format(fnum,int(timeEvol/timeStep)))
    sys.stdout.flush()
    
    # update title
    ax.set_title('X-Z Plane of Kepler-16ABb System: {} Days'.format(times[fnum]/secInDay))
    
    ax.scatter(positionArray[:,0,fnum],positionArray[:,2,fnum], \
               marker='o',s=gain*masses/maxMass, c=colorArray)
    
    # update velocities
    # velocityDict['particle{}'.format(i)] =  ax.quiver(positionArray[i,0,fnum],positionArray[i,2,fnum],velocityArray[i,0,fnum],velocityArray[i,0,fnum], color=colorArray[i])

# animate
anim = FuncAnimation(fig, animate, interval=50, frames = int(timeEvol/timeStep))
anim.save(simDir+outputDir+'kepler16Animation.mp4')
