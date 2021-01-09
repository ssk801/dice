#dice
#09jan2021
#code for rolling various numbers of dice with various numbers of of sides

#needed for random number generation
import random

#single roll of fixed side number
def d4():
  return random.randint(1,4)

def d6():
  return random.randint(1,6)
  
def d8():
  return random.randint(1,8)

def d10():
  return random.randint(1,10)
  
def d20():
  return random.randint(1,20)

#single roll of any side number
def dn(n):
  return random.randint(1,n)
  
#multiple rolls of any side number
#use: ndn(a,b) where a is number of dice and b is number of sides
def ndn(a,b):
  rolls=[]
  for num in range(a):
    rolls.append(random.randint(1,b))
  return rolls
 
