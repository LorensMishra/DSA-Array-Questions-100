# 08_second_largest_element.py

def second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = second_largest(arr)

# Output
print("Array:", arr)
print("Second largest element:", result)

"""
Time Complexity:
O(n) -> Single traversal of the array.

Space Complexity:
O(1) -> Uses constant extra space.
"""
