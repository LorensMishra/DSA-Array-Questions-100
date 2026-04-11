# Question33: Find kth largest element

"""
Time Complexity: O n log n
Space Complexity: O 1
"""

def kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k - 1]


arr = list(map(int, input().split()))
k = int(input())
print(kth_largest(arr, k))