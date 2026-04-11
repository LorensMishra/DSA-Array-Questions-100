"""
Time Complexity: O n
Space Complexity: O 1
"""

def sum_of_subarrays(arr):
    n = len(arr)
    total_sum = 0
    
    for i in range(n):
        total_sum += arr[i] * (i + 1) * (n - i)
    
    return total_sum


arr = list(map(int, input().split()))
print(sum_of_subarrays(arr))