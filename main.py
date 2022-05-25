from game_mechanics import GameMechanics
from game_menu import Menu


class Application:

    @staticmethod
    def main():
        user_age_input = int(input('Podaj swój wiek: '))
        menu = Menu(user_age_input)

        number_to_check = [34, 23, 5, 6, 19, 9]
        new_numbers = GameMechanics(3, 3)
        new_numbers.draw_numbers()
        new_numbers.check_your_winnings(number_to_check)
        years, months, weeks = new_numbers.calculate_time_to_draw_six()

        menu.show_result(
            new_numbers.get_count_of_draw,
            new_numbers.get_count_of_three,
            new_numbers.get_count_of_four,
            new_numbers.get_count_of_five,
            new_numbers.bet_price,
            years,
            months,
            weeks
        )


if __name__ == '__main__':
    Application.main()
