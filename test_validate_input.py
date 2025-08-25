# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 01:12:29 2025

@author: HUZ1KOR
"""

import pytest
from validate_input import validate_negatives,validate_number_string

def test_validate_negatives_with_no_negatives():
    assert validate_negatives(['1', '2', '3']) is True

def test_validate_negatives_with_single_negatives():
    with pytest.raises(Exception) as excinfo:
        validate_negatives(['-1', '2', '3'])
    assert "negatives not allowed: -1" in str(excinfo.value)

def test_validate_negatives_with_multiple_negatives():
    with pytest.raises(Exception) as excinfo:
        validate_negatives(['-1', '2', '-33'])
    assert "negatives not allowed: -1, -33" in str(excinfo.value)

def test_validate_negatives_with_all_negatives():
    with pytest.raises(Exception) as excinfo:
        validate_negatives(['-2', '-5'])
    assert "negatives not allowed: -2, -5" in str(excinfo.value)

def test_validate_number_string_with_empty_string():
   assert validate_number_string("") == 0

def test_validate_number_string_with_correct_string():
   assert validate_number_string("1,2,3") == 0
