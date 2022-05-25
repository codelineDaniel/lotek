from drawn_numbers import DrawnNumbers


class GameMechanics(DrawnNumbers):
    def __init__(self, bet_price, count_of_bet_in_week):
        super().__init__()
        self.bet_price = bet_price
        self.count_of_bet_in_week = count_of_bet_in_week
        self.count_of_draw = 1
        self.count_of_three = 0
        self.count_of_four = 0
        self.count_of_five = 0

    def check_your_winnings(self, user_numbers: list[int]):
        is_done = True
        while is_done:
            self.numbers = []
            self.draw_numbers()
            print(self.numbers)
            if set(self.numbers) == set(user_numbers):
                is_done = False
            if len(set(self.numbers) & set(user_numbers)) == 3:
                self.count_of_three += 1
            if len(set(self.numbers) & set(user_numbers)) == 4:
                self.count_of_four += 1
            if len(set(self.numbers) & set(user_numbers)) == 5:
                self.count_of_five += 1
            self.count_of_draw += 1
            print(self.count_of_draw)

    def calculate_time_to_draw_six(self):
        years = (self.count_of_draw / 3) / 52  # 44
        months = ((years - int(years)) * 52) / 4  # 11 miesięcy
        weeks = (months - int(months)) * 4
        return int(years), int(months), int(weeks)

    @property
    def get_count_of_draw(self):
        return self.count_of_draw

    @property
    def get_count_of_three(self):
        return self.count_of_three

    @property
    def get_count_of_four(self):
        return self.count_of_four

    @property
    def get_count_of_five(self):
        return self.count_of_five
