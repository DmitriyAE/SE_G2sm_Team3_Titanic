from var16 import count_survivors


def test_count_survivors_all_classes():
    lines = [
        'PassengerId,Survived,Pclass,Name,Sex, \
            Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,female,0,0,0,0,71.2833,0,0',
        '2,1,1,0,female,0,0,0,0,83.1583,0,0',
        '3,1,2,0,female,0,0,0,0,53.1000,0,0',
        '4,1,2,0,female,0,0,0,0,40.0500,0,0',
        '5,1,3,0,female,0,0,0,0,7.9250,0,0',
        '6,1,3,0,female,0,0,0,0,9.5875,0,0'
    ]
    assert count_survivors(lines, (0, 100)) == [2, 2, 2]


def test_count_survivors_first_class_only():
    lines = [
        'PassengerId,Survived,Pclass,Name,Sex, \
            Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,female,0,0,0,0,71.2833,0,0',
        '2,0,1,0,female,0,0,0,0,83.1583,0,0',
        '3,0,2,0,female,0,0,0,0,83.1583,0,0',
        '4,0,2,0,female,0,0,0,0,53.1000,0,0',
        '5,0,3,0,female,0,0,0,0,7.9250,0,0',
        '6,0,1,0,female,0,0,0,0,100.0,0,0'
    ]
    assert count_survivors(lines, (70, 85)) == [1, 0, 0]


def test_count_survivors_no_survivors_in_price_range():
    lines = [
        'PassengerId,Survived,Pclass,Name,Sex, \
            Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,female,0,0,0,0,71.2833,0,0',
        '2,1,1,0,female,0,0,0,0,83.1583,0,0',
        '3,1,2,0,female,0,0,0,0,53.1000,0,0',
        '4,1,2,0,female,0,0,0,0,40.0500,0,0',
        '5,1,3,0,female,0,0,0,0,7.9250,0,0',
        '6,1,3,0,female,0,0,0,0,9.5875,0,0'
    ]
    assert count_survivors(lines, (100, 200)) == [0, 0, 0]
    