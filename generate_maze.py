import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # Implement create_dfs
    backtrack_stack = []
    current_cell = random.randint(0, m.total_cells - 1)
    visited_cells = 1

    while visited_cells < m.total_cells:
        neighbors = m.cell_neighbors(current_cell)
        if len(neighbors) > 0:
            n_index = random.randint(0, len(neighbors) - 1)
            new_cell = neighbors[n_index]
            m.connect_cells(current_cell, new_cell[0], new_cell[1])
            backtrack_stack.append(current_cell)
            current_cell = new_cell[0]
            visited_cells += 1
        else:
            current_cell = backtrack_stack.pop()
        m.refresh_maze_view()
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    main()
