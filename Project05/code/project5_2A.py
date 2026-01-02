from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

color_sensor = ColorSensor(Port.B)
distance_sensor = UltrasonicSensor(Port.A)

#5.2.A: Comparing the other way
while True:
    print('Distance:', distance_sensor.distance())
    print('Is it close?', not distance_sensor.distance() > 500)
    wait(250)
