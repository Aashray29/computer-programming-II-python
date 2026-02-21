import random

n = int(input(" how many times do you want to play : "))
compcount = 0
yourcount = 0
yourdict = { "s" : 1 , "w":-1, "g" : 0}
reversedict = { 1 : "snake"  , -1 : "water",  0 : "gun" }
for i in range(1,n+1):
    computer = random.choice([-1,0,1])
    

    yourchar =  input("enter your choice : ")
    you = yourdict[yourchar]

    print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

    if computer == you:
        print("its draw !")
    
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("you win!")
        yourcount += 1
    
    else:
        print("you lose!")
        compcount += 1
    
print(f"you won {yourcount} times and computer won {compcount} times ")       
