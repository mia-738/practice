import math
f=""
x=1
def is_prime(a):
    if int(a)<=1:
        return False
    elif a==2 or a==3:
        return True
    elif int(a)%2==0:
        return False
    else:
        b=math.floor(math.sqrt(int(a)))
        while True:
            x+=2
            if int(a)%x==0:
                return False
            elif x>=b:
                return True
