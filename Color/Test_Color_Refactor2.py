from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Color values were obtained from looped data set
# The values used are the lowest and highest numbers found between 2cm - 8cm
COLORS = {
    "RED":    {"H": (330, 355), "S": (43, 91), "V": (1, 52)},
    "YELLOW": {"H": (19, 53),   "S": (55, 77), "V": (1, 75)},
    "GREEN":  {"H": (120, 180), "S": (36, 75), "V": (1, 19)},
    "BLUE":   {"H": (210, 240), "S": (55, 91), "V": (1, 32)},
}

color_sensor_side = ColorSensor(Port.B)

def is_color(h, s, v, color_name):
    thresholds = COLORS[color_name]
    h_min, h_max = thresholds["H"]
    s_min, s_max = thresholds["S"]
    v_min, v_max = thresholds["V"]

    return h_min <= h <= h_max and s_min <= s <= s_max and v_min <= v <= v_max

def determineColor():
    myHSV = color_sensor_side.hsv(True)
    for color_name in COLORS:
        if is_color(myHSV.h, myHSV.s, myHSV.v, color_name):
            return color_name
    return "NONE"


def repeatColor():
    while True:
        myHSV = color_sensor_side.hsv(True)
        myColor = color_sensor_side.color(True)
        color_name = determineColor()
        print(myHSV,myColor)
        print(color_name)
        wait(100)

def main():
    repeatColor()

if __name__ == "__main__":
    main()