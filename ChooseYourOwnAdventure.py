"""
Part 4.
==================
This file calculates the orbital trajectories of a uniform cube of particles.
The input data is read from a .txt file

The system is evolved for 500 days with a timestep of .5 days

=================
Output
=================

Output/Part 5

==================
Dependencies
==================

Standard: 
    numpy
    matplotlib.pyplot
    os
    sys
    matplotlib.animation.FuncAnimation
    mpl_toolkits.mplot3d.Axes3D

Non-standard:
    main
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import sys
import os

from main import calculateTrajectories

# Question 11.
# uniformCube.txt
#----------------------------------------------------------------#

# load data
simDir = os.path.dirname(os.path.abspath(__file__))
outputDir = '/Output/Part 5'
dataDir = '/Data'

initPos, initVel = np.zeros((3,27)), np.zeros((3,27))
masses, initPos[0,:],initPos[1,:],initPos[2,:], initVel[0,:], initVel[1,:], initVel[2,:] = np.loadtxt(simDir+dataDir+'/uniformCube.txt', delimiter=' ',unpack=True)

# set constants
secInDay = 3600*24  #seconds in day

# set up simulation parameters
timeEvol = 1000 #days 
timeStep = .5  #days

timeEvol *= secInDay #convert to seconds
timeStep *= secInDay

# format initial data
initPos = initPos.T
initVel = initVel.T

# run sim
times, positionArray, velocityArray = calculateTrajectories(masses,initPos,initVel,timeEvol,timeStep)

# Question 12.
# visualize
#------------------------------------------------------------------#

# set 3d axes
fig = plt.figure()
ax3d = fig.add_subplot(111, projection = '3d')

ax3d.set_title('Uniform Cube of Particles: {} Days'.format(times[0]/secInDay))
'''
ax3d.set_xlabel('Position [m]')
ax3d.set_ylabel('Position [m]')
ax3d.set_zlabel('Position [m]')
'''
ax3d.set_axis_off()

ax3d.grid(False) #turn grid off

# number of frames
frameNum = int((timeEvol/timeStep) + 1)

# axis framing (initial and final elevation and azimuth)
initElev = 50
finElev  = 0
initAzm  = 0
finAzm   = 360

elevArray = np.linspace(initElev, finElev, frameNum)
azmArray = np.linspace(initAzm, finAzm, frameNum)

# plot initial frame

#markers for particles 
ax3d.scatter3D(positionArray[:,0,0], positionArray[:,1,0], positionArray[:,2,0])

#trajectories
for i in np.arange(len(masses)):  
    ax3d.plot3D(positionArray[:,0,0].T,positionArray[:,1,0].T, positionArray[:,2,0].T)
    
#velocity vectors
ax3d.quiver3D(positionArray[:,0,0],positionArray[:,1,0], positionArray[:,2,0], velocityArray[:,0,0],velocityArray[:,1,0],velocityArray[:,2,0])

# get axes limits
xAxisLim1,xAxisLim2 = ax3d.get_xlim()
yAxisLim1,yAxisLim2 = ax3d.get_ylim()
zAxisLim1,zAxisLim2 = ax3d.get_zlim()

zoom = 1.5 #factor by which to zoom in/out

xAxisLim1 *= zoom
xAxisLim2 *= zoom
yAxisLim1 *= zoom
yAxisLim2 *= zoom
zAxisLim1 *= zoom
zAxisLim2 *= zoom

# animate function
def animate(fnum):
    # progress bar
    sys.stdout.write('\rdrawing frame {}/{}'.format(fnum,frameNum-1))
    sys.stdout.flush()

    # delete previous trajectory, markers, and velocity arrow
    ax3d.cla()

    # update title and axis 
    ax3d.set_title('Uniform Cube of Particles: {} Days'.format(times[fnum]/secInDay))
    ax3d.set(xlim3d=(xAxisLim1,xAxisLim2), ylim3d=(yAxisLim1, yAxisLim2), zlim3d=(zAxisLim1,zAxisLim2))
    '''
    ax3d.set_xlabel('Position [m]')
    ax3d.set_ylabel('Position [m]')
    ax3d.set_zlabel('Position [m]')
    '''

    ax3d.set_axis_off()
    ax3d.grid(False) #turn grid off

    # rotate axes every other frame
    if (fnum % 2 == 0):
        ax3d.view_init(elevArray[fnum], azmArray[fnum])
    
    # update trajectories, markers, and velocity vectors
    ax3d.scatter3D(positionArray[:,0,fnum],positionArray[:,1,fnum], positionArray[:,2,fnum])
    
    for i in np.arange(len(masses)):
        ax3d.plot3D(positionArray[i,0,0:fnum].T, positionArray[i,1,0:fnum].T, positionArray[i,2,0:fnum].T, color='blue')
        
    ax3d.quiver3D(positionArray[:,0,fnum],positionArray[:,1,fnum], positionArray[:,2,fnum], velocityArray[:,0,fnum], velocityArray[:,1,fnum], velocityArray[:,2,fnum])

# animate
anim = FuncAnimation(fig, animate, interval=25, frames = frameNum)
anim.save(simDir+outputDir+'/uniformCube.mp4')
