from random import randint as rnd
import random
import datetime

#version 2.7 (yes skipped to 2.7)
#   Added type 6
#       (ax + b)² = a² + 2ab + b²
#       (ax - b)² = a² - 2ab + b²
#   Better type 1,2 number pair generation:
#       Higher difference
#       Always different unit digit
#   Better symbols in type 5*:
#       Replaced / with ÷ 
#       Replaced x with × 
#   Banned 5 as divisor in type4
#   Shows day of week on the top
#version 2.7.2 
#   multiple varibles will generate for type6


MUL = u'\u00D7'
DIV = u'\u00F7'
SQR = u'\u00B2'

same_denominator_allowed = False    #set condition weather same denominator can generate in type5
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
variables = list("abcdlmnpqrsxyz")

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

def same_unit_place(x,y):
    if str(x)[-1] == str(y)[-1]:
        return True
    else:
        return False

def timestamp():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    day = days[now.weekday()]
    print(date, day)

common = [[0 for _ in range(2)] for _ in range(5)]
used = []
f = 10
t = 100
eleven_multiple_encountered = False

for i in range(5):
    x = rnd(f,t-20)
    y = rnd(x,t)
    diff = 16

    while x in used or x%10==0 or x%100==0 or (x%11==0 and eleven_multiple_encountered):
        rn = unequally_distributed_rng()
        x = rn
        if rn%11==0:
            eleven_multiple_encountered=True
    used.extend([x,x+1,x-1])
        
    while y in used or y%10==0 or x%100==0 or y-x<diff or (x%11==0 and eleven_multiple_encountered) or same_unit_place(x,y):
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
    while y==5:
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


def type6():
    a = rnd(1,20)
    b = rnd(2,20)
    x = random.choice(variables)
    print(f"({a}{x} + {b}){SQR}")
    print(f"({a}{x} - {b}){SQR}")

def main():
    timestamp()
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
    print("\n    ---type6---\n")
    type6()
    print()

main()
