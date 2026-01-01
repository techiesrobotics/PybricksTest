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

#4.2.B: Fast mode and slow mode
def slow_mode():
    drive_base.settings(100, 100, 90, 90)

def fast_mode():
    drive_base.settings(500, 500, 360, 360)

def drive_square(side_length):
    for _ in range(4):
        drive_base.straight(side_length)
        drive_base.turn(90)

    drive_base.brake()

# Drive a slow square
slow_mode()
drive_square(100)

wait(1000)

# Drive a fast square
fast_mode()
drive_square(100)