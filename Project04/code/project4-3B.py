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

#4.3.B: On the dance floor
blink_color = {"value": Color.BLUE}
blinking = {"active": True}

async def change_color(color: Color):
    blink_color["value"] = color

async def blink():
    while blinking["active"]:
        hub.light.on(blink_color["value"])
        await wait(200)
        hub.light.off()
        await wait(200)

async def play_melody():
    await hub.speaker.play_notes(
        [
            "C3/4", "C3/4",
            "G3/4", "G3/4",
            "A3/4", "A3/4",
            "G3/2",

            "F3/4", "F3/4",
            "E3/4", "E3/4",
            "D3/4", "D3/4",
            "C3/2",
        ],
        tempo=120
    )

async def drive_square(distance):
    for i in range(4):
        await multitask(
            drive_base.straight(distance),
            change_color(Color.BLUE)
        )
        await multitask(
            drive_base.turn(90),
            change_color(Color.RED)
        )
    blinking["active"] = False
    hub.light.off()

async def dance_square():
    await multitask(
        blink(),
        drive_square(200),
        play_melody()
    )

run_task(dance_square())
