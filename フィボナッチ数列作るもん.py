a=""
b=""
c=0
d=0

while True:
    a=input()
    b=input()
    if int(a)<0 or int(b)<0:
        print("整数を入力してください")
    else:
        break

while int(d)<50:
    c=int(a)+int(b)
    print(c)
    a=b
    b=c
    d+=1
