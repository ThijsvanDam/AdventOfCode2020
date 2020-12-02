class InputConversion:

    def __init__(self, input_string):
        splitted = input_string.split(" ")

        self.input_string = input_string
        numbers = splitted[0].split("-")
        self.firstNum = numbers[0]
        self.secondNum = numbers[1]
        self.letter = splitted[1].replace(":", "")
        self.text = splitted[2]


def check_part_one(input_conversion):
    return int(input_conversion.firstNum) <= input_conversion.text.count(input_conversion.letter) <= int(
        input_conversion.secondNum)


def check_part_two(input_conversion):
    return (input_conversion.text[int(input_conversion.firstNum) - 1] == input_conversion.letter) != (
                input_conversion.text[int(input_conversion.secondNum) - 1] == input_conversion.letter)


def count_correct_inputs(input_list):
    count_one = 0
    count_two = 0
    for input_string in input_list:
        input_conversion = InputConversion(input_string)

        if check_part_one(input_conversion):
            count_one += 1

        if check_part_two(input_conversion):
            count_two += 1

    return count_one, count_two
