#Program that tells the length of the widest fragment in a sequence

#Prompts user to enter the first number of the sequence
number = eval(input("Enter sequence:"))
prev = number # A variable which stores the previous value of sequence 
count = 1
final = 1

#loop for entering the sequence until 0 is entered in sequence
while number != 0:
    number = eval(input("Enter sequence:"))
    if number == prev:     #Condition for checking if previouse and current numbers are same
        number = prev
        count += 1         # If both are same then Count variable will get an increment in it
        
        
    #Condition will run if the previous number is not same   
    else:
        if count > final: # If count is greater then final it will assign count value to final
            final = count
        count = 1         # Count will get back to 1 because the previous value is not same
        prev = number
    
print ("The length of widest fragment is: ", final)    #Prints the final result

#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
