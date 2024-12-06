"""
Advent of Code 2023 Day 13 (Done on Dec 6, 2024)
https://adventofcode.com/2023/day/13
Authors: Samantha (Sam) Tetef, Daniel Moerner, John Yamashiro, Kelechi Ukonu Nwankwoala,
         Ramapriya Radhakrishnan, Satyajit Sarangdhar
"""


def get_input(path):
    patterns = []
    with open(path) as file:
        input = file.read()
        input = input.split("\n\n")
        for pattern in input:
            pattern = pattern.split("\n")
            patterns.append(pattern)
        return patterns


def rotate(pattern):
    rotated_pattern = []
    for j in range(len(pattern[0])):
        line = ""
        for i in range(len(pattern) - 1, -1, -1):
            line += pattern[i][j]
        rotated_pattern.append(line)
    return rotated_pattern


def crop_pattern(pattern, row_num):
    min_dist = min(row_num, len(pattern) - row_num)
    return pattern[row_num - min_dist : row_num + min_dist]


def compare_strings(cropped_pattern):
    halfway = len(cropped_pattern) // 2
    first_half = cropped_pattern[:halfway]
    second_half = cropped_pattern[halfway:]
    return first_half == list(reversed(second_half))


def find_line_of_symmetry(pattern):
    for row_num in range(1, len(pattern)):
        cropped_pattern = crop_pattern(pattern, row_num)
        is_reflection = compare_strings(cropped_pattern)
        if is_reflection:
            return row_num
    return 0


def part1(patterns):
    total = 0
    for pattern in patterns:
        stat = 0
        if not (stat := 100 * find_line_of_symmetry(pattern)):
            pattern = rotate(pattern)
            stat = find_line_of_symmetry(pattern)
        total += stat

    return total


if __name__ == "__main__":
    patterns = get_input("./13.txt")
    print(f"Part 1: {part1(patterns)}")
