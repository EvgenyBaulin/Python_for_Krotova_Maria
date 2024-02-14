def is_adjacency_matrix(matrix, n):
	for i in range(n):
		if matrix[i][i] != 0 or any(x not in (0, 1) for x in matrix[i]):
			return "NO"

	for i in range(n):
		for j in range(i + 1, n):
			if matrix[i][j] != matrix[j][i]:
				return "NO"

	return "YES"


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(is_adjacency_matrix(matrix, n))
