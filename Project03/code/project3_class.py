from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from TRRobo import *

robot = TRRobot()

# Challenge #3.1.A: Living on the edge ⸺ Pick a fixed starting point on your
# desk and measure the distance to the edge of your desk. Tell the robot to
# drive exactly that distance and back again. Tip: On your first try, reduce
# the value slightly. Be prepared to catch your robot if it falls.
# Safety first! When you’re away from the computer, you can stop
# the program using the hub button.
# https://www.youtube.com/watch?v=fv3hDuycIqo&list=PLjWRBRiZoARHJEqJojDHSY6pTD_pMhuDS
def living_on_the_edge():
    robot.MoveForward(50)

# Challenge #3.1.B: Spell your name ⸺ Can you put together a sequence
# of Drive blocks so that it drives along the first letter of your name?
# What about your whole name? Hint: Besides in-place turns, you can also
# choose a curve with a given angle and radius. When you’re satisfied with
# the result, try attaching a pen to the robot so it draws your name as it moves.
# https://www.youtube.com/watch?v=QFzBQgZnLYY&list=PLjWRBRiZoARHJEqJojDHSY6pTD_pMhuDS
def spell_name():
    # Letter M
    robot.MoveForward(200)
    robot.TurnRight(150)
    robot.MoveForward(150)
    robot.TurnLeft(110)
    robot.MoveForward(150)
    robot.TurnRight(140)
    robot.MoveForward(200)

    # Letter S
    robot.drive_base.curve(90, -270)
    robot.drive_base.curve(90, 270)

# Challenge #3.1.C: Satnav subtitles ⸺ Previously, you’ve experimented
# with the Print block. Add print blocks to your program to make the robot
# indicate exactly what it will do. For example, make it say
# “Turning 90 degrees!” Where do you put these Print blocks? Should they
# go before or after each Drive block?
# https://www.youtube.com/watch?v=RAygxZIqdog&list=PLjWRBRiZoARHJEqJojDHSY6pTD_pMhuDS
def satnav_subtitles():
    print("Turning 90 degrees right")
    robot.TurnRight(90)
    print("Moving forward for 250mm")
    robot.MoveForward(250)
    print("Moving backwards for 250mm")
    robot.MoveBackward(250)
    print("Turning 90 degrees left")
    robot.TurnLeft(90)

# Challenge #3.2.C: Countdown clock ⸺ Can you combine Wait Time blocks,
# Print blocks, and Comment blocks to create a countdown clock? First, display
# a message to say "Time remaining...", and then display 10, 9, 8 and so on
# until time is up. How do you ensure that each new message is exactly one
# second apart? Test your result using the stopwatch feature on your phone.
# Note: Does this feel repetitive? In the next chapters you’ll learn how to
# get the same result with fewer blocks.
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