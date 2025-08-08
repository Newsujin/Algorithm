T = int(input())

for _ in range(T):
    n = int(input())
    closet = dict()
    
    for i in range(n):
        clothes, category = input().split()
        if category not in closet:
            closet[category] = [clothes]
        else:
            closet[category].append(clothes)

    result = 1
    for value in closet.values():
        result *= (len(value) + 1)
    print(result - 1)