import math
import numpy
import matplotlib.pyplot as plt
from tkinter import *

#find max distance traveled by a body in the x plane
#v^2 = u^2 + 2as
#v = u + at
#s = ut + 0.5*at^2
#Assume no air resistance
#Assume body remains stationary when it impacts the ground

def plotGraph(yAxis,xAxis,timeAxis):
    #Graphing and plotting, see matplot.lib library for more info (https://matplotlib.org/tutorials/introductory/sample_plots.html)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twiny() #creates 2 x axis both relative to shared y axis
    ax1.set_xlabel("Time(Seconds)")
    ax1.set_ylabel("Vertical Displacement(Meters)")
    ax2.set_xlabel("Horizontal Displacement(Meters)")
    ax2.set_xlim(0,xAxis[len(xAxis)-1])
    ax1.grid()
    ax1.plot(timeAxis,yAxis)

def getHeight(u,t,a,h): #get max distance given the parameters
    s = (u*t) + (0.5*a)*(t**2) + h
    return s
    
    
def heightLength(h,angle,u,a): #function to get max height and x distance. 
    
    h,angle,u,a = float(h),math.radians(float(angle)),float(u),float(a) #parse inputs to floats for calcualtions
    
    #finding cartesian components of inital and final velocity (final velocity not currently used for anything)
    if angle != 1.5707963267948966:
        uy = u*math.sin(angle)
        ux = u*math.cos(angle)
        #vy = v*math.sin(angle)
        #vx = v*math.cos(angle) 
    else:
        uy = u
        ux = 0
        
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
    
    return max(height), max(xdis),height,xdis,time
    
def clicked(): #perform opertion on button click
    height = txt1.get()
    angle = txt2.get()
    initial_velocity = txt3.get()
    acceleration = txt4.get()
    lbl5 = Label(window, text = "Caluclating...")
    lbl5.grid(column = 0, row = 4)
    
    maxHeight, maxDistance,height_list, xdis_list,time_list =  heightLength(height, angle,initial_velocity, acceleration)
    
    #Create label based off the returned values for max distance/height
    maxHeight = "Max Height: ", maxHeight
    maxDistance = "Max Distance: ", maxDistance
    print(maxHeight, maxDistance)
    lbl6= Label(window,text = maxHeight)
    lbl6.grid(column = 0, row = 5)
    lbl7= Label(window,text = maxDistance)
    lbl7.grid(column = 0, row = 6)
    #create plot based on returened lists
    plotGraph(height_list,xdis_list,time_list)

#Define window, name, and parameters
window = Tk()
window.title("Projectile Motion")
window.geometry('400x200')

#Insert text with user input text field. 
lbl1 = Label(window, text="Enter a value for initial height (m)")
lbl1.grid(column=0, row=0)

txt1 = Entry(window, width = 10)
txt1.grid(column = 1, row = 0)

lbl2 = Label(window, text="Enter a value for angle of trajectory (Deg)")
lbl2.grid(column=0, row=1)

txt2 = Entry(window, width = 10)
txt2.grid(column = 1, row = 1)

lbl3 = Label(window, text="Enter a value for initial velocity of the particle (m/s)")
lbl3.grid(column=0, row=2)

txt3 = Entry(window, width = 10)
txt3.grid(column = 1, row = 2)

lbl4 = Label(window, text="Enter a value for acceleration due to gravity (m/s^2)")
lbl4.grid(column=0, row=3)

txt4 = Entry(window, width = 10)
txt4.grid(column = 1, row = 3)

#button that runs "clicked" function on click
btn = Button(window, text="Submit Values", command = clicked)
btn.grid(column=1, row=4)

#loop until closed
window.mainloop()
