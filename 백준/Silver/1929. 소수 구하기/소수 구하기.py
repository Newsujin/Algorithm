import math

m, n = map(int, input().split())

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if is_prime(i):
        print(i)