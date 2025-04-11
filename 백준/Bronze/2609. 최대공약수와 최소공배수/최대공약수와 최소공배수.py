n, m = map(int, input().split())

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
print(gcd(n,m))

def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result
print(lcm(n, m))