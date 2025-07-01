N, B = map(int, input().split())

answer = []
while N > 0:
    remainder = N % B
    N //= B

    if remainder >= 10:
        answer.append(chr(remainder - 10 + ord('A')))
    else:
        answer.append(str(remainder))

print(''.join(reversed(answer)))