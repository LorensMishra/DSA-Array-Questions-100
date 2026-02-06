# 06_check_array_sorted.py

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = is_sorted(arr)

# Output
print("Array:", arr)
print("Is array sorted in ascending order?:", result)

"""
Time Complexity:
O(n) -> Checks adjacent elements once.

Space Complexity:
O(1) -> Uses constant extra space.
"""
