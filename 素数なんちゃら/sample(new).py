import math

def is_prime(a,x=1):
    
    if a<=1:
        return False
    elif a==2 or a==3:
        return True
    elif a%2==0:
        return False
    else:
        b=math.floor(math.sqrt(a))
        while True:
            x+=2
            if a%x==0:
                return False
            elif x>=b:
                return True
