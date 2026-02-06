# 11_remove_duplicates_array.py

def remove_duplicates(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = remove_duplicates(arr)

# Output
print("Original array:", arr)
print("Array after removing duplicates:", result)

"""
Time Complexity:
O(n^2) -> 'not in' check takes O(n) inside loop.

Space Complexity:
O(n) -> Extra space used for unique elements.
"""
# 11_remove_duplicates_array.py

def remove_duplicates(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
result = remove_duplicates(arr)

# Output
print("Original array:", arr)
print("Array after removing duplicates:", result)

"""
Time Complexity:
O(n^2) -> 'not in' check takes O(n) inside loop.

Space Complexity:
O(n) -> Extra space used for unique elements.
"""
