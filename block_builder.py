""" 
Codewriting Task: Building Blocks and Obstacles on a Number Line

Given an infinite integer number line, you need to implement code that supports two types of operations:

	1.	[1, x]: Builds an obstacle at coordinate x along the number line. It is guaranteed that coordinate x
        does not contain any obstacles when this operation is performed.
	2.	[2, x, size]: Checks whether it is possible to build a block of size size which ends immediately 
        before or on coordinate x. This operation checks coordinates x and (x - size + 1). It produces "1" 
        if possible (i.e., there are no obstacles at the specified coordinates), or "0" otherwise. This operation 
        does not actually build the block, it only checks whether a block can be built.

Given an array of operations containing both types of operations described above, your task is to return a binary 
string representing the outputs for all [2, x, size] operations.

Example

For:

operations = [
  [1, 2],
  [1, 5],
  [2, 5, 2],
  [2, 3, 1],
  [2, 2, 2],
  [2, 3, 2]
]
obstacles on 2 and 5
The output should be:

solution(operations) = "1110"

Explanation:

Consider each operation:

	1.	[1, 2] - Builds an obstacle at coordinate 2.
	2.	[1, 5] - Builds an obstacle at coordinate 5.
	3.	[2, 5, 2] - Checks and produces "1" since it is possible to build a block occupying coordinates 3 and 4.
	4.	[2, 3, 1] - Checks and produces "1" since it is possible to build a block of size 1 occupying coordinate 3.
	5.	[2, 2, 2] - Checks and produces "1" since it is possible to build a block occupying coordinates 0 and 1.
	6.	[2, 3, 2] - Checks and produces "0" since it is not possible to build a block occupying coordinates 1 and 2 due to the obstacle at coordinate 2.


WRONG ORIGINAL EXAMPLES

solution(operations) = "1010"
Consider each operation:

	1.	[1, 2] - Builds an obstacle at coordinate 2.
	2.	[1, 5] - Builds an obstacle at coordinate 5.
	3.	[2, 5, 2] - Checks and produces "1" since it is possible to build a block occupying coordinates 3 and 4.
	4.	[2, 3, 1] - Checks and produces "0" since it is not possible to build a block occupying coordinate 3 because there is an obstacle at coordinate 5.
	5.	[2, 2, 2] - Checks and produces "1" since it is possible to build a block occupying coordinates 1 and 2.
	6.	[2, 3, 2] - Checks and produces "0" since it is not possible to build a block occupying coordinates 1 and 2 due to the obstacle at coordinate 2.

Thus, the output is "1010".

This should help explain the task and the expected output format.
 """


def block_builder(operations: list[list[int]]) -> str:
    number_line: list[int] = []
    answer: str = ""

    def place_block(operation):
        size = operation[2]
        curr_zero_block = 0
        for i in range(location - 1, -1, -1):
            if number_line[1] == 0:
                curr_zero_block += 1
            else:
                curr_zero_block = 0

            if curr_zero_block >= size:
                return "1"
        return "0"

    for operation in operations:
        location = operation[1]
        if operation[0] == 1:
            if location < len(number_line):
                number_line[location] = 1
            else:
                for i in range(len(number_line), location):
                    number_line.append(0)
                number_line.append(1)
        elif operation[0] == 2:
            answer += place_block(operation)

    print(f"{answer=}")
    return answer


import bisect
from typing import Callable


def index_block_builder(operations: list[list[int]]) -> str:
    obstacles: list[int] = []

    def place_obstacle(x: int) -> str:
        # insert_idx = bisect.bisect_left(obstacles, x)
        # obstacles.insert(insert_idx, x)
        bisect.insort_left(obstacles, x)
        return ""

    def place_block(end: int, size: int) -> str:
        start = end - size + 1
        left_idx = bisect.bisect_left(obstacles, start)
        right_idx = bisect.bisect_left(obstacles, end)
        return "1" if right_idx == left_idx else "0"

    function_dict: dict[int, Callable] = {1: place_obstacle, 2: place_block}

    return "".join(
        function_dict[operation[0]](*operation[1:]) for operation in operations
    )


operations = [[1, 5], [1, 2], [2, 5, 2], [2, 3, 1], [2, 2, 2], [2, 3, 2]]
assert index_block_builder(operations) == "1110"
