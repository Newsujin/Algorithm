cash = int(input())
stock_prices = list(map(int, input().split()))

jh_cash = sm_cash = cash
jh_cnt = sm_cnt = up = down = 0

for idx, price in enumerate(stock_prices):
    # 준현
    jh_cnt += jh_cash // price
    jh_cash = jh_cash % price
    
    # 성민
    if idx > 0:
        today, yesterday = stock_prices[idx], stock_prices[idx - 1]
        if yesterday > today: # 하락
            up = 0
            down += 1
        elif yesterday < today: # 상승
            down = 0
            up += 1
        if down >= 3: # 3일 연속 하락
            sm_cnt += sm_cash // price
            sm_cash = sm_cash % price
        if up >= 3 and sm_cnt > 0: # 3일 연속 상승
            sm_cash += sm_cnt * price
            sm_cnt = 0

last_price = stock_prices[-1]
jh_total = last_price * jh_cnt + jh_cash
sm_total = last_price * sm_cnt + sm_cash

if (jh_total > sm_total):
    print("BNP")
elif (jh_total < sm_total):
    print("TIMING")
else:
    print("SAMESAME")