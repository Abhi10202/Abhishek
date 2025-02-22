import random

print("-----------------------------------")
print("This is a Snake Water Gun Game !!!! ")
print("-----------------------------------")

print("Choose Any One \n1)rock \n2)paper \n3)scissors")

def wins ():
    global i
    print(f"your input {user} and computer choose {system}")
    print("................................")
    print("          you win the game ")
    print("................................")
    i+=1
    print(f"total score is < {i} >")
        

def lose():
    print(f"your input {user} and computer choose {system}")
    print("................................")
    print("<<       you lose the game >>")
    print("................................")
    print(f"total score is < {i} >")

i=0
while (True):
    
    computer=["rock","paper","scissor"]
    system=random.choice(computer)
    user=input("Choose >> ")
    luser=user.lower()
    if luser==system:
        print(f"your input {user} and computer choose {system}")
        print("................................")
        print("             Tie !! ")
        print("................................")  
        print(f"total score is < {i} >")
        

    elif luser=="paper" and system == "rock":
        wins()

    elif luser=="rock" and system== "paper":
        lose()
        
    elif luser =="scissor" and system=="paper":
        wins()

    elif luser =="paper" and system=="scissor":
        lose()

    elif luser=="rock" and system=="scissor":
        wins()

    elif luser=="scissor" and system =="rock":
        lose()
    
    replay=input("Have you play more ? yes/no  : ")
    if replay.lower()=="yes":
        pass
    else:
        break 





