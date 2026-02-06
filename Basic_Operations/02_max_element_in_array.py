# 02_max_element_in_array.py

def max_element(arr):
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = max_element(arr)

# Output
print("Array:", arr)
print("Maximum element in array:", result)

"""
Time Complexity:
O(n) -> Traverses all n elements once.

Space Complexity:
O(1) -> Uses constant extra space (excluding input array).
"""

