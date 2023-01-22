c=0
d=0

def Fibonacci(a,b):
    while True:
        if int(a)<0 or int(b)<0:
            print("\n\"整数を\"入力してください\n")
        else:
            break

    while int(d)<50:
        c=int(a)+int(b)
        print(c)
        a=b
        b=c
        d+=1

    print("")
