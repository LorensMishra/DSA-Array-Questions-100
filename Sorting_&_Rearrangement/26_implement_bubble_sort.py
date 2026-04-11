# Question26: Implement Bubble Sort algorithm

"""
Problem:
Given an array, sort it using Bubble Sort.

Time Complexity:
Worst case time complexity is O n square when the array is in reverse order.
Average case time complexity is O n square.
Best case time complexity is O n when the array is already sorted.

Space Complexity:
Space complexity is O 1 because sorting is done in place without using extra memory.
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Runtime Input
arr = list(map(int, input("Enter elements separated by space: ").split()))

result = bubble_sort(arr)
print("Sorted array:", result)