""" 
50 mins

Codewriting Task: Bubble Explosion

Imagine you are given a board of cells, each containing a bubble of a specific color. Neighboring cells of a bubble are defined as
adjacent cells (either in the same row or column) that have a common side with the given cell. For example, neighboring cells for
each of the cells A, B, and C are highlighted in the diagram with corresponding colors.

Task:

Your task is to perform a bubble explosion on the board. A bubble explosion is defined by the following rules:

	1.	A bubble within any given cell is eligible to explode if it has the same color as bubbles in at least 2 neighboring cells.
	2.	All eligible bubbles and their neighboring bubbles of the same color are marked for explosion.
	3.	All marked bubbles explode at the same time. Exploded bubbles are removed from the board, resulting in empty cells.
	4.	After all exploded bubbles are removed, remaining bubbles in cells above empty cells drop down to fill all empty cells.

Input:

	•	A multidimensional array of integers representing the initial board of cells (bubbles). Integers represent colors of bubbles
        within cells. All cells will initially contain bubbles.

Output:

	•	Return the final state of the board after a bubble explosion. The output should be a multidimensional array of integers with 
        the same size as bubbles, replacing all empty cells (without bubbles) with 0.

Constraints:

	•	1 ≤ bubbles.length ≤ 100
	•	1 ≤ bubbles[i][j] ≤ 10^4

Example:

For:

bubbles = [
  [1, 1, 2, 1],
  [1, 1, 2, 2],
  [3, 1, 2, 2],
  [3, 3, 3, 4]
]

The output should be:

solution(bubbles) = [
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 1],
  [0, 0, 0, 4]
]

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than  will fit within the execution time limit.
"""


def bubble_explosion(bubbles: list[list[int]]) -> list[list[int]]:
    max_row = len(bubbles)
    max_col = len(bubbles[0])

    directions = [
        (1, 0),  # down
        (-1, 0),  # up
        (0, 1),  # right
        (0, -1),  # left
    ]

    # find eligible
    def is_eligible(row_idx, col_idx):
        curr_color = bubbles[row_idx][col_idx]
        matching_neighbors = get_matching_neighbors(curr_color, row_idx, col_idx)
        return len(matching_neighbors) >= 2

    def flood_fill(row_idx, col_idx, col) -> None:
        # BFS with queue
        queue = [(row_idx, col_idx)]
        while queue:
            # print(f"{queue=}")
            r, c = queue.pop()
            bubbles[r][c] = 0
            matching_neighbors = get_matching_neighbors(col, r, c)
            queue.extend(matching_neighbors)

    def get_matching_neighbors(
        color: int, row_idx: int, col_idx: int
    ) -> list[tuple[int, int]]:
        return [
            (new_row, new_col)
            for d_row, d_col in directions
            if 0 <= (new_row := row_idx + d_row) < max_row
            and 0 <= (new_col := col_idx + d_col) < max_col
            and bubbles[new_row][new_col] == color
        ]

    for row_idx in range(max_row):
        for col_idx in range(max_col):
            if is_eligible(row_idx, col_idx):
                col = bubbles[row_idx][col_idx]
                if col != 0:
                    flood_fill(row_idx, col_idx, col)

    # flood fill eligible

    # drop down.
    # explode eligibles along with flanking ones.
    # [1, 0, 0, 4] -> [1, 4]  -> [0, 0, 1, 4] -> invert
    def inversion_drop(bubbles: list[list[int]]) -> list[list[int]]:
        # invert, remove 0's
        inverted = [
            [row[idx] for row in bubbles if row[idx] != 0] for idx in range(max_col)
        ]

        # ref-fill 0s to the left
        inverted = [[0] * (max_col - len(row)) + row for row in inverted]

        # invert back to original form
        inverted = [[row[idx] for row in inverted] for idx in range(max_row)]

        return inverted

    def drop_from_top(arr):
        # ooo side effects
        for i in range(max_row - 1):
            for j in range(max_col):
                # if cell is nonzero and cell below is zero: flip!
                if arr[i][j] != 0 and arr[i + 1][j] == 0:
                    arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
                    # cell_col, below_col = below_col, cell_col
        return arr

    def pull_from_bottom(arr):
        for j in range(max_col):
            i = nonzero_i = max_row - 1
            while i >= 0 and nonzero_i >= 0:
                while arr[nonzero_i][j] == 0 and nonzero_i > 0:
                    nonzero_i = nonzero_i - 1
                arr[i][j], arr[nonzero_i][j] = arr[nonzero_i][j], arr[i][j]
                i = i - 1
                nonzero_i = nonzero_i - 1
        return arr

    testinput = [[0, 0, 0, 0], [0, 7, 0, 1], [0, 3, 0, 4], [5, 0, 0, 0]]
    # print(f'{drop_from_top(bubbles)=}')
    print(f"{pull_from_bottom(testinput)=}")
    # print(f'{inversion_drop(bubbles)=}')
    # return bubbles
    # return inversion_drop(bubbles)
    # return drop_from_top(bubbles)
    return pull_from_bottom(bubbles)


bubbles = [[5, 1, 2, 1], [1, 1, 2, 2], [3, 1, 2, 2], [3, 3, 3, 4]]

exploded_bubbles = bubble_explosion(bubbles)
for row in exploded_bubbles:
    print(row)
