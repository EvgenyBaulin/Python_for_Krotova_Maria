def dfs(graph, visited, vertex):
	visited[vertex] = True
	for i in range(len(graph)):
		if graph[vertex][i] == 1 and not visited[i]:
			dfs(graph, visited, i)


def count_vertices_in_connected_component(graph, start_vertex):
	n = len(graph)
	visited = [False] * n
	dfs(graph, visited, start_vertex)
	return sum(visited)


N, S = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = count_vertices_in_connected_component(graph, S - 1)

print(result)
