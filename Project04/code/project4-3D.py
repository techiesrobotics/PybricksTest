from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task

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

    return hub, left_motor, right_motor, drive_base

hub, left_motor, right_motor, drive_base = setup()

#4.3.D: Multitasking efficiently
async def combined_task():
    hub.light.on(Color.RED)
    await wait(500)
    print("Hello")
    hub.light.on(Color.GREEN)
    await wait(500)
    print("world")

async def main():
    await multitask(
        left_motor.run_angle(500, 360),
        hub.speaker.beep(500, 100),
        combined_task(),
    )


run_task(main())