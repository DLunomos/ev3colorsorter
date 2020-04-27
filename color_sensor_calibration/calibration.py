#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Button, Color, ImageFile, SoundFile
from pybricks.tools import wait

ev3 = ev3brick() #Initialize the brick

touch_sensor = TouchSensor(Port.S1)
assert touch_sensor
color_sensor = ColorSensor(Port.S3) #Initializes then
assert color_sensor #checks the color and touch sensor
speaker.beep(frequency = 670, duration = 100)

color_list = DataLog(name="color_list", extension="txt")

# This loop runs until you press the down button, 
# waiting for the user to input a colored brick 
# and the color for our training set
while !(button.DOWN in buttons.pressed()):
    ev3.screen.clear
    ev3.screen.draw_text(-60, -60, "Press the down button to end the program.", text_color=Color.BLACK, background_color=None)
    ev3.screen.draw_text(-60, 40, "Put a brick to the color sensor.", text_color=Color.BLACK, background_color=None)
    ev3.screen.draw_text(-60, -40, "Then press the touch sensor to sense it.", text_color=Color.BLACK, background_color=None)

    if touch_sensor.pressed():
        brick_color = color_sensor.rgb()
        brick_color = list(brick_color) # Changes to a list

        ev3.screen.clear()
        ev3.screen.draw_text(-40, 40, text="Press the button for the color you showed.", text_color=Color.BLACK, background_color=None)
        ev3.screen.draw_text(-80, -10, text="Left button: BLUE", text_color=Color.BLACK, background_color=None)
        ev3.screen.draw_text(-40, -10, text="Up button: RED", text_color=Color.BLACK, background_color=None)
        ev3.screen.draw_text(0, -10, text="Center button: YELLOW", text_color=Color.BLACK, background_color=None)
        ev3.screen.draw_text(40, -10, text="Right button: GREEN", text_color=Color.BLACK, background_color=None)
        wait(1000)


        # adds the color to each list
        if button.LEFT in buttons.pressed():
            brick_color.append("BLUE")
            color_list.log(','.join(brick_color))
        elif button.UP in buttons.pressed():
            brick_color.append("RED")
            color_list.log(','.join(brick_color))
        elif button.CENTER in buttons.pressed():
            brick_color.append("YELLOW")
            color_list.log(','.join(brick_color))
        elif button.RIGHT in buttons.pressed():
            brick_color.append("GREEN")
            color_list.log(','.join(brick_color))