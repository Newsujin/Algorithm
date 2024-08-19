def compress_str(s, unit):
    compressed = ""
    prev = s[:unit]
    cnt = 1

    for i in range(unit, len(s), unit):
        current = s[i:i + unit]
        if current == prev:
            cnt += 1
        else:
            if cnt > 1:
                compressed += str(cnt) + prev
            else:
                compressed += prev
            prev = current
            cnt = 1

    if cnt > 1:
        compressed += str(cnt) + prev
    else:
        compressed += prev
    
    return compressed


def solution(s):
    min_len = len(s)
    if min_len == 1:
        return 1
    for unit in range(1, min_len // 2 + 1):
        compressed = compress_str(s, unit)
        min_len = min(min_len, len(compressed))
    return min_len
