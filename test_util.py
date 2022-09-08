from util import *
import pendulum as pdl


def test_format_to_2_decimal():
    test1 = 704.745234
    assert format_to_2_decimal(test1) == "704.75"
    test2 = -704.744234
    assert format_to_2_decimal(test2) == "-704.74"


def test_should_prev_wed_shift_backwards():
    # Test for run on a wednesday
    wednesday = pdl.datetime(2022, 9, 8, )
    assert should_prev_wed_shift_backwards(wednesday) == False
