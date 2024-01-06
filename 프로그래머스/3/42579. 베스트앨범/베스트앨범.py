def solution(genres, plays):
    dict_song = {}

    # 튜플로 (재생 횟수, 고유 번호) 저장
    for i in range(len(genres)):
        dict_song.setdefault(genres[i], []).append((plays[i], i))
    
    # 누적 재생 횟수와 고유 번호 기준으로 정렬
    for genre in dict_song:
        dict_song[genre] = sorted(dict_song[genre], key=lambda x: (-x[0], x[1]))

    # 누적 재생 횟수를 기준으로 장르를 내림차순으로 정렬
    sorted_genres = sorted(dict_song.keys(), key=lambda x: sum([song[0] for song in dict_song[x]]), reverse=True)
    # sorted_genres = sorted(dict_song.keys(), key=lambda x: sum([song[0] for song in dict_song[x]]), reverse=True)

    answer = []

    # 선택된 장르에 대해 가장 많이 재생된 두 개의 노래 선택
    for genre in sorted_genres:
        answer.extend([song[1] for song in dict_song[genre][:2]])
    return answer