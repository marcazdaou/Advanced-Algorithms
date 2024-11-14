def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        # Find the node with the smallest distance that has not been visited yet
        min_dist_node = None
        min_dist = float('inf')
        for node in graph:
            if node not in visited and distances[node] < min_dist:
                min_dist_node = node
                min_dist = distances[node]

        if min_dist_node is None:
            break

        visited.add(min_dist_node)

        # Update distances to neighbors of the current node
        for neighbor, weight in graph[min_dist_node].items():
            new_dist = distances[min_dist_node] + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist

    return distances[end]


# Example usage
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 7, 'E': 4},
    'D': {'E': 2},
    'E': {}
}
start_node = 'A'
end_node = 'E'
shortest_distance = dijkstra(graph, start_node, end_node)
print("Shortest distance from node", start_node, "to node", end_node + ":", shortest_distance)