#Python program which accepts a 4 digit binary numbers as its input and check if the number is even or not

#Promts user to enter 4 digit binary number
number = eval(input("Enter a 4 digit binary number:"))

length = len(str(number))

#Calculation for extracting each digit so that we can convert it into decimal
bin_number = number
n1 = number % 10                           
number //= 10
n2 = number % 10
number //= 10
n3 = number % 10
number //= 10
n4 = number % 10

#Converting provided binary number into decimal equavilant
decimal_eqv = (n4 * 2**3) + (n3 * 2**2) + (n2 * 2**1) + (n1 * 2**0)

if length == 4:
    if decimal_eqv % 2 == 0:
        print("Binary number",bin_number ,"is an even number and its Decimal equavilant is ",decimal_eqv)
    else:
        print("Binary number",bin_number ,"is an Odd number and its Decimal equavilant is ",decimal_eqv)
else:
    print("Please provide 4 digit binary number")
