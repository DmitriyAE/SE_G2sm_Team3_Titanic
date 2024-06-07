
from var9 import info_ticket


def test_no_data_info_ticket():
    lines = [',,Pclass,,,Sex,,,,,Fare',
             ',,1,,,female,,,,,10.5',
             ',,2,,,male,,,,,20',
             ',,3,,,female,,,,,15',
             ',,1,,,male,,,,,18',
             ',,2,,,female,,,,,10.5',
             ',,3,,,male,,,,,20',
             ]
    assert info_ticket(lines) == (28.5, 30.5, 35.0)


def test_female_info_ticket():
    lines = [',,Pclass,,,Sex,,,,,Fare',
             ',,1,,,female,,,,,10.5',
             ',,2,,,male,,,,,20',
             ',,3,,,female,,,,,15',
             ',,1,,,male,,,,,18',
             ',,2,,,female,,,,,10.5',
             ',,3,,,male,,,,,20',
             ]
    assert info_ticket(lines, 'female') == (10.5, 10.5, 15.0)


def test_male_info_ticket():
    lines = [',,Pclass,,,Sex,,,,,Fare',
             ',,1,,,female,,,,,10.5',
             ',,2,,,male,,,,,20',
             ',,3,,,female,,,,,15',
             ',,1,,,male,,,,,18',
             ',,2,,,female,,,,,10.5',
             ',,3,,,male,,,,,20',
             ]
    assert info_ticket(lines, 'male') == (18.0, 20.0, 20.0)
