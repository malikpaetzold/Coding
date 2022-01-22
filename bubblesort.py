# Implementation of the BubbleSort Algorithm

def bubbleSort(array):
    if len(array) < 2: return array
    action_needed = True
    
    while action_needed:
        action_needed = False
        
        for i in range(1, len(array), 1):
            if array[i-1] > array[i]:
                temp = array[i]
                array[i] = array[i-1]
                array[i-1] = temp
                
                action_needed = True
    
    return array

if __name__ == "__main__":
    print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))