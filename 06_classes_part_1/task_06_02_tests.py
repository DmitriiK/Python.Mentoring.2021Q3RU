import pytest
from task_06_02 import Euro, Dollar, Ruble, Currency

all_currencies = [Euro, Dollar, Ruble]
euroName = 'Euro'
rubleName = 'Ruble'
dollarName = 'Dollar'

euro2dollar = 1.25
euro2ruble = 85
dollar2ruble = 72
_curr_rates = {
    (euroName, dollarName): euro2dollar,
    (euroName, rubleName): euro2ruble,
    (dollarName, rubleName): dollar2ruble,
}

Currency._curr_rates = _curr_rates

test_currency_pairs = [
    (Euro, Ruble, euro2ruble),
    (Euro, Dollar, euro2dollar),
    (Dollar, Ruble, dollar2ruble),
    (Dollar, Euro, 1 / euro2dollar),
    (Ruble, Euro, 1 / euro2ruble),
    (Ruble, Dollar, 1 / dollar2ruble)
]


@pytest.mark.parametrize("curr_from, curr_to, expected_rate",
                         test_currency_pairs)
def test_convertation(curr_from, curr_to, expected_rate):
    kilo = curr_from(1000)
    converted_kilo = kilo.to(curr_to)
    print(f'{kilo} <-> {converted_kilo}')
    rate = converted_kilo.value / kilo.value
    assert rate == expected_rate


def test_set_new_course():
    print('test_set_new_course')
    old_course = Ruble.course(Euro)
    test_rub2euro = 40
    Ruble.set_course(Euro, test_rub2euro)
    print(f'Ruble.course(Euro) = {Ruble.course(Euro)}')
    assert Ruble.course(Euro) == test_rub2euro
    Ruble.set_course(Euro, old_course)
    # otherwise it could break further tests


def test_plus_minus_scalar():
    for curr_cls in all_currencies:
        value_to_add = 100
        a = curr_cls(500)
        before = a.value
        a += value_to_add
        after = a.value
        assert (after - before) == value_to_add
        # test minus scalar
        before = a.value
        a -= value_to_add
        after = a.value
        assert (after - before) == -value_to_add


def test_multiply():
    for curr_cls in all_currencies:
        mult = 5
        a = curr_cls(500)
        b = a * mult
        assert a.value * mult == b.value


@pytest.mark.parametrize("curr_1, curr_2, expected_rate", test_currency_pairs)
def test_operations(curr_1, curr_2, expected_rate):
    a = curr_1(100)
    b = curr_2(100)
    c = a + b
    b_in_a = b.value / expected_rate
    print(c)
    assert c.value == a.value + b_in_a
    c = a - b
    print(c)
    assert c.value == a.value - b_in_a


def test_sum_function():
    lst = [Euro(1), Euro(2)]
    xx = sum(lst)
    print(f'sum(lst)={xx}')

@pytest.mark.parametrize("curr_1, curr_2, rate", test_currency_pairs)
def test_equity(curr_1, curr_2, rate):
    print('test_equity')
    x = curr_1(25)
    eu2_ru = curr_1.course(curr_2)
    y = curr_2(x.value * eu2_ru)
    print(f'{x} <-> {y}')
    assert x == y
    y += 1
    print(f'{x} <-> {y}')
    assert x < y
    y -= 2
    print(f'{x} <-> {y}')
    assert x > y
