# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/08/2024
# Description: find the median of a list of numbers.
def find_median(numbers):
    """This function finds the median of a list of numbers."""
    if not numbers:
        return None
    sorted_numbers = sorted (numbers)
    length = len(numbers)
    middle = length // 2
    if length % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle])/2
    else:
        median = (sorted_numbers[middle])
    return median
