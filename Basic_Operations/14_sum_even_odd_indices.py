# 14_sum_even_odd_indices.py

def sum_even_odd_indices(arr):
    even_sum = 0
    odd_sum = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]

    return even_sum, odd_sum


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
even_sum, odd_sum = sum_even_odd_indices(arr)

# Output
print("Sum of elements at even indices:", even_sum)
print("Sum of elements at odd indices:", odd_sum)

"""
Time Complexity:
O(n) -> Single traversal of the array

Space Complexity:
O(1) -> Constant extra space
"""
