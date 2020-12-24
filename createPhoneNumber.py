# Input: List of Integer between 0 and 9
# Output: Correctly formatted Phone Number (String)

def createPhoneNumber(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))