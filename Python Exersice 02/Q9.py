#Program that prompts the user to enter a three-digit integer and determines whether it is a palindrome number

#Promts user to input 3 digit integer
num = eval(input("Enter a three digit integer: "))
length = len(str(num))

#Calculation for extracting the first digit and the last digit

digit_3 = num % 10       #to extract the last digit
digit_1 = num // 100     #to extract the first digit

#Conditional statement for checking wheather the number is Palindrome or not
if length == 3:
    if digit_1 == digit_3:
        print(num, "number is Palindrome number")
    else:
        print(num, "number is not Palindrome number")
else:
    print("Number less then or greater then 3 digit cannot be palindrom")
