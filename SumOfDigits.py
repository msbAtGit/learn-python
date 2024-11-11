def sumOfDigits(n):
    num = int(n)
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = int(num / 10)
    return sum

print(sumOfDigits(897))