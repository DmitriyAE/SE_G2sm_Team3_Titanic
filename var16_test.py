from var16 import count_survivors


def test_count_survivors_all_classes():
    lines = [
        'PassengerId,Survived,Pclass,,Sex,,,,,Fare',
        '1,1,1,,female,,,,,71.2,,,',
        '2,1,1,,female,,,,,83.1,,,',
        '3,1,2,,female,,,,,53.1,,,',
        '4,1,2,,female,,,,,40.5,,,',
        '5,1,3,,female,,,,,7.9,,,',
        '6,1,3,,female,,,,,9.5,,,'
    ]
    assert count_survivors(lines, (0, 100)) == [2, 2, 2]


def test_count_survivors_first_class_only():
    lines = [
        'PassengerId,Survived,Pclass,,Sex,,,,,Fare',
        '1,1,1,,female,,,,,71.2,,,',
        '2,0,1,,female,,,,,83.1,,,',
        '3,0,1,,female,,,,,100.0,,,'
    ]
    assert count_survivors(lines, (70, 85)) == [1, 0, 0]


def test_count_survivors_no_survivors_in_price_range():
    lines = [
        'PassengerId,Survived,Pclass,,Sex,,,,,Fare',
        '1,1,1,,female,,,,,71.2,,,',
        '2,1,1,,female,,,,,83.1,,,',
        '3,1,2,,female,,,,,53.1,,,',
        '4,1,2,,female,,,,,40.5,,,',
        '5,1,3,,female,,,,,7.9,,,',
        '6,1,3,,female,,,,,9.5,,,'
    ]
    assert count_survivors(lines, (100, 200)) == [0, 0, 0]
