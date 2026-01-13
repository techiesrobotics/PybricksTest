from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from TRDriveBase import *

# 3.1.A: Living on the edge
# https://www.youtube.com/watch?v=fv3hDuycIqo&list=PLjWRBRiZoARHJEqJojDHSY6pTD_pMhuDS
def living_on_the_edge():
    MoveForward(50)

# 3.1.B: Spell your name
# https://www.youtube.com/watch?v=QFzBQgZnLYY&list=PLjWRBRiZoARHJEqJojDHSY6pTD_pMhuDS
def spell_name():
    # Letter M
    MoveForward(200)
    TurnRight(150)
    MoveForward(150)
    TurnLeft(110)
    MoveForward(150)
    TurnRight(140)
    MoveForward(200)

    # Letter S
    drive_base.curve(90, -270)
    drive_base.curve(90, 270)

# 3.1.C: Satnav subtitles
# https://www.youtube.com/watch?v=RAygxZIqdog&list=PLjWRBRiZoARHJEqJojDHSY6pTD_pMhuDS
def satnav_subtitles():
    print("Turning 90 degrees right")
    TurnRight(90)
    print("Moving forward for 250mm")
    MoveForward(250)
    print("Moving backwards for 250mm")
    MoveBackward(250)
    print("Turning 90 degrees left")
    TurnLeft(90)

# 3.2.C: Countdown clock
def countdown_clock():
    print("Time remaining...")
    for number in range(10, 0, -1):
        print(number)
        wait(1000)

# ---- Command Line ----
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