# Return the first Integer that appeats more than once in the array

def firstDuplicateValue(array):
    nums = {}
    for i in array:
        if i in nums: return i
        else: nums[i] = True
    return -1

if __name__ == "__main__":
    print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))