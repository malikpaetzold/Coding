# given a string, return the longest palindromic substring
#
# input = "abaxyxa"
# output = "axyxa"
#
# input string will have a length of > 0

def longestPalindromicSubstring(string):
    outputIndex = [0, 0] # start & end index of the palindromic substring
    for i in range(1, len(string)):
        even = findPalindrom(string, i-1, i)
        odd = findPalindrom(string, i, i)
        subout = max(even, odd, key=lambda x: x[1] - x[0]) # the key is the difference between the the two values
        outputIndex = max(subout, outputIndex, key=lambda x: x[1] - x[0]) # max() returns the array with the biggest difference between values
    
    return string[outputIndex[0] : outputIndex[1] + 1] # slicing excludes the last index, therefore +1

def findPalindrom(string, index1, index2=None):
    if string[index1] != string[index2]: return [index1, index1]
    while index1 >= 0 and index2 < len(string):
        if string[index1] != string[index2]: return [index1+1, index2-1]
        index1 -= 1
        index2 += 1
    
    return [index1+1, index2-1]

print(longestPalindromicSubstring("habcbaca"))