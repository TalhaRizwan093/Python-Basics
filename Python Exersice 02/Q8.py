#program that Prompts the user to enter a point (x, y) and checks whether the point is within the circle centered at (0, 0) with radius 10

import math

#Prompts user to input points
point1, point2 = eval(input("Enter a point with two coordinates:"))

#Center points are zero
cent_pnt1 = 0
cent_pnt2 = 0

#Radius given
radius = 10

#Calculation for checking wheather the point is in the circile with radius 10
ans = math.sqrt((point1 - cent_pnt1)**2 + (point2 - cent_pnt2)**2)

if ans < radius:
    print ("Point",(point1 , point2), "is in the circle")
elif ans > radius:
    print ("Point",(point1 , point2), "is not in the circle")
else:
    print("Point",(point1 , point2), "is on the boundry of the circile")
