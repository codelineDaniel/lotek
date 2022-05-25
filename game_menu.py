class Menu:
    def __init__(self, age):
        self._age = age

    @property
    def user_age(self):
        return self._age

    def show_result(self, count_of_draw, count_of_three, count_of_four, count_of_five, price_bet,
                    years, months, weeks):
        print(f'By wygrać musiałeś zagrać {count_of_draw} razy.')
        print('Do głównej wygranej udało Ci się zdobyć:')
        print(f'Wygranych trójek: {count_of_three}')
        print(f'Wygranych czwórek: {count_of_four}')
        print(f'Wygranych piątek: {count_of_five}')
        print(f'Na wszystkie losy wydałeś {price_bet * count_of_draw:,.2f}')
        print(f'Wygrana nastąpiła by w wieku {self._age + years}')
        print(f'Od wygranej minęło: {years} lata, {months} miesiące i {weeks} tygodnie ')
