from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

ORANGE_HIGH = 20
ORANGE_LOW = 0

RED_HIGH = 360
RED_LOW = 350

MAGENTA_HIGH = 342
MAGENTA_LOW = 330

BLUE_HIGH = 225
BLUE_LOW = 210

PURPLE_HIGH = 250
PURPLE_LOW = 230

YELLOW_LOW = 45
YELLOW_HIGH = 60

GREEN_LOW = 150
GREEN_HIGH = 165

color_sensor_side = ColorSensor(Port.B)

def determineColor():
    myHSV = color_sensor_side.hsv(True)
    myColor = color_sensor_side.color(True)

    if(Color.RED == myColor):
        if(myHSV.h > ORANGE_LOW and myHSV.h < ORANGE_HIGH and myHSV.v > 20):
            return "Orange"
        elif(myHSV.h > RED_LOW and myHSV.h < RED_HIGH and myHSV.v > 20):
            return "Red"

    if(Color.BLUE == myColor):
        if(myHSV.h > PURPLE_LOW and myHSV.h < PURPLE_HIGH and myHSV.v > 20):
            return "Purple"
        elif(myHSV.h > 210 and myHSV.h < 225 and myHSV.v > 20):
            return "Blue"

    if(Color.YELLOW == myColor):
        if(myHSV.h > YELLOW_LOW and myHSV.h < YELLOW_HIGH and myHSV.v > 20):
            return "Yellow"

    if(Color.GREEN == myColor):
        if(myHSV.h > GREEN_LOW and myHSV.h < GREEN_HIGH and myHSV.v > 20):
            return "Green"

    return "UNKNOWN"

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