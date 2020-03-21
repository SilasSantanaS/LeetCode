def isPalindrome():
    x = int(input())
    original = x

    if x < 0:
        return False
    backwards = []
    while x / 10 != 0:
        backwards.append(x % 10)
        x = x / 10
    backwards.append(x)

    backward_number = 0
    for i in range(0, len(backwards)):
        backward_number += backwards[i] * pow(10, len(backwards) - (i + 1))

    if(original == backward_number):
        return True
    return False


print(isPalindrome())
