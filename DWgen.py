from random import randint as rnd
import random
import datetime

#version 2.7
#   Added type 6
#       (ax + b)² = a² + 2ab + b²
#       (ax - b)² = a² - 2ab + b²
#   Better type 1,2 number pair generation:
#       Higher difference
#       Always different unit digit
#   Better symbols in type 5*:
#       Replaced / with ÷ 
#       Replaced x with × 
#   Banned 5 as a divisor in type4
#   Shows day of week on the top
#   Fixed factors representation
#   Code optimization
#version 2.7.1
#   Critical bug fix
#       used XOR instead of power operator in type 6
#version 2.7.2
#   multiple varibles will generate for type6
#version 2.7.3
#   added ... at end of non-terminating recurring answers in type4


MUL = u'\u00D7'
DIV = u'\u00F7'
SQR = u'\u00B2'

same_denominator_allowed = False# set condition weather same denominator can generate in type5
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

def ind(index, number):         #allows to subscript numbers. x[y] would be ind(y,x)
    return int(str(number)[index])

def right(s,margin=4):             #aligns text to right with given margin position
    s = str(s)
    return(" "*(margin-len(s))+s)

def left(s,margin=4):
    s = str(s)
    return(s+" "*(margin-len(s)))

def hcf(x,y):
    while y:
        x,y = y,x%y
    return(x)

def unequally_distributed_rng():
    return random.choices(range(1000),range(1000,0,-1))[0]

def terminator(num):            #stops repeating of decimals after being repeated twice
    num = str(num)
    last_num = ""
    result = ""
    has_crossed_point = False
    for i in num:
        result += i
        if i == ".":
            has_crossed_point = True
            continue
        if has_crossed_point:
            if i == last_num:
                result += "..."
                break
            else:
                last_num = i
    return result

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
    x = rnd(f,t-30)
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
        print("{x}-{y} = -({y}-{x}) = -{r}".format(x=x,y=y,r=y-x))

def type2():
    for i in common:
        x,y = i
        print("-{x}-{y} = -({x}+{y}) = -{r}".format(x=x,y=y,r=x+y))
    
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

    db = d*b
    da = d*a
    cb = c*b
    ca = c*a
    
    result = x*y
    
    #   ab
    #   cd
    #-----
    #da db
    #ca cb
    #------
    #result

    print(right(x))
    print(right(y))
    print("----")
    if db<10:
        print(right("{}{}".format(da,db)))
    else:
        c = ind(0,db)
        print(right("{}{}".format(da+c,ind(1,db)))," c({})".format(c))
    if cb<10:
        print(right("{}{}0".format(ca,cb)))
    else:
        c = ind(0,cb)
        print(right("{}{}0".format(ca+c,ind(1,cb)))," c({})".format(c))
    print("----")
    print(right(result))

def type4(f1=100,t1=999,f2=3,t2=9):
    x = rnd(f1,t1)
    while x%100==0 or x%10==0:
        x = rnd(f1,t1)
    y = rnd(f2,t2)
    while y==5:
        y = rnd(f2,t2)
    if not x%y == 0:
        r = terminator(x/y)
    else:
        r = int(x/y)
    print(f"{x} / {y} = {r}\nDIY")

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
    
    if z==o:
        rednum=""
        redden=""
        num=x+y
        den=z
        factor=hcf(num,den)
        if factor>1:
            rednum = str(int(num/factor))
            redden = str(int(den/factor))

        print("{a}   {b}   {a} + {b}   {r1}".format(a=x,b=y,r1=right(x+y,2)),right(rednum))
        print("- + - = ----- = --","= --    f={}".format(factor) if factor>1 else "")
        print("{c}   {d}     {c}     {r2}".format(c=z,d=o,r2=right(z,2)),right(redden))

        print("\n")

        rednum=""
        redden=""
        num=x-y
        den=z
        factor=hcf(x-y,z)
        if factor>1:
            rednum = str(int(x-y/factor))
            redden = str(int(z/factor))

        print("{a}   {b}   {a} - {b}   {r1}".format(a=x,b=y,r1=num)+rednum)
        print("- - - = ----- = --")
        print("{c}   {d}     {c}     {r2}".format(c=z,d=o,r2=den)+redden)

    else:
        redden=""
        rednum=""
        num = x*o+y*z
        den = z*o
        factor=hcf(num,den)
        if factor>1:
            rednum=" "+str(int(num/factor))
            redden=" "+str(int(den/factor))

        print("{a}   {b}   {a}x{d}+{c}x{b}   {sr1} + {sr2}   {r1}".format(a=x,b=y,c=z,d=o,sr1=left(x*o,2),sr2=right(y*z,2),r1=num),right(rednum,5))
        print("- + - = ------- = ------- = ---","= --    f={}".format(factor) if factor>1 else "")
        print("{c}   {d}    {c} x {d}       {r2}     {r2}".format(c=z,d=o,r2=left(den,2)),right(redden,5))

        print("\n")

        num = x*o-y*z
        den = z*o
        factor=hcf(num,den)
        if factor>1:        
            rednum=str(int(num/factor))
            redden=str(int(den/factor))

        print("{a}   {b}   {a}x{d}-{c}x{b}   {sr1} - {sr2}   {r1}".format(a=x,b=y,c=z,d=o,sr1=left(x*o,2),sr2=right(y*z,2),r1=x*o-y*z),right(rednum,5))
        print("- - - = ------- = ------- = ---","= --    f={}".format(factor) if factor>1 else "")
        print("{c}   {d}    {c} x {d}       {r2}     {r2}".format(c=z,d=o,r2=left(z*o,2)),right(redden,5))

    print("\n")

    rednum = ""
    redden = ""
    num = x*y
    den = z*o
    factor = hcf(num,den)
    if factor>1:
        rednum = str(int(num/factor))
        redden = str(int(den/factor))

    print("{a}   {b}   {a} x {b}   {r1}   {rn}".format(a=x,b=y,c=z,d=o,r1=x*y,rn=rednum))
    print("- {} - = ----- = -- {}   {}".format(MUL,"= --" if factor>1 else "",("f={}".format(factor)) if factor>1 else ""))
    print("{c}   {d}   {c} x {d}   {r2}   {rd}".format(c=z,d=o,r2=z*o,rd=redden))

    print("\n")

    rednum = ""
    redden = ""
    num = x*o
    den = z*y
    factor = hcf(num,den)
    if factor>1:
        redden = str(int(den/factor))
        rednum = str(int(num/factor))

    print("{a}   {b}   {a} x {d}   {r1}{rn}".format(a=x,b=y,d=o,r1=x*o,rn="   "+rednum))
    print("- {} - = ----- = -- {}   {}".format(DIV,"= --" if factor>1 else "",("f={}".format(factor)) if factor>1 else ""))
    print("{c}   {d}   {c} x {b}   {r2}{rd}".format(c=z,d=o,b=y,r2=z*y,rd="   "+redden))


def type6():
    a = rnd(1,20)
    b = rnd(2,20)
    x = random.choice(variables)
    print(f"({a}{x} + {b}){SQR} = {a**2}{x}{SQR} + {2*a*b}{x} + {b**2}")
    print(f"({a}{x} - {b}){SQR} = {a**2}{x}{SQR} - {2*a*b}{x} + {b**2}")

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

#main()
type4()