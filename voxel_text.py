from ursina import *
import math
import random                           # Import the random library

random_generator = random.Random()      # Create a random number generator

# Linux does not like borderless windows (X11).
window.borderless = False
app = Ursina()

t = 0.0

#generate terrain
cubes = []                                       
for i in range(0,80):
    for j in range(0,80):
        newcube = Entity(model='cube', texture = "dirt", position=(i, 0, j), scale=(1,1,1))
        cubes.append(newcube)


# starting camera position
camera.position = (0,1,0)

def update():
    global cube
    global t

    if held_keys['w']:                               # If q is pressed
        camera.position += (0, 0, 10*time.dt)           # move up vertically
    if held_keys['s']:                               # If a is pressed
        camera.position -= (0, 0, 10*time.dt)           # move down vertically
    if held_keys['a']:
        camera.position -= (time.dt, 0, 0)
    if held_keys['d']:
        camera.position += (time.dt, 0, 0)
    
    if held_keys['l']:
        camera.rotation_y += 20*time.dt    
    if held_keys['k']:
        camera.rotation_y -= 20*time.dt 

    t += time.dt



app.run()