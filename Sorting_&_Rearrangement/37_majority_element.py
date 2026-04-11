# Question37: Majority element

"""
Time Complexity: O n
Space Complexity: O 1
"""

def majority(arr):
    count = 0
    candidate = None
    
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate


arr = list(map(int, input().split()))
print(majority(arr))