def pair_sum(arr, target):
    seen = set()

    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)

    return False

# Input
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

print(pair_sum(arr, target))

"""
Time Complexity:
O(n) -> Single pass with hashing.

Space Complexity:
O(n) -> Extra space for set.
"""