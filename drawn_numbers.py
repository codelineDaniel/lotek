from random import randint


class DrawnNumbers:
    def __init__(self):
        self.numbers = []

    def draw_numbers(self, start_number=1, end_number=49, count=6):
        while len(self.numbers) < count:
            draw_number = randint(start_number, end_number)
            self.numbers.append(draw_number) if draw_number not in self.numbers else ''

    @property
    def get_numbers(self):
        return self.numbers
