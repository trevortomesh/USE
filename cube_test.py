from ursina import *
import math

# Linux does not like borderless windows (X11).
window.borderless = False
app = Ursina()

cube = Entity(model="cube", color=color.red)
t = 0.0

def update():
    global cube
    global t

    if held_keys['w']:                               # If q is pressed
        camera.position += (0, time.dt, 0)           # move up vertically
    if held_keys['s']:                               # If a is pressed
        camera.position -= (0, time.dt, 0)           # move down vertically
    if held_keys['a']:
        camera.position += (time.dt, 0, 0)
    if held_keys['d']:
        camera.position -= (time.dt, 0, 0)

    t += time.dt

    cube.x = math.cos(t) * 2.0
    #cube.y = math.sin(t) * 2.0


app.run()