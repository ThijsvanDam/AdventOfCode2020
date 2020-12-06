def get_distinct_letter_count(letter_string):
    return len("".join(set(letter_string)))


def get_distinct_letter_count_per_group_sum(input):
    grouped_input = split_into_groups(input)
    return sum(map(lambda x: get_distinct_letter_count(x), grouped_input))


def split_into_groups(form_answers):
    return [x.replace("\n", "") for x in form_answers.split("\n\n")]


def get_unanimous_letter_count_per_group_sum(input):
    return sum([get_unanimous_letter_count(*x) for x in split_into_groups_including_count(input)])


def get_unanimous_letter_count(letter_string, group_count):
    return sum([(1 if letter_string.count(x) >= group_count else 0) for x in set(letter_string)])


def split_into_groups_including_count(form_answers):
    return [(x.replace("\n", ""), x.count("\n") + 1) for x in form_answers.split("\n\n")]


input = None

# not 3486
