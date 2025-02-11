# -*- coding: utf-8 -*-


def find_combination_from_grid(grid):
    com = 1
    for x in grid.values():
        com *= len(x)
    return com


for key, value in hypertuned_params_gs.items():
    nb_combination = find_combination_from_grid(value)
    print("%s: %i combinations " % (key, nb_combination))

