# 01_sum_of_array_elements.py

def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = sum_of_array(arr)

# Output
print("Array:", arr)
print("Sum of array elements:", result)

"""
Time Complexity:
O(n) -> Iterates through n elements once.

Space Complexity:
O(1) -> Uses constant extra space (excluding input array).
"""
