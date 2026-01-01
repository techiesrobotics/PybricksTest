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

#4.1.B: Cutting corners
def square_curved_corners(W, R):
    straight_length = W - (2 * R)

    for _ in range(4):
        drive_base.straight(straight_length)
        drive_base.curve(R, 90)  # radius R, 90° turn

square_curved_corners(250, 100)