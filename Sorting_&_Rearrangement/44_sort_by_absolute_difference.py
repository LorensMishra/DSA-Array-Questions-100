"""
Time Complexity: O n log n
Space Complexity: O 1
"""

def sort_by_diff(arr, x):
    return sorted(arr, key=lambda num: abs(num - x))


arr = list(map(int, input().split()))
x = int(input())
print(sort_by_diff(arr, x))