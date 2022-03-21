l = [0]
for x in l:
    print(x, '\r', end = "")

    i = 1
    t = 0
    if int(x) < 1:
        t += x
    while i * i <= int(x):
        if int(x) % i == 0:
            t += i
            if i * i != x:
                s = round(int(x) / i)
                if i != s:
                    t += s
        i = i + 1

    if t-x == x:
        print()
        
    l.append(x+1)
