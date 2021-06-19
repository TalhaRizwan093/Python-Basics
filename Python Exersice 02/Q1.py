#Program to calculate average speed of a runner

#Distance a runner runs in Kilometer
distance_in_kilo = 14

#Distance a runner runs in Miles
distance_in_miles = 14 / 1.6

#Time taken by runner in hours, time in minutes seconds is given
time_in_min = 45
time_in_sec = 30
time_in_hr = (45 / 60) + (30 / 3600) #45 minutes and 30 seconds are converted into hours

#Formula for calculating average speed in seconds
avg_speed = distance_in_miles / time_in_hr

#Prints the average speed of runner on console
print ("Average speed of runner in miles per hour is", format(avg_speed,".2f"))
