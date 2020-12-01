total_sum = 2020


def get_multiplication_of_2020_sum_two(number_list):
    for i in range(len(number_list)):
        if (total_sum - number_list[i]) in number_list:
            return number_list[i] * (total_sum - number_list[i])


def get_multiplication_of_2020_sum_three(number_list):
    for i in range(len(number_list)):
        first_number = number_list[i]
        for j in range(len(number_list) - 1):
            if j is not i:
                second_number = number_list[j]
                if (total_sum - first_number - second_number) in number_list:
                    return (total_sum - first_number - second_number) * first_number * second_number
