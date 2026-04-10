def search_matrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return -1

# Input
rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

target = int(input())

print(search_matrix(matrix, target))

"""
Time Complexity:
O(n * m) -> Traverses entire matrix.

Space Complexity:
O(1)
"""