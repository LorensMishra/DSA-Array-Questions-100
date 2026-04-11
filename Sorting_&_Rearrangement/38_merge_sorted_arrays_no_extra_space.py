# Question38: Merge two sorted arrays

"""
Time Complexity: O n log n
Space Complexity: O 1
"""

def merge_arrays(a, b):
    a.extend(b)
    a.sort()
    return a


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(merge_arrays(a, b))