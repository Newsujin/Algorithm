import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    stock_prices = list(map(int, sys.stdin.readline().split()))
    profit = 0
    max_price = 0
    for i in range(N - 1, -1, -1):
        if stock_prices[i] > max_price:
            max_price = stock_prices[i]
        else:
            profit += max_price - stock_prices[i]
    print(profit)