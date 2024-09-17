def fact_num(a):
    fact = 1
    i = 1
    while i <= a:
        fact = fact * i
        i = i + 1
    return fact


factorial = fact_num(6)

print(factorial)
