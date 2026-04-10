def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# User Input
n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key: "))

print(linear_search(arr, key))

"""
Time Complexity:
O(n) -> Iterates through n elements once.

Space Complexity:
O(1) -> Uses constant extra space (excluding input array).
"""