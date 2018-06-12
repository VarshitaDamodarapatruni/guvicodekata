def factorial(n11):
    if n11 == 0:
        return 1
    else:
        return n11 * factorial(n11-1)
n11=int(input())
print(factorial(n11))
