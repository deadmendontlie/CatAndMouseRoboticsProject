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

brick.sound.beep()
colorSensor = ColorSensor(Port.S4)
sonarSensor = UltrasonicSensor(Port.S2)
touchSensor = TouchSensor(Port.S1)
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)

def Tom():
    done = False
    while not Button.LEFT in brick.buttons():
        brick.display.text(colorSensor.reflection())
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
    while not done
        if(chase == True)
            done = True;
    
def chase():
    chaseValue = (sonarSensor.distance()/1275)/2
    if(chaseValue < .1)
        leftMotor.dc(0)
        rightMotor.dc(0)
        if(colorSensor.reflection() < 20)
            touchSensor.pressed()
            return True
        else:
            leftMotor.dc(-30)
            rightMotor.dc(-30)
            wait(1500)
    else:
        leftMotor.dc(100 * chaseValue)
        rightMotor.dc(100 * chaseValue)
        return False

def searchTurn():
    checks = 0
    while sonarSensor.distance > 1275 and checks < 5
        leftMotor.dc(20)
        rightMotor.dc(0)
        wait(1000)
        if sonarSensor.distance < 1275
            leftMotor.dc(0)
            return True
        else:
            checks = checks + 1

def search forward()
    leftMotor.dc(30)
    rightMotor.dc(30)
    wait(2000)
def main():
    Tom()
main()
