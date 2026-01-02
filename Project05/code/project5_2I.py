from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

def setup():
    hub = PrimeHub()

    distance_sensor = UltrasonicSensor(Port.A)
    left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.D)

    drive_base = DriveBase(
        left_motor,
        right_motor,
        wheel_diameter=56,
        axle_track=110
    )

    return hub, distance_sensor, left_motor, right_motor, drive_base

hub, distance_sensor, left_motor, right_motor, drive_base = setup()

# The main program starts here.
while True:
    drive_base.drive(200, 0)

    while not distance_sensor.distance() <= 500:
        wait(0)

    current_distance = distance_sensor.distance()

    drive_base.straight(-250)

    if current_distance <= 250:
        drive_base.turn(-120)
    else:
        drive_base.turn(120)