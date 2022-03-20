import re
import random
import math
import os

a=""
bina=0
b=""
b1=""
c=65535
c1=65535
d=0
d1=0
e=0
f=0
f1=0

while True:
    a=input()
    if re.compile('[a-z]+').fullmatch(a):

        print("\n数を入力してください\n")

    else:
        if int(a)<0:
          
            print("\n整数を入力してください\n")
        
        else:
            break

b1=10**random.randrange(0,20)+1
b=math.floor(random.random()*b1)

if len(bin(int(b)))<len(bin(int(c))):
    c>>=18-len(bin(b))
else:
    c<<=len(bin(b))-18
    f=1

d=b&c

if f==1:
    d>>=len(bin(b))-18

bina=bin(int(a))

if len(bin(int(a)))<len(bin(int(c1))):
    c1>>=18-len(bina)
else:
    c1<<=len(bina)-18
    f1=1

d1=int(a)&c1

if f1==1:
    d1>>=len(bina)-18

e=d^d1

print(bin(e))
print(e)

os.system('PAUSE')
