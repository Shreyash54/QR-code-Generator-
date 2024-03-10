def count_ways_maze(grid, x, y, n, visited):
    if x == n - 1 and y == n - 1:
        return 1  # We found a valid path

    if x < 0 or y < 0 or y >= n or x >= n or grid[x][y] == 0 or visited[x][y]:
        return 0  # Invalid move, so no additional ways from this point

    visited[x][y] = True

    # Calculate the total number of ways by summing the ways from all four directions
    total_ways = (
        count_ways_maze(grid, x - 1, y, n, visited) +
        count_ways_maze(grid, x + 1, y, n, visited) +
        count_ways_maze(grid, x, y - 1, n, visited) +
        count_ways_maze(grid, x, y + 1, n, visited)
    )

    visited[x][y] = False

    return total_ways

# Example usage with a custom 3x3 maze
maze = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

n = len(maze)
visited = [[False for _ in range(n)] for _ in range(n)]

ways_count = count_ways_maze(maze, 0, 0, n, visited)
print(f"Number of possible ways: {ways_count}")
