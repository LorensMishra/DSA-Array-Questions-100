# Question32: Sort array in descending order

"""
Time Complexity: O n log n
Space Complexity: O 1
"""

def sort_desc(arr):
    return sorted(arr, reverse=True)


arr = list(map(int, input().split()))
print(sort_desc(arr))