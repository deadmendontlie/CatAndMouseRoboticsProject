#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
#Kody did everything below this atm check the github if you don't believe me
def Tom():
    brick.sound.beep()
    colorSensor = ColorSensor(Port.S4)
    sonarSensor = UltrasonicSensor(Port.S2)
    touchSensor = TouchSensor(Port.S1)
    leftMotor = Motor(Port.B)
    rightMotor = Motor(Port.C)
    while not Button.LEFT in brick.buttons():
        brick.display.text(colorSensor.ambient())
    while not Button.RIGHT in brick.buttons():
        brick.display.text(touchSensor.pressed())
    while not Button.CENTER in brick.buttons():
        brick.display.text(sonarSensor.distance())
    while not Button.DOWN in brick.buttons():
        leftMotor.dc(30)
        wait(2000)
        leftMotor.dc(0)
    while not Button.UP in brick.buttons():
        rightMotor.dc(30)
        wait(2000)
        rightMotor.dc(0)
    

def main():
    Tom()
main()
