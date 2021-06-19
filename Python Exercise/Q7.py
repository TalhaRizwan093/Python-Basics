#Program  that prompts the user to enter two sorted lists and displays the mergedlist

#Main function
def main():
    import sys             #For adding exit function if user is not entring sorted list
    test_list1 = []        #Temporary lists
    test_list2 = []
    length1 = eval(input("Enter length of lst1:"))      #Prompts user to enter length of Lists
    length2 = eval(input("Enter length of lst2:"))
    prev1 = 0
    prev2 = 0
    
    #Input for both sorted lists if the list is not in sorted form program will break and exit
    for i in range (0,length1):
        val1 = eval(input("Enter values for list1:"))

        #Condition if user enters non sorted list as program only works with sorted list
        if prev1 > val1:
            print("Please enter values in acending order and re-run the program")
            sys.exit()
        else:
            test_list1.append(val1)
        prev1 = val1

    for i in range (0,length2):
        val2 = eval(input("Enter values for list2:"))
        
        #Condition if user enters non sorted list as program only works with sorted list
        if prev2 > val2:
            print("Please enter values in acending order and re-run the program")
            sys.exit()
        else:
            test_list2.append(val2)
        prev2 = val2


    # printing original lists
    print ("The original list 1 is : " ,test_list1) 
    print ("The original list 2 is : " ,test_list2)

    merge(test_list1,test_list2)


#Function for merging two sorted list to creat a new merged sorted list 
def merge(list1,list2):
    result = [] 
    i, j = 0, 0
    
    #Loop for comparision of values of both lists
    while i < len(list1) and j < len(list2): 
        if list1[i] < list2[j]:     #Condition if list1 elements are less then it will append it in order
          result.append(list1[i]) 
          i += 1

        else:                       #If not it will append list2 elements in order
          result.append(list2[j]) 
          j += 1
    for x in range(i,len(list1)):
        result.append(list1[x])
    for y in range(j,len(list2)):
        result.append(list2[y])
 

    # printing result 
    print ("The combined sorted list is : " ,result)
    
main()

#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
