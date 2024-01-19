def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    answer = ""
    while numbers:
        answer = str(numbers.pop()) + answer
    return answer