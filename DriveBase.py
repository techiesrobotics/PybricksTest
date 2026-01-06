from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
distance_sensor = UltrasonicSensor(Port.A)
color_sensor = ColorSensor(Port.B)

drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)

drive_base.settings(straight_speed=250)
drive_base.use_gyro(True)

def SetGyro(boolean):
    drive_base.use_gyro(boolean)

def SetSpeed(speed):
    drive_base.settings(straight_speed=speed)

def MoveForward(distance):
    drive_base.straight(distance)

def MoveBackward(distance):
    drive_base.straight(-1* distance)

def TurnRight(degrees):
    drive_base.turn(degrees)

def TurnLeft(degrees):
    drive_base.turn(-1* degrees)