def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]  # Priority queue: (distance, node)

    # Custom priority queue functions
    def push(queue, item):
        queue.append(item)
        queue.sort(key=lambda x: x[0])

    def pop(queue):
        return queue.pop(0)

    while pq:
        dist, node = pop(pq)

        # Skip if the distance to the node is already greater than the known shortest distance
        if dist > distances[node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            # Update the distance if a shorter path is found
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                push(pq, (new_dist, neighbor))

    # Print the shortest distances to each vertex
    shortest_distances = distances
    for vertex, distance in shortest_distances.items():
        if distance == float('inf'):
            print("INF")
        else:
            print(distance)


# Example usage
graph = {
    0: {1: 10, 2: 5},
    1: {2: 2, 3: 1},
    2: {1: 3, 3: 9},
    3: {},
    4: {}
}
start_node = 0
end_node = 4
dijkstra(graph, start_node, end_node)