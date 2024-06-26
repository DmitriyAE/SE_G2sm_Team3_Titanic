from var2 import count_passengers


def test_count_passengers():
    lines = ['0,Survived,2,3,4,5,5,7,8,9,10,Embarked',
             '1,1,,,,,,,,,,,C',
             '2,1,,,,,,,,,,,Q',
             '3,1,,,,,,,,,,,C',
             '4,1,,,,,,,,,,,S',
             '5,0,,,,,,,,,,,C',
             '6,0,,,,,,,,,,,Q',
             '7,0,,,,,,,,,,,C',
             '8,0,,,,,,,,,,,S',
             ]
    assert count_passengers(lines) == (0, 0)


def test_C_count_passengers():
    lines = ['0,Survived,2,3,4,5,5,7,8,9,10,Embarked',
             '1,1,,,,,,,,,,,C',
             '2,1,,,,,,,,,,,Q',
             '3,1,,,,,,,,,,,C',
             '4,1,,,,,,,,,,,S',
             '5,0,,,,,,,,,,,C',
             '6,0,,,,,,,,,,,Q',
             '7,0,,,,,,,,,,,C',
             '8,0,,,,,,,,,,,S',
             ]
    assert count_passengers(lines, 'C') == (2, 2)


def test_Q_count_passengers():
    lines = ['0,Survived,2,3,4,5,5,7,8,9,10,Embarked',
             '1,1,,,,,,,,,,,C',
             '2,1,,,,,,,,,,,Q',
             '3,1,,,,,,,,,,,C',
             '4,1,,,,,,,,,,,S',
             '5,0,,,,,,,,,,,C',
             '6,0,,,,,,,,,,,Q',
             '7,0,,,,,,,,,,,C',
             '8,0,,,,,,,,,,,S',
             ]
    assert count_passengers(lines, 'Q') == (1, 1)


def test_S_count_passengers():
    lines = ['0,Survived,2,3,4,5,5,7,8,9,10,Embarked',
             '1,1,,,,,,,,,,,C',
             '2,1,,,,,,,,,,,Q',
             '3,1,,,,,,,,,,,C',
             '4,1,,,,,,,,,,,S',
             '5,0,,,,,,,,,,,C',
             '6,0,,,,,,,,,,,Q',
             '7,0,,,,,,,,,,,C',
             '8,1,,,,,,,,,,,S',
             ]
    assert count_passengers(lines, 'S') == (0, 2)
