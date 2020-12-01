import day_one


def get_input_list(prefix):
    input_list = []
    with open("{prefix}_input.txt".format(prefix=prefix), "r") as f:
        [input_list.append(int(i)) for i in f]
    return input_list


def day(current_day):
    if current_day != "one":
        print()
    print("The answers of day {} are:".format(current_day))


if __name__ == '__main__':
    day("one")
    print(day_one.get_multiplication_of_2020_sum_two(get_input_list("day_one")))
    print(day_one.get_multiplication_of_2020_sum_three(get_input_list("day_one")))

    day("two")
