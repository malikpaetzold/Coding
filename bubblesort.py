# Implementation of the BubbleSort Algorithm

def bubbleSort(array):
    # O(n^2) time | O(1) space
    action_needed = True
    end_complete = 1
    
    while action_needed:
        action_needed = False
        
        for i in range(len(array) - end_complete):
            if array[i+1] < array[i]:
                array[i+1], array[i] = array[i], array[i+1]
                
                action_needed = True
        end_complete += 1
    
    return array

if __name__ == "__main__":
    print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))