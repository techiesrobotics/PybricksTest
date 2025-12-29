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

#3.1.A: Living on the edge
def living_on_the_edge():
    drive_base.straight(50)

#3.1.B: Spell your name
def spell_name():
    # Letter M
    drive_base.straight(200)
    drive_base.turn(150)
    drive_base.straight(150)
    drive_base.turn(-110)
    drive_base.straight(150)
    drive_base.turn(140)
    drive_base.straight(200)

    # Letter S
    drive_base.curve(90, -270)
    drive_base.curve(90, 270)

#3.1.C: Satnav subtitles
def satnav_subtitles():
    print("Turning 90 degrees right")
    drive_base.turn(90)
    print("Moving forward for 250mm")
    drive_base.straight(250)
    print("Moving backwards for 250mm")
    drive_base.straight(-250)
    print("Turning 90 degrees left")
    drive_base.turn(-90)

#3.2.C: Countdown clock
def countdown_clock():
    print("Time remaining...")
    for number in range(10, 0, -1):
        print(number)
        wait(1000)

#Command Line
while True:
    print("\nSelect an option:")
    print("1 - Living on the edge")
    print("2 - Spell your name")
    print("3 - Satnav subtitles")
    print("4 - Countdown clock")
    print("q - Quit")

    choice = input("Enter choice: ")

    print()
    if choice == "1":
        living_on_the_edge()
    elif choice == "2":
        spell_name()
    elif choice == "3":
        satnav_subtitles()
    elif choice == "4":
        countdown_clock()
    elif choice.lower() == "q":
        print("Exiting program")
        break
    else:
        print("Invalid choice")