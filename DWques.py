from random import randint as rnd
import math
import random
import datetime

#version 2.0
#Whats new: New name DWques (dew-kes, dukes, due-kwes)
#           Rebuilt from DWgen 2.6 codebase

now = datetime.datetime.now()
print("today's date:",now.strftime("%d/%m/%y"))

same_denominator_allowed = False    #set condition weather same denominator can generate in type5

def ind(index, number):             #allows to subscript numbers. x[y] would be ind(y,x)
    return int(str(number)[index])

def right(s,margin=4):              #aligns text to right with given margin position
    s = str(s)
    return(" "*(margin-len(s))+s)

def left(s,margin=4):               #adds margin after text
    s = str(s)
    return(s+" "*(margin-len(s)))

def unequally_distributed_rng():
    return random.choices(range(1000),range(1000,0,-1))[0]

common = [[0 for _ in range(2)] for _ in range(5)]
used = []
f = 10
t = 100
eleven_multiple_encountered = False

for i in range(5):
    x = rnd(f,t-20)
    y = rnd(x,t)

    while x in used or x%10==0 or x%100==0 or (x%11==0 and eleven_multiple_encountered):
        rn = unequally_distributed_rng()
        x = rn
        if rn%11==0:
            eleven_multiple_encountered=True
    used.extend([x,x+1,x-1])
        
    while y in used or y%10==0 or x%100==0 or y-x<10 or (x%11==0 and eleven_multiple_encountered):
        rn = unequally_distributed_rng()
        y = rn
        if rn%11==0:
            eleven_multiple_encountered=True
    used.extend([y,y+1,y-1])
    
    common[i][0] = x
    common[i][1] = y


def type1():

    for i in common:
        x,y = i
        print("{x}-{y}".format(x=x,y=y))

def type2():
    for i in common:
        x,y = i
        print("-{x}-{y}".format(x=x,y=y))
    
def type3(f1=50,t1=100,f2=10,t2=50):  #must be 2 digit
    x = rnd(f1,t1)
    y = rnd(f2,t2)
    while x%10==0 or x%10==1:
        x = rnd(f1,t1)
    while y%10==0 or x%10==1:
        y = rnd(f2,t2)

    a = ind(0,x)    
    b = ind(1,x)
    c = ind(0,y)
    d = ind(1,y)

    print(right(x))
    print("x"+right(y,3))
    print("----")

def type4(f1=100,t1=999,f2=3,t2=9):
    x = rnd(f1,t1)
    while x%100==0 or x%10==0:
        x = rnd(f1,t1)
    y = rnd(f2,t2)
    print("{} / {}".format(x,y))

def type5(f=2,t=9):
    x = rnd(f,t)
    y = rnd(f,t)
    z = rnd(f,t)
    o = rnd(f,t)

    # x   y
    # - + - =
    # z   o

    used=[]
    used.extend([x,y,z,o]) # TODO find and implement efficient way to stop repeating

    while x in used:
        x = rnd(f,t)
    used.append(x)

    while y in used:
        y = rnd(f,t)
    used.append(y)

    while z in used:
        z = rnd(f,t)
    if not same_denominator_allowed:
        used.append(z)

    while o in used:
        o = rnd(f,t)

    print("{a}   {b}".format(a=x,b=y))
    print("- + -")
    print("{c}   {d}".format(c=z,d=o))

    print("\n")

    print("{a}   {b}".format(a=x,b=y))
    print("- - -")
    print("{c}   {d}".format(c=z,d=o))

    print("\n")

    print("{a}   {b}".format(a=x,b=y))
    print("- x -")
    print("{c}   {d}".format(c=z,d=o))

    print("\n")

    print("{a}   {b}".format(a=x,b=y))
    print("- / -")
    print("{c}   {d}".format(c=z,d=o))


def main():
    
    print("\n     ---type1---\n")
    type1()
    print("\n     ---type2---\n")
    type2()
    print("\n     ---type3---\n")
    type3()
    print("\n     ---type4---\n")
    type4()
    print("\n     ---type5---\n")
    type5()

main()
