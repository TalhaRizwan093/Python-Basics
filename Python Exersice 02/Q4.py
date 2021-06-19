#Program that eads an integer between 0 and 1000 and adds all the digits in the integer

#Promts user to enter the number between 0 and 1000
num = eval(input("Enter a number between 0 and 1000: "))

#Calculation of sum of each digit

digit_1 = num % 10                         # Extract the last digit

num //= 10                                 # Removes the extracted digit

digit_2 = num % 10                         # Extract the last digit

digit_3 = num // 10                        # Removes the extracted digit

sum = digit_1 + digit_2 + digit_3

#Prints the sum of digits
print ("The sum of the digits is",sum)
