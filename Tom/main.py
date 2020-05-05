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
robot = DriveBase(leftMotor, rightMotor, 56, 114)

def tom():
    running = True
    while running:
        chaseValue = chase()
        print(chaseValue)
        if chaseValue == 1:
            running = False
        elif chaseValue == 0:
            searchTurn()

def chase():
    sensorValue = sonarSensor.distance()
    if sensorValue < 1275:
        if sensorValue < 100:
            print('in')
            leftMotor.dc(50)
            rightMotor.dc(52)
            wait(1000)
            if  touchSensor.pressed() and colorSensor.color() == Color.BLACK:
                leftMotor.dc(0)
                rightMotor.dc(0)
                return 1
            else:
                robot.drive_time(-50,0, 5000)
                robot.drive_time(50,90,3000)
                return 0
        else:
            speed = (100 * (sensorValue / 1275))
            if speed < 30:
                speed = speed + 20
            leftMotor.dc(speed)
            rightMotor.dc(speed + 2)
            return -1
    return 0


def searchForward():
    robot.drive_time(50, 0, 2000)

def searchTurn():
    checks = 0
    while sonarSensor.distance() > 1275 and checks < 5:
        robot.drive_time(40,90, 1000)
        if sonarSensor.distance() < 1275:
            return True
        else:
            checks = checks + 1
    searchForward()
    return False

def main():
    tom()
main()
