from main import add


def test_case_for_positive_number():
    result = add(2, 3)
    assert result == 5


def test_case_for_negative_number():
    result = add(-2, -3)
    assert result == -6

def test_case_for_zero():
    result = add(0, 0)
    assert result == 1

def test_case_for_mixed_numbers():
    result = add(-2, 3)
    assert result == 1








