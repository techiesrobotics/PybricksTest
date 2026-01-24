from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from Test_Color_Refactor import *
from TRRobo import *

robot = TRRobot()

def drive_and_detect_color(distance_mm):
    last_color = None

    robot.drive_base.reset()
    robot.drive_base.drive(200, 0)

    while abs(robot.drive_base.distance()) < distance_mm:
        color_name = determineColor()

        if color_name != "UNKNOWN":
            print("Detected:", color_name)

        wait(50)

    robot.drive_base.stop()

def main():
    drive_and_detect_color(1000)

if __name__ == "__main__":
    main()