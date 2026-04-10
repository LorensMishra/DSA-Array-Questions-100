def max_index(arr):
    max_idx = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i

    return max_idx

# Input
n = int(input())
arr = list(map(int, input().split()))

print(max_index(arr))

"""
Time Complexity:
O(n)

Space Complexity:
O(1)
"""