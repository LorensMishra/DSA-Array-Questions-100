"""
Time Complexity: O n log n
Space Complexity: O n
"""

def median(arr1, arr2):
    arr = sorted(arr1 + arr2)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    return arr[n//2]


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(median(arr1, arr2))