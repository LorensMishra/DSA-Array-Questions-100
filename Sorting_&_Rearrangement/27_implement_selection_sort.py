# Question27: Implement Selection Sort algorithm

"""
Problem:
Given an array, sort it using Selection Sort.

Time Complexity:
Worst case time complexity is O n square.
Average case time complexity is O n square.
Best case time complexity is O n square.

Space Complexity:
Space complexity is O 1 because sorting is done in place.
"""

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


arr = list(map(int, input("Enter elements: ").split()))
print("Sorted array:", selection_sort(arr))