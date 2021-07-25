"""
Problem Statement
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [1, 2, 9]
output = [1, 3, 0]
Example 3:

input = [9, 9, 9]
output = [1, 0, 0, 0]

"""

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    out = []
    l = len(arr)
    remember = 0
    for i in range(l):
        curr_num = arr[l-i-1]
        new_num = curr_num + remember
        if i == 0: new_num += 1
        remember = 0
        if new_num >= 10:
            remember = 1
            new_num -= 10
        out.insert(0, new_num)
    if remember == 1: out.insert(0, 1)
    return out

# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail   ---   Correct: ", solution, " Returned: ", output )
            return
    print("Pass")

# Test Case 1
arr = [0]
solution = [1]

test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)