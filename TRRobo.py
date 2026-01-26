from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch

class TRRobot:
    def __init__(
        self,
        left_motor_port=Port.C,
        right_motor_port=Port.D,
        distance_sensor_port=Port.A,
        color_sensor_port=Port.B,
        wheel_diameter=56,
        axle_track=110,
        default_speed=250
    ):

        self.hub = PrimeHub()

        self.left_motor = Motor(left_motor_port, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(right_motor_port)

        self.distance_sensor = UltrasonicSensor(distance_sensor_port)
        self.color_sensor = ColorSensor(color_sensor_port)

        self.watch = StopWatch()

        self.drive_base = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=wheel_diameter,
            axle_track=axle_track
        )

        self.drive_base.settings(straight_speed=default_speed)
        self.drive_base.use_gyro(True)

    def SetGyro(self, enabled: bool):
        self.drive_base.use_gyro(enabled)

    def SetSpeed(self, speed):
        self.drive_base.settings(straight_speed=speed)

    def MoveForward(self, distance):
        self.drive_base.straight(distance)

    def MoveBackward(self, distance):
        self.drive_base.straight(-distance)

    def TurnRight(self, degrees):
        self.drive_base.turn(degrees)

    def TurnLeft(self, degrees):
        self.drive_base.turn(-degrees)

    async def MoveForward_As(self, distance):
        await self.drive_base.straight(distance)

    async def MoveBackward_As(self, distance):
        await self.drive_base.straight(-1* distance)

    async def TurnRight_As(self, degrees):
        await self.drive_base.turn(degrees)

    async def TurnLeft_As(self, degrees):
        await self.drive_base.turn(-1* degrees)

    async def moveArmUp(self, arm, speed, angle):
        await self.arm.run_angle(speed, angle)

    async def moveArmDown( self,arm, speed, angle):
        await self.arm.run_angle(speed, -1 * angle)