def min_index(arr):
    min_idx = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    return min_idx

# Input
n = int(input())
arr = list(map(int, input().split()))

print(min_index(arr))

"""
Time Complexity:
O(n)

Space Complexity:
O(1)
"""