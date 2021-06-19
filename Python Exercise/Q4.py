#Program that prints the elements that appear in the list only once


num_list = []
temp_list = []
final_list = []
count = 0


length = eval(input("Enter length of list you have:"))     #Prompts user to enter the length of list
 
for i in range(0,length):                                 #loop for input of numbers in list
    value = eval(input("Enter numbers for list:"))
    num_list.append(value)
    
temp_list = num_list                                      #temporary variable for storing the value of list

for i in range(0,length):
    for j in range (0, length):                           #Numbers of temporary list will check on all numbers of num_list
        if temp_list[i] == num_list[j]:
            count += 1                                    #If count value is 1 it means number only appears once
    if count == 1:
        final_list.append(temp_list[i])                   #Makes a final list of all single occurance numbers
    count = 0

print("The orignal list that is entered is",num_list)
print("Elements that appears only once are",final_list)                                         #Prints the list

#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
