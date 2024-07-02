from collections import defaultdict
from math import ceil

def str2min(time):
    hour_, min_ = time.split(':')
    return int(hour_) * 60 + int(min_)

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    assets = defaultdict(int)
    accumulate = defaultdict(int)
    fees = defaultdict(int)
    answers = []
    for record in records:
        times, car_number, types = record.split()
        times = str2min(times)
        if types == 'IN':
            assets[car_number] = times
        
        elif types == 'OUT':
            accumulate[car_number] += times - assets[car_number]
            del assets[car_number]
        
    for car_number, elapsed_time in assets.items():
        elapsed_time = str2min('23:59') - elapsed_time
        accumulate[car_number] += elapsed_time
    
    for car_number, elapsed_time in sorted(accumulate.items(), key = lambda x: x[0]):
        fee = default_fee + max(0, ceil((elapsed_time - default_time)/unit_time) * unit_fee)
        answers.append(fee) 
    
    return answers