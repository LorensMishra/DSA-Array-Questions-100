# 15_check_element_exists.py

def element_exists(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter element to search: "))

# Function Call
result = element_exists(arr, target)

# Output
print("Array:", arr)
print(f"Does {target} exist in array?:", result)

"""
Time Complexity:
O(n) -> Linear search through array elements.

Space Complexity:
O(1) -> Constant extra space.
"""
