import re
import random
import math
import os

b=int(random.randrange(0,65535))
f=0
x=3

while f<3
    a=""
    a1=""
    c=""

    while True:
        a1=input()
        if re.compile('[a-z]+').fullmatch(a1):

            print("\n数を入力してください\n")

        else:
            if int(a1)<0:
          
                print("\n整数を入力してください\n")
        
            else:
                a=int(a1)
                break

    c=(a^b)//256
    if c%x==0:
        print("You Won!!!")
        f+=1
        break
    else:
        print("You Lose!!!")
        break
    b=(47265*b)%(2**16)
os.system('PAUSE')
