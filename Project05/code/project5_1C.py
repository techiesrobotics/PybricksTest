from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, UltrasonicSensor
from pybricks.parameters import Port

hub = PrimeHub()

color_sensor = ColorSensor(Port.B)
distance_sensor = UltrasonicSensor(Port.A)

#5.1.C: Measure and share
while True:
    print("\nSelect sensor:")
    print("1 = Color Sensor")
    print("2 = Distance Sensor")
    print("q = Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(
            "Color:", color_sensor.color(),
            "| Reflected:", color_sensor.reflection(),
            "| Ambient:", color_sensor.ambient()
        )

    elif choice == "2":
        print("Distance (mm):", distance_sensor.distance())

    elif choice.lower() == "q":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
