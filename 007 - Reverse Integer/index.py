def main():
    dividers = []
    x = 1534236469

    isNegative = False
    if x < 0:
        isNegative = True
        x = abs(x)

    while x / 10 != 0:
        dividers.append(x % 10)
        x /= 10
    dividers.append(x % 10)

    result = 0
    for i in range(len(dividers)):
        result += dividers[i] * pow(10, len(dividers) - (i + 1))

    if isNegative:
        result *= -1
        if result < pow(-2, 31):
            return 0
        return result

    if result > pow(2, 31) - 1:
        return 0
    return result


print(main())
