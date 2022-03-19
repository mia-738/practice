import re
import os
b=1

while True:
    a=input()

    if re.compile('[a-z]+').fullmatch(a):

        print("\n数を入力してください\n")

    else:
        break


if int(a)<2:
    print("素数ではない")
elif int(a)==2:
    print("素数")

else:
    while True:
        b+=1
        if int(a)%b==0:
            print("素数ではない")
            break
        elif b==int(a)-1:
            print("素数")
            break

os.system('PAUSE')
