from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from Test_Color_Refactor2 import *
from TRRobo import *

robot = TRRobot()

# drive and detect color example:
# https://www.youtube.com/watch?v=c2XkUQgEWeg

def drive_and_detect_color(distance_mm):
    robot.drive_base.reset()
    robot.drive_base.drive(200, 0)

    last_color = None

    while abs(robot.drive_base.distance()) < distance_mm:
        color_name = determineColor()

        if color_name != "NONE" and color_name != last_color:
            print("Detected:", color_name)
            last_color = color_name

        wait(10)

    robot.drive_base.stop()

def main():
    drive_and_detect_color(300)

if __name__ == "__main__":
    main()