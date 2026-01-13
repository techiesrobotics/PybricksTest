from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from TRRobo import *

robot = TRRobot()

# Drive in a square
# https://www.youtube.com/watch?v=tpoMPDKgzEc
def DriveSquare(side_length):
    for _ in range(4):
        robot.MoveForward(side_length)
        robot.TurnRight(90)
    robot.drive_base.brake()

def main():
    DriveSquare(250)

if __name__ == "__main__":
    main()