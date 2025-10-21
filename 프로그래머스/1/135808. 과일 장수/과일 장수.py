def solution(k, m, score):
    answer = 0                  				# 최대 이익 값 (결과 값)
    start, end = 0, m           				# 사과의 수 시작, 끝
    score.sort(reverse=True)    				# 사과 점수 기준, 내림차순 정렬
    
    while( len(score[start:end]) == m ):        # 사과의 수가 만족할 때 loop
        answer += ( min(score[start:end]) * m ) # 최저점수 * 사과의 수, 누적
        start += m                              # 시작 + 사과의 수
        end += m                                # 끝 + 사과의 수

    return answer