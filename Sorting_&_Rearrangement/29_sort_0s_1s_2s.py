# Question29: Sort an array of 0s, 1s and 2s

"""
Problem:
Sort an array containing only 0s, 1s and 2s.

Time Complexity:
Time complexity is O n.

Space Complexity:
Space complexity is O 1.
"""

def sort_012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr


arr = list(map(int, input("Enter elements: ").split()))
print(sort_012(arr))