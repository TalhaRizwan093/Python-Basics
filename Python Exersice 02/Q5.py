#Program to calculate length of runway needed to takeoff for an airplane


#Promts user to enter the value of takeoff speed V and acceleration a
v,a = eval(input("Enter speed in (m/s) and acceleration in (m/s^2) respectivily:"))

#Calculation of length
length = (v*v)/(2*a)

#Prints the length of runway
print("The minimum runway length for this airplane is", format(length,".3f") , "meters")
