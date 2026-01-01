from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()

#Setup
def setup():
    hub = PrimeHub()

    left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.D)

    drive_base = DriveBase(
        left_motor,
        right_motor,
        wheel_diameter=56,
        axle_track=110
    )

    return hub, drive_base

hub, drive_base = setup()

#4.2.A: Tracing your steps
def drive_square(side_length):
    #This function makes the robot drive one square.
    print("----Starting square----")
    for _ in range(4):
        print("Straight")
        drive_base.straight(side_length)
        print("Turn")
        drive_base.turn(90)
    print("----Completed a square----")
    drive_base.brake()

print("Let's go!")
drive_square(200)
wait(2000)
print("Let's go again!")
drive_square(200)