# https://www.algoexpert.io/questions/Two%20Number%20Sum
# Solution 1
def twoNumberSum(array, targetSum):
    # Write your code here.
    result = []
    for i, item1 in enumerate(array):
        for j, item2 in enumerate(array[i + 1:]):
            if item1 + item2 == targetSum:
                result.append(item1)
                result.append(item2)
    return result


# Solution 2
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        potential = targetSum - num
    if potential in nums:
        return [potential, num]
    else:
        nums[num] = True
    return []


# Solution 3
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] < targetSum:
            left += 1
        elif array[left] + array[right] > targetSum:
            right -= 1
        return []
