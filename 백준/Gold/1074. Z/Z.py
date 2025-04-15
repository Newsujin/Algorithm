n, r, c = map(int, input().split())

def find_order(n, r, c):
    if n == 0:
        return 0
    
    half_size = 2**(n - 1)
    
    quadrant = 0
    if r < half_size and c >= half_size:
        quadrant = 1
        c -= half_size
    elif r >= half_size and c < half_size:
        quadrant = 2
        r -= half_size
    elif r >= half_size and c >= half_size:
        quadrant = 3
        r -= half_size
        c -= half_size
    
    return quadrant * half_size * half_size + find_order(n - 1, r, c)


print(find_order(n, r, c))