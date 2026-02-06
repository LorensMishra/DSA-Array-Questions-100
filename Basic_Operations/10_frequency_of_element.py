# 10_frequency_of_element.py

def frequency_of_element(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter element to find frequency: "))

# Function Call
result = frequency_of_element(arr, target)

# Output
print("Array:", arr)
print(f"Frequency of {target}:", result)

"""
Time Complexity:
O(n) -> Traverses all elements once.

Space Complexity:
O(1) -> Uses constant extra space.
"""
