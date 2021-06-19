#Program to find four perfect numbers less then 10000

#Add variable for using in loop
add = 0

#Outer loop for itrating through all numbers from 1 - 10000
for i in range(1,10001):
    
    #Inner loop for itrating until the value of outer loop for checking each number
    for j in range(1, i):
        
        #Condition for checking sum of its proper divisors is exactly equal to the number.
        if(i % j == 0):
            add = add + j
    if (add == i):
        print(i,"is a Perfect Number")
    add = 0
    
#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
