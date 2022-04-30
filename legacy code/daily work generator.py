from random import randint as rnd

same_denominator_allowed = True # in type 5

def left(s,margin=4):             #aligns text to left to a given margin position
    s = str(s)
    return(" "*(margin-len(s))+s)

f,t = 10,100  # range to generate random numbers in type 1 and 2

common = [[0 for _ in range(2)] for _ in range(5)]
used = []
for i in range(5):
    x = rnd(f,t-20)
    y = rnd(x,t)

    while x in used or x%10==0:
        rn = rnd(f,t-20)
        x = rn
    used.extend([x,x+1,x-1])
        
    while y in used or y%10==0 or y-x<10:
        rn = rnd(x,t)
        y = rn
    used.extend([y,y+1,y-1])
    
    common[i][0] = x
    common[i][1] = y


def type1():

    for i in common:
        x,y = i
        print("{x} - {y}".format(x=x,y=y))

def type2():
    for i in common:
        x,y = i
        print("- {x} - {y}".format(x=x,y=y))
    
def type3(f1=10,t1=50,f2=50,t2=100):  #must be 2 digit
    x = rnd(f1,t1)
    y = rnd(f2,t2)
    while x%10==0 or x%10==1:
        x = rnd(f1,t1)
    while y%10==0 or y%10==1:
        y = rnd(f2,t2)

    print("{} x {}".format(y,x))

def type4(f1=100,t1=999,f2=3,t2=9):
    x = rnd(f1,t1)
    while x%100==0 or x%10==0:
        x = rnd(f1,t1)
    y = rnd(f2,t2)
    while y%10==0:
        y = rnd(f2,t2)
    print("{x} / {y}".format(x=x,y=y))

def type5(f=2,t=9):
    x = rnd(f,t)
    y = rnd(f,t)
    z = rnd(f,t)
    o = rnd(f,t)

    # x   y
    # - + -
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
        if not same_denominator_allowed:
            used.append(o)

    subtypes = ['+','-','x','/']
    for subtype in subtypes:
        print("{a}   {b}".format(a=x,b=y))
        print("- {s} -".format(s=subtype))
        print("{c}   {d}".format(c=z,d=o))
        print("\n")

def main():
    
    print("\n    ---type1---\n")
    type1()
    print("\n    ---type2---\n")
    type2()
    print("\n    ---type3---\n")
    type3()
    print("\n    ---type4---\n")
    type4()
    print("\n    ---type5---\n")
    type5()

main()