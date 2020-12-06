import day_one
import day_two
import day_three
import day_four
import day_five
import day_six_oneliner


def get_input_list_string(prefix):
    input_list = []
    with open("inputs/{prefix}_input.txt".format(prefix=prefix), "r") as f:
        [input_list.append(i) for i in f]
    return input_list


def get_input_list_int(prefix):
    input_list = []
    with open("inputs/{prefix}_input.txt".format(prefix=prefix), "r") as f:
        [input_list.append(int(i)) for i in f]
    return input_list


def get_entire_input(prefix, postfix=""):
    with open("inputs/{prefix}_input{postfix}.txt".format(prefix=prefix, postfix=postfix), "r") as f:
        return f.read()


def day(current_day):
    if current_day != "one":
        print()
    print("The answers of day {} are:".format(current_day))


if __name__ == '__main__':
    day("one")
    print(day_one.get_multiplication_of_2020_sum_two(get_input_list_int("day_one")))
    print(day_one.get_multiplication_of_2020_sum_three(get_input_list_int("day_one")))

    day("two")
    print(day_two.count_correct_inputs(get_input_list_string("day_two")))

    day("three")
    print(day_three.count_trees(get_input_list_string("day_three"), 1, 3))
    print(day_three.count_trees_multiple_slopes(get_input_list_string("day_three")))

    day("four")
    print(day_four.validate_passwords(get_entire_input("day_four")))

    day("five")
    print(day_five.determine_highest_seat(get_input_list_string("day_five")))
    print(day_five.determine_my_seat(get_input_list_string("day_five")))

    day("six")
    print(day_six_oneliner.get_distinct_letter_count_per_group_sum_oneliner(get_entire_input("day_six")))
    print(day_six_oneliner.get_unanimous_letter_count_per_group_sum_oneliner(get_entire_input("day_six")))

