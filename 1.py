import random
import math
import os

a=""
bina=0
b=""
c=65535
c1=65535
d=0
d1=0
e=0
f=0

while True:
    a=input()
    if str.isdigit(a):

        if int(a)<0:
            print("\n整数を入力してください\n")
        
        else:
            break

    else:
        print("\n数を入力してください\n")

b=math.floor(random.random()*1000000001)
c<<=len(bin(b))-18
d=b&c


bina=bin(int(a))

if len(bin(int(a)))<len(bin(int(c1))):
    c1>>=18-len(bina)
else:
    c1<<=len(bina)-18
    f=1

d1=int(a)&c1

d>>=len(bin(b))-18

if f==1:
    d1>>=len(bina)-18

e=d^d1

print(bin(e))
print(e)

os.system('PAUSE')
