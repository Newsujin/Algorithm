expression = input()

split_by_minus = expression.split('-')

result = sum(int(x) for x in split_by_minus[0].split('+'))

for part in split_by_minus[1:]:
    result -= sum(int(x) for x in part.split('+'))

print(result)