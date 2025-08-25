def validate_number_string(number_string):
    """Returns 0 if the 'number_string' is empty."""

    if not number_string:
        return 0

def validate_negatives(number_list):
    """ Raises an expception is negative numbers are found in the input"""
    
    negatives = [int(n) for n in number_list if n and int(n) < 0]
    if negatives:
        raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
    else:
        return True
