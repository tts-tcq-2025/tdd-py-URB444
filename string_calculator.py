import re
from process_string import filter_number_string
from validate_input import validate_number_string,validate_negatives

def evaluate_string(number_string):
    if validate_number_string(number_string)!=0: # Checks if 'number_string' is empty
        delimiter,number_string = filter_number_string(number_string) # Seperate delimiters and numbers
        number_list = re.split(delimiter, number_string) # List of numbers to be added
        if validate_negatives(number_list):
            return calculate_string(number_list)
    else:
        return 0

def calculate_string(number_list):
    """Returns the sum of the numbers in 'number_list' """
    return sum(int(n) for n in number_list if n and int(n) <= 1000)


if __name__ == '__main__':
    print(evaluate_string("1"))
    print(evaluate_string("1,2"))
