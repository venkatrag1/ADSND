import unittest

def find_next_left(input_list, left, right):
    """
    Advance left index to next non-zero value.

    Args:
       input_list(list): List to be sorted
       left(int): Left index
       right(int): Right index
    """
    while left <= right and input_list[left] == 0:
        left += 1
    return left

def find_prev_right(input_list, left, right):
    """
    Decrement right index to prev non-2 value.

    Args:
       input_list(list): List to be sorted
       left(int): Left index
       right(int): Right index
    """
    while left <= right and input_list[right] == 2:
        right -= 1
    return right

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    left = 0
    right = len(input_list) - 1
    left = find_next_left(input_list, left, right)  # Position left and right at values which need to be swapped out
    right = find_prev_right(input_list, left, right)

    if left < right:
        current = left + 1  # Since everything upto left is 0, begin iteration at left + 1
        while left <= right and current <= right:
            if input_list[current] == 1:
                current += 1  # Advance current if we see 1
            elif input_list[current] == 0:   # Push 0 to last hole on the left and copy the value in hole to current and recheck
                input_list[current], input_list[left] = input_list[left], input_list[current]
                left = find_next_left(input_list, left, right)
                if left > current:
                    current = left + 1
            elif input_list[current] == 2:  # Push 2 to last hole on the right and copy the value in hole to current and recheck
                input_list[current], input_list[right] = input_list[right], input_list[current]
                right = find_prev_right(input_list, left, right)
            else:
                raise ValueError('Invalid value {} at index {}. List can only contain 0, 1, 2'.format(input_list[current], current))
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

class TestSort012(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

    def test_case2(self):
        test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

    def test_case3(self):
        test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    def test_case4(self):
        test_function([])

    def test_case5(self):
        test_function([0, 0, 0, 0, 0, 0])

    def test_case6(self):
        test_function([1, 1, 1, 1, 1, 1])

    def test_case7(self):
        test_function([2])

if __name__ == '__main__':
    unittest.main()
