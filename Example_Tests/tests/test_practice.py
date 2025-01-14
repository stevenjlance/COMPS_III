from practice import two_plus_two, one_minus_one

def test_two_plus_two():
    ''''Check that two plus two equals four'''
    assert two_plus_two() == 4

def test_one_minus_one():
    '''Check that one minus one equals zero'''
    assert one_minus_one() == 0