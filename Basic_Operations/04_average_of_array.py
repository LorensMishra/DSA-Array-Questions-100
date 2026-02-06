# 04_average_of_array.py

def average_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = average_of_array(arr)

# Output
print("Array:", arr)
print("Average of array elements:", result)

"""
Time Complexity:
O(n) -> Iterates through all n elements once.

Space Complexity:
O(1) -> Uses constant extra space (excluding input array).
"""
