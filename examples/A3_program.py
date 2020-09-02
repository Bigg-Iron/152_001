'''
 3.12 A3 Program
 You must implement the lawOfCosines and distance functions. Comments are provided to guide your implementation. The main function is provided for you.

You will need to use the Python functions imported from the math module on line 4. Note that the inputs are in degrees, but the functions take radians so you will need to convert them using the radians function in the math module.

Sample input
This sample input computes the diagonal distance for the state of Colorado. The latitude boundaries are 37 to 41 degrees, while the longitude boundaries are -102 to -109 degrees. The geographic coordinates represent the southeast and northwest corners of the state. The radius of the earth is given in miles.

37
-102
41
-109
3959

Sample output
In zyBooks the output does not include the input values so you should only see the prompts, each on a separate line. The final line shows the tuples for the geographic points and the integer distance.

latitude  #1?
longitude #1?
latitude  #2?
longitude #2?
radius of earth?
the distance from (37.0, -102.0) to (41.0, -109.0) is 466 '''

# Great Circle Distances between geographic points

# import the math functions we need.
from math import radians, acos, sin, cos, fabs

def lawOfCosines(geo1, geo2):
    # The geographic coordinates are tuples with latitude and longitude values
    pass
	# convert the geographic coordinates to radians and compute absolute differences
	# Use the Law of Cosines formula to determine the central angle


def distance(radius,centralAngle):
    # The distance is the radius of the earth times the calculated central angle
    d = radius * centralAngle
	# Return the unrounded integer distance
    pass


def main():
	# obtain two geographic points as tuples
	geo1 = (float(input('latitude  #1?\n')), float(input('longitude #1?\n')))
	geo2 = (float(input('latitude  #2?\n')), float(input('longitude #2?\n')))
	# obtain the radius of the earth
	radius = float(input('radius of earth?\n'))
	# print distance between points
	dis = distance(radius, lawOfCosines(geo1, geo2))
	print('the distance from', geo1, 'to', geo2, 'is', dis)


# do not change the following code
if __name__ == '__main__':
    main()


