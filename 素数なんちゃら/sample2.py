#Miller-Rabin素数判定法

import random

def is_prime(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
