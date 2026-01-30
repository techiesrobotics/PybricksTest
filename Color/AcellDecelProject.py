from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TRRobo import *

robot = TRRobot()

def Accelerate():
    straight_speed, straight_accel, turn_rate, turn_accel = robot.drive_base.settings()
    print("Wheel Diameter: 56")
    print("Axle Track: 112")
    print("Acceleration & Deceleration:", straight_accel)
    robot.MoveForward(200)

Accelerate()