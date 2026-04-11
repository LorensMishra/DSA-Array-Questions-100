"""
Time Complexity: O n log n
Space Complexity: O n
"""

def min_swaps(arr):
    n = len(arr)
    arrpos = list(enumerate(arr))
    arrpos.sort(key=lambda x: x[1])
    
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or arrpos[i][0] == i:
            continue
        
        cycle = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][0]
            cycle += 1
        
        swaps += cycle - 1
    
    return swaps


arr = list(map(int, input().split()))
print(min_swaps(arr))