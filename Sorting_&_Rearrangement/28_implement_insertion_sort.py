# Question28: Implement Insertion Sort algorithm

"""
Problem:
Sort an array using Insertion Sort.

Time Complexity:
Worst case time complexity is O n square.
Average case time complexity is O n square.
Best case time complexity is O n when already sorted.

Space Complexity:
Space complexity is O 1.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


arr = list(map(int, input("Enter elements: ").split()))
print("Sorted array:", insertion_sort(arr))