import re
from process_string import filter_number_string, get_string_parts

def test_filter_number_string_default_delimiter():
    delimiter, nums_str_part = filter_number_string("1,2\n3")
    assert delimiter == ',|\n'
    assert nums_str_part == "1,2\n3"

def test_filter_number_string_single_char_delimiter():
    delimiter, nums_str_part = filter_number_string("//;\n1;2;3")
    assert delimiter == re.escape(';') + '|\n'
    assert nums_str_part == "1;2;3"

def test_filter_number_string_multi_char_delimiter():
    delimiter, nums_str_part = filter_number_string("//[***]\n1***2***3")
    assert delimiter == re.escape('***') + '|\n'
    assert nums_str_part == "1***2***3"

def test_filter_number_string_with_special_char_delimiter():
    delimiter, nums_str_part = filter_number_string("//[.*?]\n1.*?2.*?3")
    assert delimiter == re.escape('.*?') + '|\n'
    assert nums_str_part == "1.*?2.*?3"

def test_get_string_parts_single_char():
    regex_object = re.match(r'^//(\[.*\]|.)\n(.*)', "//;\n1;2;3", re.DOTALL)
    delimiter, nums_str_part = get_string_parts(regex_object)
    assert delimiter == re.escape(';') + '|\n'
    assert nums_str_part == "1;2;3"

def test_get_string_parts_multi_char():
    regex_object = re.match(r'^//(\[.*\]|.)\n(.*)', "//[***]\n1***2***3", re.DOTALL)
    delimiter, nums_str_part = get_string_parts(regex_object)
    assert delimiter == re.escape('***') + '|\n'
    assert nums_str_part == "1***2***3"