'''def romanToInt():  # O(n) solution
    numbersDictionary = {"I": 1, "V": 5, "X": 10,
                         "L": 50, "C": 100, "D": 500, "M": 1000}

    s = "MCMXCIV"
    i = len(s) - 1
    answer = 0

    while i > 0:
        if numbersDictionary.get(s[i]) <= numbersDictionary.get(s[i - 1]):
            answer += numbersDictionary.get(
                s[i]) + numbersDictionary.get(s[i - 1])
        else:
            answer -= numbersDictionary.get(s[i - 1]) - \
                numbersDictionary.get(s[i])
        i -= 2

    if i == 0:
        answer += numbersDictionary.get(s[i])
    return answer'''


def convertRoman(half, numbersDictionary):
    print("half: {}".format(half))

    if len(half) <= 2:  # base case
        if len(half) == 2:
            if numbersDictionary.get(half[len(half) - 1]) <= numbersDictionary.get(half[len(half) - 2]):
                return numbersDictionary.get(half[len(half) - 1]) + numbersDictionary.get(half[len(half) - 2])
            else:
                return numbersDictionary.get(half[len(half) - 2]) - numbersDictionary.get(half[len(half) - 1])
        else:
            print("kkkk: {}".format(numbersDictionary.get(half)))
            return 0
    else:
        return convertRoman(half[:len(half) / 2], numbersDictionary) + convertRoman(half[len(half) / 2:], numbersDictionary)


def romanToInt():
    numbersDictionary = {"I": 1, "V": 5, "X": 10,
                         "L": 50, "C": 100, "D": 500, "M": 1000}

    s = "X"
    answer = 0

    return answer + convertRoman(s[:len(s) / 2], numbersDictionary) + convertRoman(s[len(s) / 2:], numbersDictionary)


# print(romanToInt())

name = "silas"

# print(name[:len(name) / 2])
# print(name[len(name) / 2:])
print("answer: {}".format(romanToInt()))
