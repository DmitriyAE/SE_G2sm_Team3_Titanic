from var7 import calculate_average_age


def test_calculate_average_age_without_family_size():
    lines = [
        'PassengerId,,Pclass,,,,Age,SibSp',
        '1,,1,,,,10,2',
        '2,,1,,,,20,3',
        '3,,2,,,,30,4',
        '4,,2,,,,40,5',
        '5,,3,,,,50,6',
        '6,,3,,,,60,7',
    ]
    assert calculate_average_age(lines) == (15.0, 35.0, 55.0)


def test_calculate_average_age_with_family_size_2():
    lines = [
        'PassengerId,,Pclass,,,,Age,SibSp',
        '1,,1,,,,10,2',
        '2,,1,,,,20,3',
        '3,,2,,,,30,4',
        '4,,2,,,,40,5',
        '5,,3,,,,50,6',
        '6,,3,,,,60,7',
    ]
    assert calculate_average_age(
        lines, consider_family_size=True, family_size=2) == (10.0, 0, 0)


def test_calculate_average_age_with_invalid_data():
    lines = [
        'PassengerId,,Pclass,,,,Age,SibSp',
        '1,,1,,,,10,2',
        '2,,1,,,,,3',
        '3,,2,,,,Тридцать,4',
        '4,,2,,,,40,5',
        '5,,3,,,,50,6',
        '6,,3,,,,60,7',
    ]
    assert calculate_average_age(lines) == (10.0, 40.0, 55.0)
