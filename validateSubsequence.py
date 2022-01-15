# Validate Subsequenze

def isValidSubsequence(array, sequence):
    # Write your code here.
    if len(array) < len(sequence): return False
    if array == sequence: return True
    
    pointer = 0
    for n in array:
        if n == sequence[pointer]:
            pointer += 1
            if pointer == len(sequence): return True
    
    return False
    

if __name__ == "__main__":
    print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))