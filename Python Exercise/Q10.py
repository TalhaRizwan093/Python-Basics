#Program that prompts the user to enter the employee record and displays it in decreasing order of the total hours.

#Function for assigning days for simplicity
def day_assign(n):
    if n == 0:
        return "Monday"
    elif n == 1:
        return "Tuesday"
    elif n == 2:
        return "Wednesday"
    elif n == 3:
        return "Thursday"
    elif n == 4:
        return "Friday"
    elif n == 5:
        return "Saturday"
    elif n == 6:
        return "Sunday"

# Defination of displayEmployee Function
def displayEmployee(record):
    total_hours = []             #List of total hours
    th = 0                       #Variable of total hours that stores total hours of current employee that is added
    k=0                          #Temporary Variable
    hours = []                   #List where all hours of employees are save
    employees = []               #List where employes with their hours are save
    for i in range(0,record):    #Loop for inputting working hours of 7 days
        employees.append(i)      #Appends the Employee number first
        print("Enter working hours of employee",i,"From sunday to saturday") 
        for j in range(0,7):
            print("Enter hours of", day_assign(j), end = " ")
            val = eval(input())   #Prompts user to enter working hours of employees on each day
            hours.append(val)    #Appends each hour to hours list
            if j == 6:           #Condition runs when 1 employee get his whole record
            
                while k < len(hours):    #This loop Adds all the hours of 1 employee
                    th = hours[k] + hours[k+1] + hours[k+2] + hours[k+3] + hours[k+4] + hours[k+5] + hours[k+6]  #Adds all the hours of 1 employee
                    total_hours.append(th)    # Appends the total hours of each employee in the total hours list
                    employees.append(th)      #Appends the total hours of employee. This list have the employee number alse
                    th = 0                    #Making total hour variable 0 because it will not add to the hours of previouse employee
                    k = k + 7                 #Jumps 7 because we need 1 employee data at a time
                
    total_hours.sort(reverse=True)            #Sort the list in decreasing order
    print("           \t Su\t M\t Tu\t W\t Th\t F\t Sa")     #Prints the Days on top
    employe = 0
    for i in range(0,len(hours),7):          #Loop for printing record As given in Question
        print("Employee",employe,'\t',hours[i],'\t',hours[i+1],'\t',hours[i+2],'\t',hours[i+3],'\t',hours[i+4],'\t',hours[i+5],'\t',hours[i+6])
        employe += 1
    count = 0
    for ch in total_hours:
        if ch == 0:
            count += 1
        else: 
            continue
    printing = 0
    prev = 0
    for i in range(0,len(total_hours)):      #Loops for printing total hours with employees number in decreasing order
        for j in range(0,len(employees)):    #This loop itrates on the values of employees
            if total_hours[i] == employees[j]: # This condition will check if the hours both list got are same if yes then employee - 1 is the number of that particular employee
                if employees[j-1] < len(total_hours):
                    if total_hours[i] == 0 and employees[j] == 0:
                        if count > printing:   # This condition stop 0 hours worker to print again and again
                            prev = employees[j-1]
                            if prev == employees[j-1]:
                                print("Employee", employees[j-1] ,"Worked or",total_hours[i],"hours")
                                printing += 1
                        else:
                            continue
                            
                    else:    
                        print("Employee", employees[j-1] ,"Worked or",total_hours[i],"hours")     #Prints the employes total hours in decreasing order

def main():
    num_employees = eval(input("Enter number of employees:"))
    displayEmployee(num_employees)
    
main() 


#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
