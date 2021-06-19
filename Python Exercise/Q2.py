#Program that checks equal numbers in a sequence and tells how much of them are same

#Prompts the user to enter the sequence of three numbers
num1 , num2 , num3 = eval(input("Enter three numbers seperated with comma: "))

#Conditions for checking wheather the numbers are same or different
if num1 == num2 and num1 == num3:
    print("3")
elif num1 == num2:
    if num1 != num3:
        print("2")

elif num1 == num3:
    if num2 != num1:
        print("2")
        
elif num2 == num3:
    if num2 != num1:
        print("2")

else:
    print("0")

#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved    
