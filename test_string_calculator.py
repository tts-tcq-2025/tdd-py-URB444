
from string_calculator import calculate_string

def test_calculate_string_single_string():
    assert calculate_string(['1']) == 1

def test_calculate_string_double_string():
    assert calculate_string(['1', '2']) == 3

def test_calculate_string_multiple_string():
    assert calculate_string(['1', '2', '3']) == 6

def test_calculate_string_with_outofrange_numbers():
    assert calculate_string(['1001', '2', '999']) == 1001

def test_calculate_string_zero():
    assert calculate_string(['0', '0', '0']) == 0