
from main import info_ticket

def test_no_data_info_ticket():
    lines = [ '0,1,Pclass,3,4,Sex,6,7,8,9,Fare',
        '1,0,1,0,0,female,0,0,0,0,10.5',
        '2,0,2,0,0,male,0,0,0,0,20',
        '3,0,3,0,0,female,0,0,0,0,15',
        '4,0,1,0,0,male,0,0,0,0,18',
        '5,0,2,0,0,female,0,0,0,0,10.5',
        '2,0,3,0,0,male,0,0,0,0,20',
    ]
    assert info_ticket(lines) == (28.5, 30.5, 35.0)

def test_female_info_ticket():
    lines = [ '0,1,Pclass,3,4,Sex,6,7,8,9,Fare',
        '1,0,1,0,0,female,0,0,0,0,10.5',
        '2,0,2,0,0,male,0,0,0,0,20',
        '3,0,3,0,0,female,0,0,0,0,15',
        '4,0,1,0,0,male,0,0,0,0,18',
        '5,0,2,0,0,female,0,0,0,0,10.5',
        '2,0,3,0,0,male,0,0,0,0,20',
    ]
    assert info_ticket(lines,'female') == (10.5, 10.5, 15.0)

def test_male_info_ticket():
    lines = [ '0,1,Pclass,3,4,Sex,6,7,8,9,Fare',
        '1,0,1,0,0,female,0,0,0,0,10.5',
        '2,0,2,0,0,male,0,0,0,0,20',
        '3,0,3,0,0,female,0,0,0,0,15',
        '4,0,1,0,0,male,0,0,0,0,18',
        '5,0,2,0,0,female,0,0,0,0,10.5',
        '2,0,3,0,0,male,0,0,0,0,20',
    ]
    assert info_ticket(lines,'male') == (18.0, 20.0, 20.0)
