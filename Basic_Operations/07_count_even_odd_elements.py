# 07_count_even_odd_elements.py

def count_even_odd(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
even, odd = count_even_odd(arr)

# Output
print("Array:", arr)
print("Even elements count:", even)
print("Odd elements count:", odd)

"""
Time Complexity:
O(n) -> Iterates through all elements once.

Space Complexity:
O(1) -> Uses constant extra space.
"""
