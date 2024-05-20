def solution(elements):
    arr_len = len(elements)
    elements *= 2

    arr_set = set()
    for length in range(1, arr_len + 1):
        for start in range(arr_len):
            arr_sum = sum(elements[start:start + length])
            arr_set.add(arr_sum)

    return len(arr_set)