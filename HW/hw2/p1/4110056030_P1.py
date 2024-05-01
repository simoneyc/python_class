class stack:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = {'W': (-1, 0), 'S': (1, 0), 'A': (0, -1), 'D': (0, 1)}
        self.visited = set()
        self.shortest_path = []

    def is_valid_move(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.maze[r][c] != 1 and (r, c) not in self.visited

    def explore_maze(self, r, c, path):
        if self.maze[r][c] == 9:
            if not self.shortest_path or len(path) < len(self.shortest_path):
                self.shortest_path = path
            return
        self.visited.add((r, c))
        for direction in self.directions:
            dr, dc = self.directions[direction]
            new_r, new_c = r + dr, c + dc
            if self.is_valid_move(new_r, new_c):
                self.explore_maze(new_r, new_c, path + [direction])
        self.visited.remove((r, c))

    def count_moves(self):
        move_count = {'W': 0, 'S': 0, 'A': 0, 'D': 0}
        for move in self.shortest_path:
            move_count[move] += 1
        return move_count


def read_maze_from_file(filename):
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append([int(x) for x in line.split()])
    return maze


maze = read_maze_from_file('maze.txt')

solver = stack(maze)
solver.explore_maze(1, 1, [])
move_count = solver.count_moves()

print("找到出口，路徑為:", ''.join(solver.shortest_path))
print("WSAD數量:")
for move in move_count:
    print(f"{move}: {move_count[move]}")
