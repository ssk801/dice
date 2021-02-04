#01feb2021
#generates a list of figures representing the frequency of sums from the rolling of 2d6
#min sum is 2, max is 12 so there are 11 possible outcomes
#note -2 index offset to cater for this and not have empty places in the list

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
        #print(roll)
    histo[roll-n]+=1

print(histo)
