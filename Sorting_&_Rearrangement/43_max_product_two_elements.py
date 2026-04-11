"""
Time Complexity: O n log n
Space Complexity: O 1
"""

def max_product(arr):
    arr.sort()
    return arr[-1] * arr[-2]


arr = list(map(int, input().split()))
print(max_product(arr))