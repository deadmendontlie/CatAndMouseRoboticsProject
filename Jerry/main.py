#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

brick.sound.beep()

colorSensor = ColorSensor(Port.S4)
sonarSensor = UltrasonicSensor(Port.S2)
# touchSensor = TouchSensor(Port.S1)
touchSensor = TouchSensor(Port.S3) # Tom touch sensor on S1

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

wheel_diameter = 56
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

def SensorTest():
    
    while not Button.LEFT in brick.buttons():
        brick.display.text(colorSensor.ambient())

    while not Button.RIGHT in brick.buttons():
        brick.display.text(touchSensor.pressed())
    
    while not Button.CENTER in brick.buttons():
        brick.display.text(sonarSensor.distance())
    
    while not Button.DOWN in brick.buttons():
        left_motor.dc(30)
        wait(2000)
        left_motor.dc(0)
    
    while not Button.UP in brick.buttons():
        right_motor.dc(30)
        wait(2000)
        right_motor.dc(0)
    
def Jerry():
    threshold = 500
    count = 0

    while not Button.CENTER in brick.buttons():
        while True:
            while sonarSensor.distance() < threshold:
                # give Jerry an initial speed boost 
                # the closer the object is to Jerry, the faster the speed boost
                pid = (threshold - sonarSensor.distance()) * 0.75

                # only the first time Jerry detects an object close to it
                if count == 0:
                    robot.drive(-pid, 0)
                else:
                    robot.drive(-100, 0)

                # slows down after hitting a wall
                if (touchSensor.pressed() == True):
                    # backs up, changes direction, and starts running at normal speed
                    robot.drive(100, 0)
                    robot.drive_time(100, 90, 1000)
                    count = 1
            while sonarSensor.distance() >= threshold:
                # staying idle and just spinning
                left_motor.dc(20)
                wait(100)

def main():
    # SensorTest()
    Jerry()

main()
