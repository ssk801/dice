#01feb2021
#another histo, but this time for 3d6
#note offset has changed to -3

import random

def d6():
    return random.randint(1,6)

histo=[]

for i in range (1,17):
    histo.append(0)

print(histo)
print(len(histo))

for j in range(1,100000):
    roll=d6()+d6()+d6()
    #print(roll)
    histo[roll-3]+=1

print(histo)
