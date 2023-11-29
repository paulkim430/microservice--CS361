from collections import deque


def solve_puzzle(board, source, destination):
    rows, cols = len(board), len(board[0])
    directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}

    def is_valid_cell(row, col):
        return 0 <= row < rows and 0 <= col < cols and board[row][col] == '-'

    queue = deque([source])
    visited = set([source])
    parents = {source: None}

    while queue:
        current = queue.popleft()
        if current == destination:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for direction, (dx, dy) in directions.items():
            new_row, new_col = current[0] + dx, current[1] + dy
            neighbor = (new_row, new_col)
            if is_valid_cell(new_row, new_col) and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parents[neighbor] = current

    return None
