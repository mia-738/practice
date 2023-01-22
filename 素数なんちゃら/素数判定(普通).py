b=1

def prime(a):
    if int(a)<2:
        return False
    elif int(a)==2:
        return True

    else:
        while True:
            b+=1
            if int(a)%b==0:
                return False
            elif b==int(a)-1:
                return True
