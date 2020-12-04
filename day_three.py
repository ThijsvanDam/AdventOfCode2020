def count_trees(tree_line_list, hor_steps, vert_steps):
    horizontal = 0
    vertical = 0
    trees = 0

    while vertical < len(tree_line_list):

        tree_line = tree_line_list[vertical].rstrip()

        if tree_line[horizontal % len(tree_line)] == "#":
            trees += 1

        vertical += vert_steps
        horizontal += hor_steps
    return trees


def count_trees_multiple_slopes(tree_line_list):
    return count_trees(tree_line_list, 1, 1) * \
           count_trees(tree_line_list, 3, 1) * \
           count_trees(tree_line_list, 5, 1) * \
           count_trees(tree_line_list, 7, 1) * \
           count_trees(tree_line_list, 1, 2)
