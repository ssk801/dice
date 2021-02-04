#04feb2021
#generates a list of figures representing the frequency of sums from the rolling of nd6
#calculates the appropriate array length to hold all possible values

import random

def d6():
    return random.randint(1,6)

histo=[]

nn=input()
n=int(nn)

for i in range (1,n*5+2):
    histo.append(0)

for j in range(1,100000):
    roll=0
    for k in range(n):
        roll+=d6()
    histo[roll-n]+=1

print(histo)

