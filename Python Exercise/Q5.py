#Program to check the validity of password input by users.

#Prompts user to enter the Password
password = input("Enter password. Password must fullfil the following conditions \n • At least 1 letter between [a-z] and 1 letter between [A-Z].\n • At least 1 number between [0-9]. \n • At least 1 character from [$#@]. \n • Minimum length 6 characters. \n • Maximum length 16 characters. \n")

#Count variables for each condition for validation
digit_count = 0
lower_count = 0
upper_count = 0
char_count = 0
length = len(password)

#Condition for checking length according to the rules
if length < 6 or length > 16:
    print("wrong length")

#Loop for itrating over the characters of string and check weather it have the conditions that is given
for i in password:
    if i.isdigit():
        digit_count = 1
    elif i.islower():
        lower_count = 1
    elif i.isupper():
        upper_count = 1
    elif i == '$' or i == '#' or i == '@':
        char_count = 1
    else:
        continue

#Conditino if every conditions are fullfiled or not 
if digit_count == 1 and lower_count == 1 and upper_count == 1 and char_count == 1:
    print("Your Password is Valid")
else:
    print("Your Password is not Valid")


#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
