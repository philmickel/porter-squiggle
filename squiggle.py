import vpython as vp
import numpy as np
from opensimplex import OpenSimplex

#initialize some important variables; resolution, freq, and amp relate to the noise produced in order to get the scribble so random
#fps refers to literally the frames per second we want the simulation to run at; if we just let it go, the computer will run at max speed
#rotate angle is just a calculation to determine how many radians per step to rotate the system so that it does 1 full rotation in 30 seconds
resolution = 200
freq = 10
amp = 150
fps = 60
angle = (np.pi*2)/(30*fps)


#OpenSimplex is a module that provides the randomized noise based off the Simplex system; it's integral to making the scribble so pretty
tmp = OpenSimplex(seed=0)

#For a 3D scribble, we want to span the unit sphere in spherical coordinates and we don't care about rho, so we make a meshgrid from 0-2pi in
#both the phi and theta angle space
phi, theta = np.meshgrid(np.linspace(0, np.pi*2, resolution), np.linspace(0, np.pi*2, resolution)) 
xypairs = np.dstack([phi, theta]).reshape(-1, 2)


xyz_coords = np.zeros((xypairs.shape[0], 3))

#this is the scribble algorithm. 
#while scanning over each ordered pair of phi and theta, convert to cartesian coordinates
#then plug our x,y,z into the 4D noise formula with manually tweaked w-values(4th dimension)
#the y variable is multiplied by 2 in order to make the scribble more vertical as VPython calls the vertical axis y, not z like math
for index, pair in enumerate(xypairs):
    x = np.sin(pair[0])*np.sin(pair[1]) * freq
    y = np.cos(pair[1]) * freq
    z = np.cos(pair[0])*np.sin(pair[1]) * freq
    xyz_coords[index] = [amp*tmp.noise4d(x, y, z, -15), 2*amp*tmp.noise4d(x, y, z, 10), amp*tmp.noise4d(x, y, z, 113)]    
    
    
#we're repeating the vectorarray in order to slow down the drawing algorithm without making the movements choppy
vectorarray = np.repeat(xyz_coords, 1, axis=0)
#Without this initial line portion, there would be some random line pre-drawn for a few seconds prior to the scribble starting
initial_point = vectorarray[0]
final_point = vectorarray[1]
initial_line = [vp.vector(initial_point[0], initial_point[1], initial_point[2]), 
                vp.vector(final_point[0], final_point[1], final_point[2])]

#initialize the window; disabling autoscale prevents the camera from zooming in and out depending on how much screen the scribble takes up
#setting the range preemptively so we don't have to manually zoom
scene = vp.canvas(title='Nurturebook Pro', width=1000, height=1000)
scene.autoscale=False
scene.range = 150

#create the squiggle object; initially it should be zero due to the repeat making the first and second points the same
#retain is how many points to keep, so we don't have to manually roll the array or anything like that. As we add more,
#the oldest points get removed.
squiggle = vp.curve(pos=initial_line, radius = .3, retain = fps*11)


for i in range(len(vectorarray)):
    vp.rate(fps)                                              #limit the number of loops per second
    squiggle.rotate(angle=angle, axis=vp.vector(0, 1, 0))     #rotate around the vertical axis by some angle
    vectorx, vectory, vectorz = vectorarray[i]                #since we can only append vector objects and we can't enter np arrays as params
    new_point = vp.vector(vectorx, vectory, vectorz)          #split into 3 points first then enter
    squiggle.append(new_point)                                #add the vector
