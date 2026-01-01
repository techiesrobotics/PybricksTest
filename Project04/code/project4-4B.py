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

#4.4.B: Everything at once
async def subtask():
    for count in range(5):
        await wait(0)
        print('Go!')
        await multitask(
            left_motor.run_angle(500, 360),
            hub.speaker.beep(500, 700),
        )

async def subtask2():
    while True:
        await wait(0)
        print('Green')
        hub.light.on(Color.GREEN)
        await wait(1000)
        print('Red')
        hub.light.on(Color.RED)
        await wait(1000)

async def main():
    await multitask(
        subtask(),
        subtask2(),
        race=True,
    )


run_task(main())