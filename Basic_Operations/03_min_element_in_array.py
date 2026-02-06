# 03_min_element_in_array.py

def min_element(arr):
    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = min_element(arr)

# Output
print("Array:", arr)
print("Minimum element in array:", result)

"""
Time Complexity:
O(n) -> Traverses all n elements once.

Space Complexity:
O(1) -> Uses constant extra space (excluding input array).
"""
