# Question34: Find kth smallest element
"""
Time Complexity: O n log n
Space Complexity: O 1
"""

def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


arr = list(map(int, input().split()))
k = int(input())
print(kth_smallest(arr, k))