"""
Authors: Saleh Alghusson, Daniel Moerner, Satyajit Sarangdhar, Ramapriya Radhakrishnan

The Number Bracelets Game referenced in Peter Norvig's Pytudes
http://www.geom.uiuc.edu/~addingto/number_bracelets/number_bracelets.html
https://github.com/norvig/pytudes/blob/main/ipynb/NumberBracelets.ipynb
The Rules:
Imagine that you have lots of beads, numbered from 0 through 9, as many as you want of each kind. Here are the rules for making a number bracelet:

1. Pick a first and a second bead. They can have the same number.
2. To get the third bead, add the numbers on the first and second beads. If the sum is more than 9, just use the last (ones) digit of the sum.
3. To get the next bead, add the numbers on the last two beads you used, and use only the ones digit. So to get the fourth bead, add the numbers on the second and third beads, and use the ones digit.
4. Keep going until you get back to the first and second beads, in that order.
5. Then pop off the last two beads.

input: tuple of two ints  from 0-9.
output: tuple of ints of size n (n is undefined), all the ints from 0-9.

number_bracelet((2, 6)) -> (2, 6, 8, 4)
    1. (2, 6)
    2. (2, 6, 2+6) -> (2, 6, 8)
    3. (2, 6, 8, 6+8 % 10) -> (2, 6, 8, 14%10) -> (2, 6, 8, 4)
    4. (2, 6, 8, 4, 8+4 % 10) -> (2, 6, 8, 4, 12%10) -> (2, 6, 8, 4, 2).
    5. (2, 6, 8, 4, 2, 4+2 % 10) -> (2, 6, 8, 4, 2, 6) -> return (2, 6, 8, 4). because first two beads (2,6) == last two beads (2,6)     
"""

import time

def get_all_tuple_pairs():
    results = []
    for i in range(10):
        for j in range(10):
            results.append(tuple([i, j]))
    return results


def get_all_list_pairs():
    results = []
    for i in range(10):
        for j in range(10):
            results.append([i, j])
    return results      


def make_bracelet_for_tuples(beads):
    if len(beads) != 2:
        raise Exception('Invalid Input')
    
    while True:
        new_bead = (beads[-2] + beads[-1]) % 10
        beads = (*beads, new_bead)
        if beads[:2] == beads[-2:]:
            return beads[:-2]

def make_bracelet_for_lists(beads):
    if len(beads) != 2:
        raise Exception('Invalid Input')
    
    while True:
        new_bead = (beads[-2] + beads[-1]) % 10
        beads.append(new_bead)
        if beads[:2] == beads[-2:]:
            return beads[:-2]

shortest_bracelet_len = float("inf") # what's a good starting number?
longest_bracelet_len = 0
shortest_beads = list()
longest_beads = list()
shortest_result = list()
longest_result = list()


tuple_pairs = get_all_tuple_pairs()
start_time = time.time()
for beads in tuple_pairs:
    result_list = make_bracelet_for_tuples(beads)
    
    if len(result_list) > longest_bracelet_len:
        longest_beads = beads
        longest_result = result_list
        longest_bracelet_len = len(result_list)
        
    if len(result_list) < shortest_bracelet_len:
        shortest_beads = beads
        shortest_result = result_list
        shortest_bracelet_len = len(result_list)

    # print(f"number_set: {beads}. bracelet: {result_list}")
end_time = time.time()
print(f"tuple_time: {end_time-start_time}")

list_pairs = get_all_list_pairs()
start_time = time.time()
for beads in list_pairs:
    result_list = make_bracelet_for_lists(beads)
    
    if len(result_list) > longest_bracelet_len:
        longest_beads = beads
        longest_result = result_list
        longest_bracelet_len = len(result_list)
        
    if len(result_list) < shortest_bracelet_len:
        shortest_beads = beads
        shortest_result = result_list
        shortest_bracelet_len = len(result_list)

    # print(f"number_set: {beads}. bracelet: {result_list}")
end_time = time.time()
print(f"list_time: {end_time-start_time}")


print()
# print(f"shortest_beads: {shortest_beads}. bracelet: {shortest_result}, {len(shortest_result)}")
# print(f"longest_beads: {longest_beads}. bracelet: {longest_result}, {len(longest_result)}")
