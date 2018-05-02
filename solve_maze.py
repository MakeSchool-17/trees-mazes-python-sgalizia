import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    backtrack_stack = []
    current_cell = 0
    visited_cells = 0

    # While the current_cell is not the goal
    while current_cell != m.total_cells - 1:
        neighbors = m.cell_neighbors(current_cell)
        neighbors_length = len(neighbors)
        if neighbors_length > 0:
            n_index = random.randint(0, neighbors_length - 1)
            new_cell = neighbors[n_index]
            m.visit_cell(current_cell, new_cell[0], new_cell[1])
            backtrack_stack.append(current_cell)
            current_cell = new_cell[0]
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = backtrack_stack.pop()
        m.refresh_maze_view()
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    from collections import deque
    queue = deque()
    current_cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.append((current_cell, in_direction))

    while current_cell != (m.total_cells - 1) and len(queue) > 0:
        current_cell, in_direction = queue.popleft()
        m.bfs_visit_cell(current_cell, in_direction)
        visited_cells += 1
        m.refresh_maze_view()

        neighbors = m.cell_neighbors(current_cell)
        for neighbor in neighbors:
            queue.append(neighbor)

    m.reconstruct_solution(current_cell)
    m.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
