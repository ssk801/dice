#01feb2021
#generates a list of figures representing the frequency of sums from the rolling of 2d6
#min sum is 2, max is 12 so there are 11 possible outcomes
#note -2 index offset to cater for this and not have empty places in the list

import random

def d6():
    return random.randint(1,6)

histo=[]

for i in range (1,12):
    histo.append(0)

for j in range(1,100000):
    roll=d6()+d6()
    histo[roll-2]+=1

print(histo)
