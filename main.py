#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Button, Color, ImageFile, SoundFile
from pybricks.tools import wait

# The colored objects are either red, green, blue, or yellow.
POSSIBLE_COLORS = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW)

# Initialize the Color Sensor. It is used to detect the color of the objects.
color_sensor = ColorSensor(Port.S3)
brick.display.clear()
# This is the main loop. It waits for you to scan and insert 8 colored objects.
# Then it sorts them by color. Then the process starts over and you can scan
# and insert the next set of colored objects.
while True:
  
    # Store the color measured by the Color Sensor.
    color = color_sensor.color()
    if color in POSSIBLE_COLORS:
        brick.display.clear()
        if color == Color.RED:
            brick.display.text("color is red",(25,50))
        if color == Color.GREEN:
            brick.display.text("color is green",(25,50))
        if color == Color.YELLOW:
            brick.display.text("color is yellow",(25,50))
        if color == Color.BLUE:
            brick.display.text("color is blue",(25,50))
    # Determine if the color read is among POSSIBLE_COLORS
    if color in POSSIBLE_COLORS:
        # if yes, beep the brick
        
        brick.sound.beep(1000, 100, 100)

        
    #today we tried our code and found out that the code works. When the color sensor tried to see blue it showed yellow 
       #so when we try it again we have too find 
       #a place where to try it that can make to code sense the colors correct.
    
        
