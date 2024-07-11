def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''
        
        checked_number = False
        for i in range(len(f)):
            if f[i].isdigit():
                number += f[i]
                checked_number = True
            elif not checked_number:
                head += f[i]
            else:
                tail = f[i:]
                break
        answer.append((head, number, tail))
    
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(string) for string in answer]
