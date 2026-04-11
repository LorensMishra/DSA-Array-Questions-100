# Question39: Union of two sorted arrays

"""
Time Complexity: O n
Space Complexity: O n
"""

def union(arr1, arr2):
    return list(set(arr1 + arr2))


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(union(arr1, arr2))