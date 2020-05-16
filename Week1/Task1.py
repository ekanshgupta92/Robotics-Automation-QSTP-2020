import math


def PolarToCartesian():  # function to convert polar to cartesian coordinates
    print("Enter r and theta(in degrees):")
    r = float(input())  # input Radius
    theta = float(input())  # input Theta in degrees
    print("X = " + str(r*math.cos(math.radians(theta))))
    print("Y = " + str(r*math.sin(math.radians(theta))))


def CartesianToPolar():  # function to convert cartesian to polar coordinates
    print("Enter x and y coordinates:")
    x = float(input())  # input X coordinate
    y = float(input())  # input Y coordinate
    print("R = " + str(math.sqrt(x**2 + y**2)))
    print("theta = " + str(math.degrees(math.atan(y/x))) + "°")


# main code

print("1. Polar to Cartesian")
print("2. Cartesian to Polar")
print("Enter Choice : ")

choice = int(input())

if choice == 1:
    PolarToCartesian()

elif choice == 2:
    CartesianToPolar()

else:
    print("Invalid Input")  # if choice is not 1 or 2 display error message
