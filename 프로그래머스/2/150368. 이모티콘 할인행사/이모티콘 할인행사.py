from itertools import product

def solution(users, emoticons):
    max_register_user_cnt = 0
    max_sales = 0

    discount_rates = [10, 20, 30, 40]
    for discounts in product(discount_rates, repeat=len(emoticons)):
        cur_user_cnt = 0
        cur_sales = 0

        for min_discount, min_price in users:
            total_cost = 0

            for i, emotion_price in enumerate(emoticons):
                if discounts[i] >= min_discount:
                    total_cost += emotion_price * (100 - discounts[i]) // 100
                
            if total_cost >= min_price:
                cur_user_cnt += 1
            else:
                cur_sales += total_cost
        
        if cur_user_cnt > max_register_user_cnt:
            max_register_user_cnt = cur_user_cnt
            max_sales = cur_sales
        elif cur_user_cnt == max_register_user_cnt:
            max_sales = max(max_sales, cur_sales)

    return [max_register_user_cnt, max_sales]