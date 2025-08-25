import re

def filter_number_string(number_string):
    delimiter = ',|\n'
    nums_str_part = number_string
    if number_string.startswith('//'):
        match = re.match(r'^//(\[.*\]|.)\n(.*)', number_string, re.DOTALL)
        if match:
            delimiter,nums_str_part = get_string_parts(match)

    return delimiter,nums_str_part

def get_string_parts(regex_object):
    delim_part, nums_str_part = regex_object.groups()
    if delim_part.startswith('[') and delim_part.endswith(']'):
        delim = re.escape(delim_part[1:-1])
    else:
        delim = re.escape(delim_part)
    delimiter = delim + '|\n'

    return delimiter,nums_str_part
