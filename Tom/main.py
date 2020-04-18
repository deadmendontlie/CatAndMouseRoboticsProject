#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
def Tom():
    brick.sound.beep()
    colorSensor = ColorSensor(Port.S2)
    touchSensor = TouchSensor(Port.S3)
    leftMotor = Motor(Port.B)
    rightMotor = Motor(Port.C)
    while not Button.LEFT in brick.buttons():
        brick.display.text(colorSensor.ambient())
    while not Button.RIGHT in brick.buttons():
        brick.display.text(touchSensor.pressed())
    while not Button.DOWN in brick.buttons():
        brick.display.text(leftMotor.dc(30))
    while not Button.UP in brick.buttons():
        brick.display.text(rightMotor.dc(30))
def main():
    Tom()
main()
