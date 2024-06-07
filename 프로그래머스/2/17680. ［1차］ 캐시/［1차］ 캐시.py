from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    cities_lower = [city.lower() for city in cities]

    for city in cities_lower:
        if cacheSize == 0:
            answer = 5 * len(cities_lower)
            break
        elif city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5

    return(answer)