from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from DriveBase import *

SetSpeed(250)

def DriveSquare(side_length):
    for _ in range(4):
        MoveForward(side_length)
        TurnRight(90)
    drive_base.brake()

DriveSquare(250)