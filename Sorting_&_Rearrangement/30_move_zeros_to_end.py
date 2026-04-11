# Question30: Move all zeros to the end

"""
Time Complexity:
Time complexity is O n.

Space Complexity:
Space complexity is O 1.
"""

def move_zeros_end(arr):
    j = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr


arr = list(map(int, input("Enter elements: ").split()))
print(move_zeros_end(arr))