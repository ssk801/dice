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
