# Program that plays the popular scissor-rockpaper game

import random   #Random library 

comp_wins = 0
user_wins = 0

#Loop for games until computer or user wins more then 2 times
while comp_wins <= 2 and user_wins <= 2:
    
    user_choice = eval(input("Slect  scissor, rock, and paper 0,1,2 respectively:")) #Prompts the user to enter his choice
    
    computer = random.randint(0,2)
    
    #Check the conditions according to the game rules
    if user_choice == computer:
        print("Draw")
        
    elif user_choice == 0:        
        if computer == 1:
            print("Scissor is knowked by rock you lost \n")
            comp_wins += 1
            
        else:
            print("Paper is cut into piecies by scissor you won \n")
            user_wins += 1
            
            
    elif user_choice == 1:
        if computer == 0:
            print ("Scissor is knowked by rock you won \n")
            user_wins += 1
            
        else:
            print ("Rock is wrapped by paper you lost \n")
            comp_wins += 1
            
            
    elif user_choice == 2:
        if computer == 0:
            print("Paper is cut into piecies by scissor you lost \n")
            comp_wins += 1
            
        else:
            print("Rock is wrapped by paper you won \n")
            user_wins += 1
            
    else:
        print("wrong input")
        
    print("Your scores........",  user_wins , "Computer scores........",  comp_wins) #Scores of computer and User

 #Prompts the Final Result   
if comp_wins > 2:
    print("You lose the game")
else:
    print("You won the game")


#Made by Talha Rizwan SP20-BSE-093
#Copyrights Reserved
