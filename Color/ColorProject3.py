from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def DetectArmStall(arm, speed, angle, maxLoad):
   arm.reset_angle(0)
   arm.run(angle)
   while abs(arm.load()) < abs(maxLoad):
       print("======", arm.load())


       if abs(arm.angle()) < abs(angle):
           wait(1)
       else:
           break
   arm.hold()

def MoveArmWithStallTimeDetection(arm, speed, angle):
   arm.reset_angle(0)
   arm.run(angle)
   watch = StopWatch()
   while abs(arm.angle() < abs(angle)):
       if watch.time() > 700:
           break
   arm.hold()