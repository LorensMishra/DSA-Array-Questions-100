"""
Time Complexity: O n square
Space Complexity: O 1
"""

def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


arr = list(map(int, input().split()))
print(count_inversions(arr))