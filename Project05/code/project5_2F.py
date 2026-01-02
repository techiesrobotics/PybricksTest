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


while True:
    if distance_sensor.distance() <= 500:
        drive_base.stop()
    else:
        drive_base.drive(200, 0)
    wait(0)