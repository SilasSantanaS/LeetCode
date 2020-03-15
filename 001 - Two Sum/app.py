'''def main(): SLOWER CODE
    nums = [2, 7, 11, 15]
    target = 9

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]'''


def main():  # FASTER CODE
    nums = [2, 7, 11, 15]

    target = 9
    dictionary = dict()

    for i in range(len(nums)):
        if((target - nums[i]) in dictionary):
            return [dictionary[target - nums[i]], i]
        dictionary[nums[i]] = i


print(main())
