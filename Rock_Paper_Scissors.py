Human_Score = 0 
AI_Score = 0 
Ties = 0 
import random
from random import randint 
Options = ["rock","paper", "scissors" ]
Computer_Choice = Options[randint(0,2)]
x = "go" 

while x == "go": 
    Player_Choice = input("Please Select Your Choice of Weapon:")
    
    if Player_Choice == Computer_Choice:
        print("Both of you have chosen the same weapon. It's a tie.")
        Ties += 1
   
    elif Player_Choice == "rock" and Computer_Choice == "paper":
        print("Computer chose paper. Paper covers rock. Computer wins.")
        AI_Score += 1
    elif Player_Choice == "paper" and Computer_Choice == "rock":
        print("Computer chose rock. Paper covers rock. You win.")
        Human_Score +=1
    elif Player_Choice == "scissors" and Computer_Choice == "paper":
        print("Computer chose paper. Scissors cut paper. You win.")
        Human_Score += 1
    elif Player_Choice == "paper" and Computer_Choice == "scissors":
        print("Computer chose scissors. Scissors cut paper. Computer wins.")
        AI_Score +=1
    elif Player_Choice == "scissors" and Computer_Choice == "rock":
        print ("Computer chose rock. Rock crushes scissors. Computer wins.")
        AI_Score +=1
    elif Player_Choice == "rock" and Computer_Choice == "scissors":
        print ("Computer chose scissors. Rock crushes scissors. You win.")
        Human_Score += 1
    
    print("You have", Human_Score, "wins. The AI has", AI_Score, "wins. Y'all drew", Ties, "times.")
    