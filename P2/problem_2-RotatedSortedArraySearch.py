import unittest


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return _rotated_array_search(input_list, number, 0, len(input_list)-1)

def _rotated_array_search(input_list, number, left, right):
    """
    Find the index by searching in a rotated sorted array - modified binary search

    Args:
       input_list(array): Input array to search
       number(int): Target to search
       left(int): left index of input_list to search
       right(int): right index of input_list to search
    Returns:
       int: Index or -1
    """
    if left > right:
        return -1
    middle = left + (right - left) // 2
    if input_list[middle] == number:
        if middle == 0 or input_list[middle-1] != input_list[middle]: # Handling duplicates anyway even though problem states no duplicates
            return middle
    if input_list[left] < input_list[middle]: # We know there's no rotation on left side of input_list
        if input_list[left] <= number <= input_list[middle]: # Since the target is within range of sorted left, search only on left
            return _rotated_array_search(input_list, number, left, middle-1)
        else: # We know target doesn't lie in left range, so maybe its on the right side where rotation maybe present
            return _rotated_array_search(input_list, number, middle+1, right)
    elif input_list[middle] < input_list[right]: # We know there's no rotation on the right side but rotation did exist on left side
        if input_list[middle] <= number <= input_list[right]: # Since the target is within range of sorted right, search only on right
            return _rotated_array_search(input_list, number, middle+1, right)
        else: # We know target doesn't lie in right range, so maybe its on the rotated left side
            return _rotated_array_search(input_list, number, left, middle-1)
    else: # Will only enter here when duplicates are present and so we can't determine which side rotation is on by comparing extremes and middle
        # Search on both sides - first left, if not found on left then right
        left_index = _rotated_array_search(input_list, number, left, middle-1) # Search Left
        if left_index != -1:
            return left_index
        return _rotated_array_search(input_list, number, middle+1, right) # Search Right



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

class TestRotatedArraySearch(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

    def test_case2(self):
        test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

    def test_case3(self):
        test_function([[6, 7, 8, 1, 2, 3, 4], 8])

    def test_case4(self):
        test_function([[6, 7, 8, 1, 2, 3, 4], 1])

    def test_case5(self):
        test_function([[6, 7, 8, 1, 2, 3, 4], 10])

    def test_case6(self):
        test_function([[], 10])

if __name__ == '__main__':
    unittest.main()

"""
Expected output-

****test_case1****
Pass
.

****test_case2****
Pass
.

****test_case3****
Pass
.

****test_case4****
Pass
.

****test_case5****
Pass
.

****test_case6****
Pass
.
----------------------------------------------------------------------
Ran 6 tests in 0.005s

OK

"""