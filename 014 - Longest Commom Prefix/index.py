def minAndMax(str1, str2):
    if len(str1) < len(str2):
        return str1, str2
    else:
        return str2, str1


def longestCommonPrefix(strs):
    parcial = ""
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    shorter, longer = minAndMax(strs[0], strs[1])

    for i in range(len(shorter)):
        if shorter[i] != longer[i]:
            break
        parcial += shorter[i]

    if len(strs) > 2:
        for i in range(2, len(strs)):
            shorter, longer = minAndMax(parcial, strs[i])
            if len(shorter) == 0:
                return ""
            for j in range(len(shorter)):
                if shorter[j] != longer[j]:
                    parcial = shorter[:j]
                    break

    return parcial


#print(longestCommonPrefix(["flower", "flow", "flight"]))

print(longestCommonPrefix(["ac", "ac", "a", "a"]))
