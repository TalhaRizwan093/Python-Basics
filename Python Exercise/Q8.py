#Program that displays the first 100 palindromic prime numbers

#Function that checks weather the number is prime or not
def isPrime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True

#Function that checks weather the number is Palindrome or not
def palindrome(num):
    Num=num
    r=0
    while num>0:
        digit = num % 10
        r = (r*10) + digit
        num = num // 10
    if Num==r:
        return True
    else:
        return False
    
#Main function
def main():
    num=2
    count = 1
    #Loop will run untill first 100 numbers are print
    while count <= 100:
        
        #COndition that checks if the number is prime as well as palindrome
        if isPrime(num)==True and palindrome(num)==True:
            
            #If condition is true it will print
            print(format(num, "8d"), end=" ")
            
            #COndition for checking if 10 numbers are printed then it prints a new line
            if count % 10 == 0:
                print()
            count = count + 1
        num += 1

#Call of main function        
main()

#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
