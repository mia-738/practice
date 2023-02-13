def p_number(num):

    while True:

        l = [1]
        f = []
        for x in l:

            i = 1
            t = 0
            if x < 1:
                 t += x
            while i * i <= x:
                if x % i == 0:
                     t += i
                     if i * i != x:
                         s = x // i
                         if i != s:
                             t += s
                i = i + 1

            if t-x == x:
                f.append(x)
                if len(f) == num:
                    return f
        
            l.append(x+1)
