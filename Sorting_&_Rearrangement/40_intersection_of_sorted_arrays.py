# Question40: Intersection of arrays

"""
Time Complexity: O n
Space Complexity: O n
"""

def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(intersection(arr1, arr2))