# 12_rotate_array_by_one.py

def rotate_by_one(arr):
    last = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    return arr


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
rotate_by_one(arr)

# Output
print("Array after rotating by one position:", arr)

"""
Time Complexity:
O(n) -> Shifts each element once.

Space Complexity:
O(1) -> Rotation done in-place.
"""
