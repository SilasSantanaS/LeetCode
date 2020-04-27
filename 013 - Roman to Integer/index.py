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


def romanToInt(s):
    numbersDictionary = {"I": 1, "V": 5, "X": 10,
                         "L": 50, "C": 100, "D": 500, "M": 1000, "Z": 0}

    if len(s) > 2:
        return romanToInt(s[:len(s) / 2]) + romanToInt(s[len(s) / 2:])
    if len(s) == 1:
        s += "Z"

    if numbersDictionary.get(s[0]) >= numbersDictionary.get(s[1]):
        return numbersDictionary.get(s[0]) + numbersDictionary.get(s[1])
    return numbersDictionary.get(s[1]) - numbersDictionary.get(s[0])


print(romanToInt("MCDLXXVI"))


# print(name[:len(name) / 2])
# print(name[len(name) / 2:])
