from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from TRDriveBase import *

# Challenge #5.1.C: Measure and share ⸺ The technique to display sensor
# values works with any sensor. You’ll learn to use all sensors in the coming
# chapters, but you can already explore what they measure now. Create programs
# similar to the one above, but set up different sensors. Presentation ⸺ Each
# team member explores one sensor in detail. If a sensor can measure more than
# one thing, coordinate the extra work with your team. For each sensor, create
# a short demonstration and take turns presenting your findings. What can your
# sensor measure? How accurate is it? Try it under various conditions, such as
# in the dark or outside. Is there anything that surprised you?

def color_sensor_data():
    print(
        "Color:", color_sensor.color(),
        "| Reflected:", color_sensor.reflection(),
        "| Ambient:", color_sensor.ambient()
    )

def distance_sensor_data():
    print("Distance (mm):", distance_sensor.distance())

# Challenge #5.1.D: Where did the time go? ⸺ In the experiment,
# the measurements are spaced almost exactly 100 ms apart. This might
# give you the impression that measuring and printing values takes no
# time at all. Actually, it only appears that way because 100 ms
# is plenty of time to send a few numbers to your computer in the background
# without holding up your program. If you print more text more quickly,
# you will see it start to impact the time. To see this, try reducing the
# wait time to 1 ms. Click the > icon on the Print block to add another
# value and make it print something like “looooooong text”. Analyze the
# time between the measurements. What is the smallest and biggest gap?
# Are the time differences constant or do they change a lot? Discuss ⸺ Could
# you have done the original experiment with the 100 ms pause without the 
# stopwatch block? Why is it still better to keep it?

def timed_distance(time_ms,repeat_amt):
    print('Time', 'Distance', 'Long Text', sep=",")
    for count in range(repeat_amt):
        print(watch.time(), distance_sensor.distance(), 'looooooong text', sep=",")
        wait(time_ms)

# Challenge #5.1.E: Ramp it up ⸺ Add two Drive Base Configuration blocks
# to your program to choose a new drive speed and acceleration. Verify that
# it reaches your configured top speed at the given acceleration. To verify
# the acceleration, take the change in speed and divide it by the time it took
# to get to top speed. You can determine this from the printed values or
# using a graph similar to the one above.
# https://www.youtube.com/watch?v=oOHQ9wL5cik&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

async def drive_motion():
    await MoveForward_As(250)
    await wait(500)
    await MoveBackward_As(250)
    await wait(500)

async def log_drive_data():
    print('Time', 'Distance', 'Speed', sep=",")
    while True:
        print(watch.time(), drive_base.distance(), drive_base.state()[1], sep=",")
        await wait(10)

async def run_experiment_51E():
    drive_base.settings(
        straight_speed=400,
        straight_acceleration=200
    )

    watch.reset()

    await multitask(
        drive_motion(),
        log_drive_data(),
        race=True,
    )

# Challenge #5.1.G: Where am I? ⸺ Create a program that records the Ultrasonic Sensor
# distance measurement as the robot turns around, as shown below. Place the robot
# in a corner and run the experiment. Create a graph with the robot angle on the
# x-axis and the sensor distance on the y-axis. An example result is given below.
# Based on the graph alone, can you determine the distances to the walls? What
# about the starting angle with respect to the walls? Discuss ⸺ Some data points
# appear to be missing (they are not behind the picture). Where are they? If you
# squint, you can almost see two line segments that dip down in the middle.
# Compare the angles of both dips. How far are they apart, and why? Why does a
# line graph not work in this case? Some angles appear to have multiple clearly
# distinct distance values. What does this overlap mean? Why does this occur just
# in between the two dips mentioned above? Why is it useful to show the robot
# angle on the x-axis instead of the time like we did so far?
# https://www.youtube.com/watch?v=myLchRl1XwA&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

async def rotate_robot():
    drive_base.reset()
    await TurnRight_As(360)
    await wait(200)

async def log_angle_distance():
    print("Angle,Distance")
    while True:
        angle = drive_base.angle()
        distance = await distance_sensor.distance()
        print(angle, distance, sep=",")
        await wait(10)

async def run_experiment_51G():
    watch.reset()

    await multitask(
        rotate_robot(),
        log_angle_distance(),
        race=True
    )

# Challenge #5.1.H: Hitting a wall ⸺ Now it is your turn to design and implement an
# experiment to determine the robot’s position. This time, have the robot drive
# in a square parallel to the walls of a corner, as shown below. You decide which
# values to record and plot in a graph. For example, you might record the Ultrasonic
# Sensor distance or drive base angle. For this experiment, choose time for the X-axis.
# Discuss ⸺ Before you run your experiment, sketch what you think the graphs will look like.
# Assume that you start in corner A and that Q is 250 mm and R is 500 mm. Run the experiment
# and verify your prediction. Next, run the experiment from starting position B, C, or D.
# Based on the data, ask your teammates where they think the robot started.
# https://www.youtube.com/watch?v=Z8QDkQSCFI4&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

async def drive_square(side_length=250):
    for _ in range(4):
        await MoveForward_As(side_length)
        await TurnRight_As(90)
        await wait(200)

# --- Log time, distance, speed ---
async def log_data():
    print("Time,Distance,Speed")
    while True:
        time_ms = watch.time()
        distance = await distance_sensor.distance()
        speed = drive_base.state()[1]
        print(time_ms, distance, speed, sep=",")
        await wait(10)

# --- Run the experiment ---
async def run_experiment_51H():
    drive_base.settings(straight_speed=300, straight_acceleration=200)
    watch.reset()
    await multitask(
        drive_square(),
        log_data(),
        race=True
    )

# Challenge #5.2.A: Comparing the other way ⸺ You can change how the
# comparison is performed by adjusting the comparison operator in code.
# For example, if you choose equals (==), then it will be True if
# the distance is exactly 500 mm but False for any other distance. How can
# you get the same results as in the example above but now without using the
# less than (<) operator? Hint ⸺ You don’t need to add any more code, but
# you may need to reorder one or more lines. There are two solutions.

def distance_less_than_500_not():
    if not distance_sensor.distance() >= 500:
        print("Object is closer than 500 mm")
    else:
        print("Object is further than 500 mm")

def distance_less_than_500_swapped():
    if 500 > distance_sensor.distance():
        print("Object is closer than 500 mm")
    else:
        print("Object is further than 500 mm")

# Challenge #5.2.B: Don’t move ⸺ Under some conditions, the program below
# won’t do anything at all. Why and when is that the case? Support your theory
# by adding a print statement to reveal the value of the comparison result just
# before and after the wait-until condition.
# https://www.youtube.com/watch?v=inFNQvN0Hag&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i


def distance_loop_compare():
    drive_base.drive(200, 0)

    print("Compare before loop:",
        distance_sensor.distance() <= 500)

    while not distance_sensor.distance() <= 500:
        wait(0)

    print("Compare after loop:",
        distance_sensor.distance() <= 500)

    drive_base.stop()

# Challenge #5.2.C: On the threshold ⸺ Change the example to wait until
# the sensor measures exactly 500 mm and try it out. Discuss ⸺ What will
# the program do now? Does it always do that in practice, or does it run
# into the wall more often? Why is that?
# https://www.youtube.com/watch?v=f6Ry-bsmtJA&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def distance_threshold():
    drive_base.drive(200, 0)
    while not distance_sensor.distance() == 500:
        wait(0)
    drive_base.stop()

# Challenge #5.2.D: Left and right turns ⸺ This example always makes the
# robot turn right after seeing an obstacle. Can you make it alternate between
# taking left and right turns? Discuss ⸺ Is this better or worse in terms
# of getting stuck in corners?
# https://www.youtube.com/watch?v=oCj3YtC487M&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def alternate_turns():
    turn_right = True

    while True:
        drive_base.drive(200, 0)

        while not distance_sensor.distance() <= 500:
            wait(0)

        MoveBackward(250)

        if turn_right:
            TurnRight(120)
        else:
            TurnLeft(120)

        turn_right = not turn_right

# Challenge #5.2.E: Till dead batteries do us part ⸺ Previously, you have
# explored using an infinite wait loop to prevent a program from ending
# when its last lines finished running. Can you replicate its behavior
# with a conditional repeat loop? Hint ⸺ For comparison, create a
# separate program with just an infinite loop directly underneath
# the start of the program and inspect the code.
# Even if you’ve never coded before, many of the things you see should look
# familiar based on what you’ve just learned. Try to achieve the same result
# with the conditional repeat loop. You should now see exactly the same
# underlying code!

def loop_message(message,repeat_time):
    while True:
        print(message)
        wait(repeat_time)

# Challenge #5.2.F: If, else, or both? ⸺ The if/else statement and
# multitasking (concurrent) code look a bit alike. They both contain two or more stacks
# of code but they work quite differently. Discuss ⸺ Describe the key
# differences between them and explain when either of them are useful.
# https://www.youtube.com/watch?v=AAk9tvI2uP4&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def if_else():
    if distance_sensor.distance() <= 500:
        drive_base.stop()
    else:
        drive_base.drive(200, 0)
    wait(0)

# Challenge #5.2.G: Air guitar ⸺ Create a program that plays different
# notes for different measured distances. Use the table below to determine
# the frequencies for each note. For a distance bigger than 300 mm, play C4;
# else if the distance is bigger than 270 mm, play D4, and so on. Can you
# play music on your new instrument? Discuss ⸺ Why is the order of the
# distance comparisons important? Try mixing them up and determine if you
# can still hit all notes. Why not?
# https://www.youtube.com/watch?v=9GRMmui8_r4&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def distance_tone():
    sensor = UltrasonicSensor(Port.A)
    
    MIN_DISTANCE = 40
    MAX_DISTANCE = 300

    MIN_FREQ = 261.63
    MAX_FREQ = 493.88

    while True:
        distance = sensor.distance()

        if distance < MIN_DISTANCE:
            distance = MIN_DISTANCE
        elif distance > MAX_DISTANCE:
            distance = MAX_DISTANCE

        freq = MIN_FREQ + (MAX_FREQ - MIN_FREQ) * ((distance - MIN_DISTANCE) / (MAX_DISTANCE - MIN_DISTANCE))

        hub.speaker.beep(freq, 50)
        wait(20)

# Challenge #5.2.H: In the flow ⸺ Draw the flow chart for the
# program below. Use the flow charts for the wall-avoidance and the
# wall-following on this page for inspiration.
# https://www.youtube.com/watch?v=oCj3YtC487M&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def avoid_wall():
    while True:
        drive_base.drive(200, 0)
        while not distance_sensor.distance() <= 500:
            wait(0)
        if distance_sensor.distance() <= 250:
            MoveBackward(250)
            TurnLeft(120)
        else:
            MoveBackward(250)
            TurnRight(120)

# Challenge #5.2.I: Uphill both ways ⸺ In the example above, it reverses
# in both cases before turning left or right. Could you use just a single
# reverse command by placing it before the if/else statement? Try this out.
# Discuss ⸺ You should find that it is not quite the same. It will
# mostly turn right if you wave your hand in front of the sensor, no
# matter how close. Why is that? Explain the difference with your flow
# chart from Challenge #5.2.H
# https://www.youtube.com/watch?v=oCj3YtC487M&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def avoid_wall_alt():
    while True:
        drive_base.drive(200, 0)

        while not distance_sensor.distance() <= 500:
            wait(0)

        current_distance = distance_sensor.distance()

        MoveBackward(250)

        if current_distance <= 250:
            TurnLeft(120)
        else:
            TurnRight(120)

# Challenge #5.2.J: Wait until you see it ⸺ The wait-until condition
# provides a simple and effective way to wait on a condition. Under
# the hood, it is actually just a conditional repeat loop without any
# code inside it: It repeatedly does nothing until the condition holds.
# Replicate the examples from the wait-until section on this page
# but replace the wait-until with a conditional repeat loop. How
# do you configure the condition? Test your programs
# to verify that they work just like the originals.
# https://www.youtube.com/watch?v=1PKN61uqOIY&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def wait_until_obstacle():
    drive_base.drive(200, 0)

    while True:
        if distance_sensor.distance() <= 500:
            break
        wait(0)

    drive_base.stop()

# Challenge #5.3.A: Stuck in a corner ⸺ With the program below, the robot
# has a tendency to get stuck in corners. When does this happen? Can you
# change a single setting in this program to ensure it finds a way out with
# fewer attempts?
# https://www.youtube.com/watch?v=uxc0q2aI89Q&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def bumper_turn():
    while True:
        drive_base.drive(200, 0)
        while not (Button.LEFT in hub.buttons.pressed() or Button.RIGHT in hub.buttons.pressed()):
            wait(0)
        if Button.RIGHT in hub.buttons.pressed():
            print('Left bumper hit!')
            MoveBackward(50)
            TurnRight(90)
        else:
            print('Right bumper hit!')
            MoveBackward(50)
            TurnLeft(90)

# Challenge #5.3.B: In range ⸺ Create a program that makes the robot play
# sounds while the Ultrasonic Sensor distance is between 300 mm and 600 mm.
# Hint ⸺ Use two comparison statements. One should check the upper bound
# and one should check the lower bound. Use a logical operator to combine
# both conditions. It is also possible to do this with just a single
# double comparison statement. How should you choose
# its settings to achieve the same result?
# https://www.youtube.com/watch?v=de2L3xMcEUM&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def beep_on_distance():
    while True:
        distance = distance_sensor.distance()

        if 300 <= distance <= 600:
            hub.speaker.beep(1000, 200)
        
        wait(100)

# Challenge #5.3.C: Eyes on the road ⸺ Create a program that makes the
# robot drive forward for 500 mm unless it runs into an obstacle sooner.
# Create a solution with a wait-until condition and multiple logical operators.
# Also create a solution with multitasking (concurrent) code. Presentation
# ⸺ Split the two approaches between team members and present your
# solutions to each other. Discuss the pros and cons of both methods.
# https://www.youtube.com/watch?v=ixqPfa6X_Z0&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def drive_until_condition():
    drive_base.reset()
    drive_base.drive(200, 0)

    while not (
        drive_base.distance() >= 500 or
        distance_sensor.distance() <= 200
    ):
        wait(10)

    drive_base.stop()

# Challenge #5.3.D: Wave to turn ⸺ Modify the obstacle-avoidance
# program in the previous section to respond to you waving in front
# of the sensor instead of any approaching object. Hint ⸺ When you
# wave your hand in front of the sensor, it detects a low value and then
# a high value. You could wait for these conditions just like waiting
# for a button press in the example above.
# https://www.youtube.com/watch?v=YNXbZEJ_3bA&list=PLjWRBRiZoARGk78h3BdMW4csmlazM5v3i

def wave_turn():
    while True:
        drive_base.drive(200, 0)

        while distance_sensor.distance() > 150:
            wait(10)

        while distance_sensor.distance() < 400:
            wait(10)

        drive_base.stop()
        TurnRight(90)

#---------------------------------------------------------------------

def main():
    run_task(run_experiment_51G())

if __name__ == "__main__":
    main()