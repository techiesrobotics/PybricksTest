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

#4.1.A: Chicken or the egg
def square_turn_first(side_length):
    for _ in range(4):
        drive_base.turn(90)
        drive_base.straight(side_length)
    drive_base.brake()

def square_straight_first(side_length):
    for _ in range(4):
        drive_base.straight(side_length)
        drive_base.turn(90)
    drive_base.brake()

square_straight_first(100)
square_turn_first(100)