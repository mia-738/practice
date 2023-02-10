def Fibonacci(n):
    a=1
    b=c=d=0
    print(a)
    
    while d<n-1:
        c=a+b
        print(c)
        a=b=c
        d+=1
