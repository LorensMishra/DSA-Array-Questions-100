def last_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Input
n = int(input())
arr = list(map(int, input().split()))
key = int(input())

print(last_occurrence(arr, key))

"""
Time Complexity:
O(log n)

Space Complexity:
O(1)
"""