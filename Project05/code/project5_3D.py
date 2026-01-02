from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
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

    while distance_sensor.distance() > 150:
        wait(10)

    while distance_sensor.distance() < 400:
        wait(10)

    drive_base.stop()
    drive_base.turn(90)