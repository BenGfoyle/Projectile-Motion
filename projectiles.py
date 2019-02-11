import math
import numpy
import matplotlib.pyplot as plt

#find max distance traveled by a body in the x plane
#v^2 = u^2 + 2as
#v = u + at
#s = ut + 0.5*at^2
#Assume no air resistance
#Assume body remains stationary when it impacts the ground

def getHeight(u,t,a,h):
   
    s = (u*t) + (0.5*a)*(t**2) + h
    return s
    #do maths
    """
    if unknowns become a thing to worry about
    if u == '?':
        s = (v*t) - (0.5*a)*(t**2) + h
    elif v == '?':
        s = (u*t) + (0.5*a)*(t**2) + h
    else:
        s = (u*t) + (0.5*t)*(v-u) + h
    #elif t = ?:
       #s = u*((v-u)/a) + 0.5*((v**2 + u**2 + 2*v*u)/a) + h
    """
   
h = 0
angle = 90
v = 10
u = 100
a = -10
    
h = float(input("Enter a value for initial height of projectile (meters) "))
angle = float(input("Enter a value for angle of trajectory (Deg) "))
#v = input("Enter a value for final velocity (meters/second), if unknown enter ?") #assumed to be v @ angle 
u = float(input("Enter a value for initial velocity (meters/second) "))
a = float(input("Enter a value for acceleration due to gravity (meters/second^2) "))

#finding cartesian components of inital and final velocity (final velocity not currently used for anything)
uy = u*math.sin(angle)
ux = u*math.cos(angle)
#vy = v*math.sin(angle)
#vx = v*math.cos(angle) 

#Lists used to track time, height and x displacement
height = []
time = []
xdis = []
currentTime = 0
currentHeight = getHeight(uy,currentTime,a,h) #get height at t = 0

while(currentHeight >= 0 ): #run simulation for as long as y displacement is > 0 ie while the projectile is in the air
    height.append(currentHeight) #append height/x displacemtnt/current time to respective lists
    time.append(currentTime)
    xdis.append(ux*currentTime)
    currentTime += 0.1 #incriment current time by 1/10th of a second, feel free to change this
    currentHeight = getHeight(uy,currentTime,a,h) #new current height calculated

#Graphing and plotting, see matplot.lib library for more info (https://matplotlib.org/tutorials/introductory/sample_plots.html)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny() #creates 2 x axis both relative to shared y axis
ax1.set_xlabel("Time(Seconds)")
ax1.set_ylabel("Vertical Displacement(Meters)")
ax2.set_xlabel("Horizontal Displacement(Meters)")
ax2.set_xlim(0,xdis[len(xdis)-1])
ax1.plot(time,height)