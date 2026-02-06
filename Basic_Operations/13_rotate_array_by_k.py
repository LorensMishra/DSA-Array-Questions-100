# 13_rotate_array_by_k.py

def rotate_by_k(arr, k):
    n = len(arr)
    k = k % n  # Handle k > n

    arr[:] = arr[-k:] + arr[:-k]
    return arr


# Runtime Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by space: ").split()))
k = int(input("Enter value of k (rotation count): "))

# Function Call
rotate_by_k(arr, k)

# Output
print("Array after rotating by", k, "positions:", arr)

"""
Time Complexity:
O(n) -> Each element is moved once.

Space Complexity:
O(n) -> Uses extra space for slicing.
"""
