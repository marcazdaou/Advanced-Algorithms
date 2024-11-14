def shortestPath(maze, start, destination):
    if maze[start[0]][start[1]] == 0 or maze[destination[0]][destination[1]] == 0:
        return -1  # Invalid start or end position

    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = [(start, 0)]  # (position, distance)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Possible directions: down, up, right, left

    while queue:
        position, distance = queue.pop(0)
        if position == destination:
            return distance
        for dx, dy in directions:
            new_x, new_y = position[0] + dx, position[1] + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), distance + 1))

    return -1  # No valid path found


# Test the function
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1]
]
start = (0, 0)
destination = (3,4)
print("Shortest path length:", shortestPath(maze, start, destination))