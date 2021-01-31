#dice-loop
#01feb2021
#this one uses kbd input to get the number and type of dice you want to roll

import random

while True:
    print("Dice Roller")
    print("Please enter number of dice, then number of sides, seaparated by a space")
    
    num,sides=input().split()
    for x in range(int(num)):
        print(random.randint(1,int(sides)),end=" ")
    print('\n')
