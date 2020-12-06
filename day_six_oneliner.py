def get_distinct_letter_count_per_group_sum_oneliner(i):
    return sum(map(lambda j: len("".join(set(j))), [k.replace("\n", "") for k in i.split("\n\n")]))


def get_unanimous_letter_count_per_group_sum_oneliner(i):
    return sum(sum([(1 if i[0].count(j) >= i[1] else 0) for j in set(i[0])]) for i in
               [(k.replace("\n", ""), k.count("\n") + 1) for k in i.split("\n\n")])
