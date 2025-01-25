def convert_base_to_decimal(number: str, base: int) -> int:
    """
    B진법 수를 10진법으로 변환하는 함수.

    Args:
        number (str): B진법으로 표현된 숫자.
        base (int): B진법의 밑수 (2 ≤ base ≤ 36).

    Returns:
        int: 변환된 10진법 숫자.
    """
    decimal_value = 0
    power = 0

    # 역순으로 숫자를 처리 (진법 변환)
    for digit in reversed(number):
        if digit.isdigit():  # 숫자인 경우
            value = int(digit)
        else:  # 문자인 경우 (A~Z)
            value = ord(digit) - ord('A') + 10

        # 각 자리 값에 밑수의 거듭제곱을 곱해 합산
        decimal_value += value * (base ** power)
        power += 1

    return decimal_value

# 입력 처리
if __name__ == "__main__":
    N, B = input().split()
    B = int(B)  # 진법을 정수로 변환
    result = convert_base_to_decimal(N, B)
    print(result)