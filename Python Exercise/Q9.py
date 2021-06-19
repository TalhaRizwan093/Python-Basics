#Program  that prompts the user to enter the year and first day of the year, and displays the first day of each month in the year


#Prompts user to enter Year and the first day of that year
year = eval(input("Enter year:"))
day = eval(input("Choose the first day of the year:\n 1 for Monday\n 2 for Tuesday \n 3 for Wednesday \n 4 for Thursday \n 5 for Friday \n 6 for Saturday \n 7 for Sunday. \n Choice is yours: "))
temp = 0

#Function for assigning day to numbers as per sake of simplicity
def day_assign(n):
    if n == 1:
        return "Monday"
    elif n == 2:
        return "Tuesday"
    elif n == 3:
        return "Wednesday"
    elif n == 4:
        return "Thursday"
    elif n == 5:
        return "Friday"
    elif n == 6:
        return "Saturday"
    elif n == 7:
        return "Sunday"

#List of all months
month = ["February","March","April","May","June","July","August","September","Octuber","November","December"]

#Prints the first day of the year as it was given by user
print("January 1,", year , "is", day_assign(day))

#Loop for each month
for i in range(0,11):
    
    #Condition if the month is of 31 days
    if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9:
        for j in range(1,31+1):  #Loop for itrating of days 31 times to extract the last number of day
            if day == 7:         #Condition if 1 week is complete
                day = 1
            else:
                day += 1         #increments the day + 1 until the first date of new month that is needed
        temp = day_assign(day)
        
        print(month[i] ,"1,", year , "is", temp)  #Prints the day
         
    if i == 1:                 #Loop for itrating pver days of february
        if year % 4 != 0:      #Condition for checking if the year is leap or not
            for j in range(1,28+1): #Loop for itrating of days 28 times to extract the last number of day
                if day == 7:        #Condition if 1 week is complete
                    day = 1
                else:
                    day += 1        #increments the day + 1 until the first date of new month that is needed
            temp = day_assign(day)
            print(month[i], "1,", year , "is", temp)  #Prints the day
        else:
            for j in range(1,29+1): #Loop for itrating of days 29 times to extract the last number of day
                if day == 7:        #Condition if 1 week is complete
                    day = 1
                else:
                    day += 1        #increments the day + 1 until the first date of new month that is needed
            temp = day_assign(day)
            print(month[i], "1,", year , "is", temp)  #Prints the day
                
    #Condition if the month is of 30 days
    if i == 3 or i == 5 or i == 8 or i == 10:
        for j in range(1,30+1):    #Loop for itrating of days 30 times to extract the last number of day
            if day == 7:           #Condition if 1 week is complete
                day = 1
            else:
                day += 1           #increments the day + 1 until the first date of new month that is needed
        temp = day_assign(day)
        print(month[i] ,"1,", year , "is", temp) #Prints the day

#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
