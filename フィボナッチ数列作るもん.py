c=0
d=0

def Fibonacci(a,b,n):
    while d<n:
        c=a+b
        print(c)
        a=b
        b=c
        d+=1

    print("")
