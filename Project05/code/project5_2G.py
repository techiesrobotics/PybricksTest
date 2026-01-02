from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
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
