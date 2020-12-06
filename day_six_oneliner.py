def get_distinct_letter_count_per_group_sum_oneliner(input):
    return sum(map(lambda j: len("".join(set(j))), [x.replace("\n", "") for x in input.split("\n\n")]))


def get_unanimous_letter_count_per_group_sum_oneliner(input):
    return sum(sum([(1 if x[0].count(j) >= x[1] else 0) for j in set(x[0])]) for x in
               [(x.replace("\n", ""), x.count("\n") + 1) for x in input.split("\n\n")])
