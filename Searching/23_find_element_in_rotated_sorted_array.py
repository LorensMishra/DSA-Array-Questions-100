def search_rotated(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Input
n = int(input())
arr = list(map(int, input().split()))
key = int(input())

print(search_rotated(arr, key))

"""
Time Complexity:
O(log n)

Space Complexity:
O(1)
"""