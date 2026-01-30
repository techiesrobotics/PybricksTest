from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from TRRobo import *

robot = TRRobot()

# Arm Stall Example:
# https://youtu.be/bL0dzXLOrcA
async def DetectArmStall(arm, speed, angle, maxLoad):
    arm.reset_angle(0)
    arm.run(speed)

    while abs(arm.angle()) < abs(angle):
        print("====== load:", arm.load())

        if abs(arm.load()) >= abs(maxLoad):
            print("Motor was stalled")
            break

        wait(10)

    arm.hold()


async def MoveArmWithStallTimeDetection(
    arm,
    speed,
    angle,
    stall_time=700,
    min_movement=2
):
    arm.reset_angle(0)
    arm.run(speed)

    watch = StopWatch()
    last_angle = arm.angle()

    while abs(arm.angle()) < abs(angle):
        wait(1)
        current_angle = arm.angle()

        if abs(current_angle - last_angle) > min_movement:
            watch.reset()
            last_angle = current_angle

        if watch.time() > stall_time:
            print("Motor was stalled")
            break

    arm.hold()

def main():
    run_task(MoveArmWithStallTimeDetection(robot.arm_motor,100,60))

if __name__ == "__main__":
    main()
