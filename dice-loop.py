#dice-loop
#01feb2021
#this one uses kbd input to get the number and type of dice you want to roll

import random

while True:
    print("Dice Roller")
    print("Please enter number of dice, then number of sides, seaparated by a space")
    
    num,sides=input().split()
    sum=0
    print("Rolls: ",end="")

    for x in range(int(num)):
        roll=random.randint(1,int(sides))
        sum+=roll
        print(roll,end=" ")
    print('\n'+"Sum: "+str(sum)+'\n')
