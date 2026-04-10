def count_occurrences(arr, key):
    return arr.count(key)

# Input
n = int(input())
arr = list(map(int, input().split()))
key = int(input())

print(count_occurrences(arr, key))

"""
Time Complexity:
O(n) -> Traverses full array.

Space Complexity:
O(1)
"""