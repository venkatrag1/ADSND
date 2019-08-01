import unittest
import random

def _get_min_max(ints, left, right):
    """
    Recursive helper to find min and max from left and right halves and to compare the two min/max

    Args:
       ints(list): list of integers containing one or more integers
       left(int): Left index within which to look for min/max
       right(int): Right index within which to look for min/max
    """
    if right <= left + 1:
        # Takes care of 1 and 2 elements- since left and right will be same for 1 elements so
        # doesn't matter how you index it. For 1
        if ints[left] < ints[right]:
            return ints[left], ints[right]
        else:
            return ints[right], ints[left]
    middle = left + (right - left) // 2
    left_min, left_max = _get_min_max(ints, left, middle)
    right_min, right_max = _get_min_max(ints, middle+1, right)
    # Compare min and max of two halves
    if left_min < right_min:
        min_int = left_min
    else:
        min_int = right_min

    if left_max > right_max:
        max_int = left_max
    else:
        max_int = right_max
    return min_int, max_int


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0: # Handle special case of zero elements to return None for min/max
        return None, None
    return _get_min_max(ints, 0, len(ints)-1)

class TestMinMaxUnsortedArr(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def print_pass_fail(self, expected_min, expected_max, ints):
        print ("Pass" if ((expected_min, expected_max) == get_min_max(ints)) else "Fail")

    def test_case1(self):
        ## Example Test Case of Ten Integers
        l = [i for i in range(0, 10)]  # a list containing 0 - 9
        random.shuffle(l)
        self.print_pass_fail(0, 9, l)

    def test_case2(self):
        # Empty list
        l = []  # a list containing 0 - 9
        self.print_pass_fail(None, None, l)

    def test_case3(self):
        ## One element
        l = [10]  # a list containing 0 - 9
        self.print_pass_fail(10, 10, l)

    def test_case4(self):
        ## Two element
        l = [10, 8]  # a list containing 0 - 9
        self.print_pass_fail(8, 10, l)

    def test_case5(self):
        ## Min and Max on same side
        l = [10, 0, 3, 4, 5, 5, 2, 2]  # a list containing 0 - 9
        self.print_pass_fail(0, 10, l)

    def test_case6(self):
        ## All elements are the same
        l = [2,2, 2, 2, 2, 2]  # a list containing 0 - 9
        self.print_pass_fail(2, 2, l)

if __name__ == '__main__':
    unittest.main()