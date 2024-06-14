from var3 import passenger


def test_passengers_all():
    lines = [
        ',Survived,,,Sex',
        ',1,,,female',
        ',1,,,male',
        ',1,,,female',
        ',0,,,male',
        ',1,,,female',
        ',0,,,male'
    ]
    assert passenger(lines, "Всего") == {'мужчин': 3, 'женщин': 3}


def test_passengers_survived():
    lines = [
        ',Survived,,,Sex',
        ',1,,,female',
        ',0,,,male',
        ',1,,,female',
        ',0,,,male',
        ',1,,,female',
        ',0,,,male'
    ]
    assert passenger(lines, "Выживших (1)") == {'мужчин': 0, 'женщин': 3}


def test_passengers_not_survived():
    lines = [
        ',Survived,,,Sex,,,,,,,',
        ',1,,,female,,,,,,,',
        ',0,,,male,,,,,,,',
        ',1,,,female,,,,,,,',
        ',0,,,male,,,,,,,',
        ',1,,,female,,,,,,,',
        ',0,,,male,,,,,,,'
    ]
    assert passenger(lines, "Погибших (0)") == {'мужчин': 3, 'женщин': 0}
