cash = int(input())
stock_prices = list(map(int, input().split()))

jh_cash = cash
sm_cash = cash
jh_cnt = 0
sm_cnt = 0
decrease = 0
increase = 0

for idx, price in enumerate(stock_prices):
    if price <= jh_cash:
        jh_cnt += jh_cash // price
        jh_cash = jh_cash % price
    if idx > 0:
        if stock_prices[idx - 1] > stock_prices[idx]: # 하락
            increase = 0
            decrease += 1
            if decrease >= 3 and price < sm_cash: # 3일 연속 하락
                sm_cnt += sm_cash // price
                sm_cash = sm_cash % price
        elif stock_prices[idx - 1] < stock_prices[idx]: # 상승
            decrease = 0
            increase += 1
            if increase >= 3 and sm_cnt != 0: # 3일 연속 상승
                sm_cash += sm_cnt * price
                sm_cnt = 0

last_price = stock_prices[len(stock_prices) - 1]
if (last_price * jh_cnt + jh_cash > last_price * sm_cnt + sm_cash):
    print("BNP")
elif (last_price * jh_cnt + jh_cash < last_price * sm_cnt + sm_cash):
    print("TIMING")
else:
    print("SAMESAME")