# Fizzbuzz implementation in Python

for x in range(1,101):
    if (x%3==0):print('fizz', end='')
    if (x%5==0):print('buzz', end='')
    if not (x%3==0 or x%5==0):print(x, end='')
    print()
