def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            tmp = '0' + bin(n)[2:]
            zero_idx = tmp.rfind('0')
            tmp = list(tmp)

            tmp[zero_idx] = '1'
            tmp[zero_idx + 1] = '0'
            tmp_str = ''.join(tmp)

            answer.append(int(tmp_str, 2))

    return answer