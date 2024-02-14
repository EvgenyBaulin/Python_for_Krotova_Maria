from collections import deque


def bfs_shortest_path(graph, start, end):
	n = len(graph)
	visited = [False] * n
	distance = [-1] * n

	queue = deque()
	queue.append(start)
	visited[start] = True
	distance[start] = 0

	while queue:
		current_vertex = queue.popleft()

		for neighbor in range(n):
			if graph[current_vertex][neighbor] == 1 and not visited[neighbor]:
				queue.append(neighbor)
				visited[neighbor] = True
				distance[neighbor] = distance[current_vertex] + 1

	return distance[end]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
start, end = map(int, input().split())

result = bfs_shortest_path(graph, start - 1, end - 1)
print(result)
