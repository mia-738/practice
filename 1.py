import re
import random
import math
import os

f=0

while f<3
    a=""
    a1=""
    b=""
    c=""
    d=""


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

    b=int(random.randrange(0,65535))

    c=(a^b)//256
    if c%x==0:
        print("You Won!!!")
        f+=1
        break
    else:
        print("You Lose!!!")
        break

os.system('PAUSE')
