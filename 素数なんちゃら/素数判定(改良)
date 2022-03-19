import re
import math
import os
f=""
x=1
while True:
    a=input()
    if re.compile('[a-z]+').fullmatch(a):
        print("\n数を入力してください\n")
    else:
        break
if int(a)<=1:
    f=0
elif a==2 or a==3:
    f=1
elif int(a)%2==0:
    f=0
else:
    b=math.floor(math.sqrt(int(a)))
    while True:
        x+=2
        if int(a)%x==0:
            f=0
            break
        elif x>=b:
            f=1
            break
if f==0:
    print("素数ではない")
elif f==1:
    print("素数")
os.system('PAUSE')
