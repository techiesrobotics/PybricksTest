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

#4.4.A: Backing up!
async def drive_back():
    await drive_base.straight(-250)
    print("Backed up 250 mm!")

async def timeout():
    await wait(2000)
    print("I got stuck!")

async def main():
    await multitask(
        drive_back(),
        timeout(),
        race=True
    )


run_task(main())