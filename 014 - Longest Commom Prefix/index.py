def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        counter = 0
        for j in range(len(strs[i])):
            if prefix[: j + 1] != strs[i][:j + 1]:
                counter += 1
                prefix = strs[i][:j]
                break
        if counter == 0:
            prefix = strs[i]

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
