# 05_reverse_array_inplace.py

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function Call
reverse_array(arr)

# Output
print("Reversed array:", arr)

"""
Time Complexity:
O(n) -> Each element is swapped once.

Space Complexity:
O(1) -> Reversal done in-place, no extra space used.
"""
