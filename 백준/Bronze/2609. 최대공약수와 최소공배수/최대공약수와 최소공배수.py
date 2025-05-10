x, y = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y, gcd):
    return x * y // gcd

gcd = gcd(x, y)
print(gcd)
print(lcm(max(x, y), min(x, y), gcd))