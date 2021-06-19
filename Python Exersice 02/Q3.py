#Program to calculates the energy needed to heat water from an initial temperature to a final temperature

#Promts user to enter amount of water in kilograms
amount_of_water = eval(input("Enter the amount of water in kilograms: "))

#Promts user to enter initial temperature
initial_temp = eval(input("Enter the initial temperature in degrees Celsius: "))

#Promts user to enter final temperature
final_temp = eval(input("Enter the final temperature in degrees Celsius: "))

#Calculation of energy needed
energy = amount_of_water * (final_temp - initial_temp) * 4184

#Prints energy needed on console
print("The energy needed to heat water from initial temperature",initial_temp, "to final tempurature",final_temp, "is",energy)
