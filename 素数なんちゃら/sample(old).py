def prime(a,b=1):

    if a<2:
        return False
    elif a==2:
        return True

    else:
        while True:
            b+=1
            if a%b==0:
                return False
            elif b==a-1:
                return True
