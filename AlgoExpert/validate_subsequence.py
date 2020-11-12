# https://www.algoexpert.io/questions/Validate%20Subsequence
# solution 1
def isValidSubsequence(array, sequence):
    # Write your code here.
    for item in sequence:
        if item not in array:
            return False
        array = array[array.index(item) + 1:]

    return True


# Solution 2
def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            return True
        elif sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)