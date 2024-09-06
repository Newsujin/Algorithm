def solution(places):
    result = []

    for place in places:
        loc = []
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    loc.append((row, col))
        
        keep_distance = True

        for i in range(len(loc)):
            for j in range(i + 1, len(loc)):
                r1, c1 = loc[i]
                r2, c2 = loc[j]
                manhattan = abs(r1 - r2) + abs(c1 - c2)

                if manhattan == 1:
                    keep_distance = False
                    break
                elif manhattan == 2:
                    if r1 == r2 and place[r1][(c1 + c2) // 2] != 'X':
                        keep_distance = False
                        break
                    elif c1 == c2 and place[(r1 + r2) // 2][c1] != 'X':
                        keep_distance = False
                        break
                    elif r1 != r2 and c1 != c2:
                        if place[r1][c2] != 'X' or place[r2][c1] != 'X':
                            keep_distance = False
                            break

        if keep_distance:
            result.append(1)
        else:
            result.append(0)
    
    return result