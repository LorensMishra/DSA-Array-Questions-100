# Question35: Rearrange array so that arr[i] = i

"""
Time Complexity: O n
Space Complexity: O 1
"""

def rearrange(arr):
    i = 0
    n = len(arr)
    while i < n:
        if 0 <= arr[i] < n and arr[i] != i:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1
    return arr


arr = list(map(int, input().split()))
print(rearrange(arr))