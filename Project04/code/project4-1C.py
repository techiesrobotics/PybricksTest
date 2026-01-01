from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Color
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

#4.1.C: It’s all a blur
def mix_red_green(red_percent, green_percent, base_time=4):
    total = red_percent + green_percent
    if total <= 0:
        return

    red_time = base_time * red_percent / total
    green_time = base_time * green_percent / total

    while True:
        hub.light.on(Color.GREEN)
        wait(green_time)
        hub.light.on(Color.RED)
        wait(red_time)

mix_red_green(25,75,4)