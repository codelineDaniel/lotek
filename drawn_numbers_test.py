from drawn_numbers import DrawnNumbers


def test_draw_numbers():
    # given
    computer_numbers = DrawnNumbers()

    # when
    computer_numbers.draw_numbers()

    # then
    assert len(computer_numbers.get_numbers)