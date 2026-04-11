# Question36: Alternate positive and negative

"""
Time Complexity: O n
Space Complexity: O n
"""

def rearrange(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    
    result = []
    for i in range(min(len(pos), len(neg))):
        result.append(pos[i])
        result.append(neg[i])
    
    result += pos[len(neg):]
    result += neg[len(pos):]
    
    return result


arr = list(map(int, input().split()))
print(rearrange(arr))