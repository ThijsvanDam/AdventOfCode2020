class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    @property
    def diff(self):
        return abs(self.min - self.max) + 1

    def __str__(self):
        return "{} - {}".format(self.min, self.max)


class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @property
    def seat_id(self):
        id_row_multiplication = 8
        return self.row * id_row_multiplication+ self.col

    def row_exists(self):
        first_row = 0
        last_row = 127
        return not(self.row == first_row or self.row == last_row)

    def __str__(self):
        return "{} - {}".format(self.row, self.col)


class Plane:
    def __init__(self):
        self.available_seats = [[j*8+i for i in range(0, 8)] for j in range(0, 128)]

    def book_seat(self, seat):
        self.available_seats[seat.row].remove(seat.seat_id)

    @property
    def single_seat_available(self):
        str = ""
        count = 0

        for row in self.available_seats:
            if len(row) == 1:
                str += "row({}): seat_id({}) ({})\n".format(count, row, len(row))
            count += 1
        return str

    def __str__(self):
        str = ""
        count = 0

        for row in self.available_seats:
            if len(row) > 0:
                str += "row({}): seat_ids({}) ({})\n".format(count, row, len(row))
            count += 1
        return str


def recursive_determine_seat(seat_string, seat_rows, seat_cols):
    code = seat_string[0]

    if code == "B":
        seat_rows.min = seat_rows.min + (seat_rows.diff / 2)
    elif code == "F":
        seat_rows.max = seat_rows.max - (seat_rows.diff / 2)
    elif code == "R":
        seat_cols.min = seat_cols.min + (seat_cols.diff / 2)
    elif code == "L":
        seat_cols.max = seat_cols.max - (seat_cols.diff / 2)

    if len(seat_string) == 1:
        return seat_rows.min, seat_cols.min
    else:
        remaining_code = seat_string[1:]
        return recursive_determine_seat(remaining_code, seat_rows, seat_cols)


def determine_highest_seat(seats_string_list):
    highest_seat_location = 0

    for seat_string in seats_string_list:
        seat_location = recursive_determine_seat(seat_string, Range(0, 127), Range(0, 7))

        seat_calculation = seat_location[0] * 8 + seat_location[1]
        if seat_calculation > highest_seat_location:
            highest_seat_location = seat_calculation
    return highest_seat_location


def determine_my_seat(seats_string_list):
    plane = Plane()

    for seat_string in seats_string_list:
        seat_location = recursive_determine_seat(seat_string, Range(0, 127), Range(0, 7))
        seat = Seat(row=int(seat_location[0]), col=int(seat_location[1]))
        plane.book_seat(seat)

    return plane.single_seat_available


