#Program that prompts the user to enter three integers and displays them in increasing order

num1 = eval(input("Enter first number to check:"))
num2 = eval(input("Enter second number to check:"))
num3 = eval(input("Enter third number to check:"))

#Conditional statements to evaluate 
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print("Increasing order of given numbers is",num3, num2, num1)
    else:
        print("Increasing order of given numbers is",num2, num3, num1)

elif num1 < num2 and num2 > num3:
    if num1 > num3:
        print("Increasing order of given numbers is",num3, num1, num2)
    else:
        print("Increasing order of given numbers is",num1, num3, num2)
        
elif num1 < num3 and num2 < num3:
    if num1 > num2:
        print("Increasing order of given numbers is",num2, num1, num3)
    else:
        print("Increasing order of given numbers is",num1, num2, num3)
else:
    print("All numbers are same")
