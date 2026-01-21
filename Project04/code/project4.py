from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task
from TRDriveBase import *

# Drive in a square
def drive_square(side_length):
        for _ in range(4):
            MoveForward(side_length)
            TurnRight(90)
        drive_base.brake()

# Challenge #4.1.A: Chicken or the egg ⸺ When driving in a square,
# does it matter if the straight or the turn comes first? Will the robot
# follow a different path if you swap them? Draw your prediction for both
# cases on a piece of paper and swap the code order to test your hypothesis.
# https://www.youtube.com/watch?v=W-0MNXOlLVw&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def square_turn_first(side_length):
    for _ in range(4):
        TurnRight(90)
        MoveForward(side_length)
    drive_base.brake()

def square_straight_first(side_length):
    for _ in range(4):
        MoveForward(side_length)
        TurnRight(90)
    drive_base.brake()

# Challenge #4.1.B: Cutting corners ⸺ Change the square program to drive with
# rounded corners instead of in-place turns, as shown below.
# https://www.youtube.com/watch?v=73sw0fb6K_o&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def square_curved_corners(W, R):
    straight_length = W - (2 * R)

    for _ in range(4):
        MoveForward(straight_length)
        drive_base.curve(R, 90)  # radius R, 90° turn

# Challenge #4.1.C: It’s all a blur ⸺ Reduce the wait duration as shown below.
# Now the light changes color hundreds of times per second. What is the result?
# This example creates a 50-50 mix of red and green. Why? Can you make it 75%
# green and 25% red? If you increase the wait duration, at what point does the
# light start to blink instead of blending smoothly?
# https://www.youtube.com/watch?v=XynZvNTh7Fg&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

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

# Challenge #4.1.D: Chicken or the egg, revisited ⸺ With the program below,
# you’ll hear two beeps between successive squares. Perhaps surprisingly,
# you hear the higher-pitch beep first. Why is that?
# https://www.youtube.com/watch?v=OQIQP0np2XQ&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def square_beep(side_length):
    while True:
        hub.speaker.beep(500, 200)
        drive_square(side_length)
        hub.speaker.beep(1200, 200)

# Challenge #4.1.E: Try again ⸺ Replicate the program shown above but
# swap the two repeat loops. The outer one should repeat 4 times and the
# inner one should repeat forever. Now you don’t hear a sound after each
# square, even though the beep commands are still there. Why is that? Hint
# ⸺ Add print statements throughout your program with different text
# messages to help you see which lines of code are running. Why does it
# never get to the second beep command in this case?
# https://www.youtube.com/watch?v=qgWHGWgPwrw&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def square_swap(side_length):
    def drive_square_loop(side_length):
        while True:
            print("Driving square")
            MoveForward(side_length)
            TurnRight(90)
            drive_base.brake()

    for i in range(4):
        print("Start of outer loop")
        hub.speaker.beep(500, 200)

        print("Entering inner infinite loop")
        drive_square_loop(100)

        print("This print is NEVER reached")
        hub.speaker.beep(1200, 200)

# Challenge #4.2.A: Tracing your steps ⸺ To get a better understanding
# of how this program runs all of its code, insert print statements as shown below.
# Before you try it, write down the expected output and verify your prediction.
# Discuss ⸺ Did you get it exactly right? If not, which steps did you miss?
# https://www.youtube.com/watch?v=X-t5qjY16fY&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def drive_square_print(side_length):
    #This function makes the robot drive one square.
    print("----Starting square----")
    for _ in range(4):
        print("Straight")
        MoveForward(side_length)
        print("Turn")
        TurnRight(90)
    print("----Completed a square----")
    drive_base.brake()

def tracing_steps(side_length):
    print("Let's go!")
    drive_square_print(side_length)
    wait(2000)
    print("Let's go again!")
    drive_square_print(side_length)

# Challenge #4.2.B: Fast mode and slow mode ⸺ Create two new functions called
# Slow and Fast, each with a collection of Drive Base Configuration blocks.
# The Slow task should set low acceleration and speed values for straights
# and turns. The Fast task should set high values. Now you can conveniently
# change speed profile midway throughout your program. Test it by driving
# one square very slowly and one square very quickly. Where do you place
# the function calls?
# https://www.youtube.com/watch?v=vv-TFFk2p5w&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def slow_mode():
    drive_base.settings(100, 100, 90, 90)

def fast_mode():
    drive_base.settings(500, 500, 360, 360)

# Challenge #4.2.C: An excursion into recursion ⸺ Modify the Square function to
# make it call itself as shown below. What do you think will happen? After many
# calls, you should see an error in the output pane. Research ⸺ Read the error
# message and determine which word to search for online. What is this technique
# called? Is it ever useful? Does this phenomenon occur anywhere in daily life?
# https://www.youtube.com/watch?v=ShNtQZZQ2OA&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def recurring_drive_square(side_length):
    print("Driving square")
    drive_square(side_length)
    recurring_drive_square(side_length)

# Challenge #4.3.A: In formation ⸺ Set up the left and right motor. Make them
# both move 1000 degrees at the same time. Compare the resulting movement to that
# of a fully configured DriveBase drive command. In both cases, what happens if
# you stop one wheel but not the other?
# https://www.youtube.com/watch?v=S02sNv-a688&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

def motors_run_angle(speed, rotation_angle):
    left_motor.run_angle(speed, rotation_angle, wait=False)
    right_motor.run_angle(speed, rotation_angle, wait=True)

# Challenge #4.3.B: On the dance floor ⸺ Open one of your previous programs
# that made the robot drive in a square. Use multitasking (concurrent) code
# to make it blink a blue light on the straights and blink a red light while 
# making turns. Can you make it play a well-known melody along the way?
# https://www.youtube.com/watch?v=VXUUibKrono&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

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

async def drive_square_dance(side_length):
    for i in range(4):
        await multitask(
            drive_base.straight(side_length),
            change_color(Color.BLUE)
        )
        await multitask(
            drive_base.turn(90),
            change_color(Color.RED)
        )
    blinking["active"] = False
    hub.light.off()

async def dance_square(side_length):
    await multitask(
        blink(),
        drive_square_dance(side_length),
        play_melody()
    )

# Challenge #4.3.C: On the dance floor, with functions ⸺ Open the solution that you
# made for Challenge #4.3.B. Create a function that drives straight for 250 mm
# while blinking a blue light. Unlike the previous example, this time place the
# multitasking (concurrent) code inside the function. Next, create another function for
# turning 90 degrees while blinking a red light. Once you have created these,
# where should you place the function calls to make the robot drive in
# a square while blinking the lights as instructed?
# https://www.youtube.com/watch?v=VXUUibKrono&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

async def straight_task(side_length):
    await multitask(
        drive_base.straight(side_length),
        change_color(Color.BLUE)
    )

async def turn_task(angle):
    await multitask(
        drive_base.turn(angle),
        change_color(Color.RED)
    )

async def drive_square_tasks(side_length):
    for _ in range(4):
        await straight_task(side_length)
        await turn_task(90)
    blinking["active"] = False
    hub.light.off()

async def dance_square_tasks(side_length):
    await multitask(
        blink(),
        drive_square_tasks(side_length),
        play_melody()
    )

# Challenge #4.3.D: Multitasking efficiently ⸺ The previous example runs four
# functions (stacks of code) at the same time. However, you can achieve the same
# result with just three functions. Adjust your multitasking (concurrent) code to
# reduce it to three tasks. You will see two print statements and a wait command
# floating in your code. Where should you place them to achieve the same
# result as before? You may delete code if needed.
# https://www.youtube.com/watch?v=NLfy1wkm6Eo&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

async def combined_task():
    hub.light.on(Color.RED)
    await wait(500)
    print("Hello")
    hub.light.on(Color.GREEN)
    await wait(500)
    print("world")

async def run_multitask():
    await multitask(
        left_motor.run_angle(500, 360),
        hub.speaker.beep(500, 100),
        combined_task(),
    )

# Challenge #4.4.A: Backing up! ⸺ Create a program similar to the example
# above, but make the DriveBase drive backwards for 250 mm instead of turning
# a single motor. The robot should back up by 250 mm but stop trying if it
# doesn’t get there in two seconds. Discuss ⸺ When is this technique useful
# in robotics competitions? How is this different from just driving in reverse
# for two seconds? What are the pros and cons of either approach?
# https://www.youtube.com/watch?v=pY8U6NyP9rA&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

async def drive_back(distance):
    await drive_base.straight(-distance)
    print(f"Backed up {distance} mm!")

async def timeout(time):
    await wait(time)
    print("I got stuck!")

async def backing_up(distance,time):
    await multitask(
        drive_back(distance),
        timeout(time),
        race=True
    )

# Challenge #4.4.B: Everything at once ⸺ Analyze the example above before
# you run it. What will it do? Can you definitively say which order the printed
# messages will be in? If not, what does it depend on? Is it possible to use
# multiple function calls instead of multitasking (concurrent) code? If not,
# how close can you get to the same output? Which differences remain?
# https://www.youtube.com/watch?v=CQXbLyL-RZg&list=PLjWRBRiZoAREPd1psLxDFbguaKq5NnDLl

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

async def run_subtasks():
    await multitask(
        subtask(),
        subtask2(),
        race=True,
    )

def main():
    run_task(run_subtasks())

if __name__ == "__main__":
    main()