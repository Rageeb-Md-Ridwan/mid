class Star_Cinema:
    _hall_list = []

    # task1
    @classmethod
    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    # task2
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        super().entry_hall(self)

    # task3
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

        seats = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(0)
            seats.append(row)
        self._seats[id] = seats

    # task4
    def book_seats(self, show_id, seat_list):
        if show_id in self._seats:
            seats = self._seats[show_id]
            for row, col in seat_list:
                if (
                    0 <= row < self._rows
                    and 0 <= col < self._cols
                    and seats[row][col] == 0
                ):
                    seats[row][col] = 1
                    print(f"Booked at {row}-{col}.")
                else:
                    print(f"Unavailable")
        else:
            print(f"Not found")

    # task5
    def view_show_list(self):
        if self._show_list:
            print("Shows running:")
            for show_id, movie_name, time in self._show_list:
                print(f"ID: {show_id}, Movie: {movie_name}, Time: {time}")

    # task6
    def view_available_seats(self, show_id):
        if show_id in self._seats:
            seats = self._seats[show_id]
            print(f"Available seats for {show_id}: ")
            for row in range(self._rows):
                for col in range(self._cols):
                    if seats[row][col] == "free":
                        print(f"{row} - {col} is available.")
        else:
            print(f"Not found")


# task7
class Counter:
    def __init__(self):
        self._halls = []

    def add_hall(self, hall):
        self._halls.append(hall)

    def view_all_shows(self):
        for hall in self._halls:
            hall.view_show_list()

    def view_available_seats(self, show_id):
        for hall in self._halls:
            hall.view_available_seats(show_id)

    def book_tickets(self, show_id, seat_list):
        for hall in self._halls:
            hall.book_seats(show_id, seat_list)
