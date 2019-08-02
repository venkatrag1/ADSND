import unittest

def _merge_descending(input_list, left, middle, right):
    """
    Merge subroutine to merge two sorted lists

    Args:
       input_list(list): Input List with two sorted halves
       left(int): Start Index
       middle(int): Index where the list is split into two sorted lists
       right(int): End Index
    Returns:
       None
    """
    temp_arr = [None for _ in range(right - left + 1)]
    l = left
    r = middle + 1
    k = 0
    while l <= middle and r <= right:
        # Always push the greater of the element from the two lists
        if input_list[l] > input_list[r]:
            temp_arr[k] = input_list[l]
            l += 1
        else:
            temp_arr[k] = input_list[r]
            r += 1
        k += 1
    while l <= middle:
        # Copy left over in left array
        temp_arr[k] = input_list[l]
        k += 1
        l += 1
    while r <= right:
        # Copy left over in right array
        temp_arr[k] = input_list[r]
        k += 1
        r += 1
    for k in range(left, right+1):
        # Copy back from temp list into original
        input_list[k] = temp_arr[k - left]


def _merge_sort(input_list, left, right):
    """
    Merge sort that uses a descending order merge

    Args:
       input_list(list): Input List
       left(int): Left index
       right(int): Right index
    Returns:
       None
    """
    if left < right:
        middle = left + (right - left) // 2
        _merge_sort(input_list, left, middle)
        _merge_sort(input_list, middle+1, right)
        _merge_descending(input_list, left, middle, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    _merge_sort(input_list, 0, len(input_list) - 1)  # Sort numbers in-place
    num_A, num_B = 0, 0
    for idx, num in enumerate(input_list):
        # Copy even and odd index elements into alternate accumulators
        if idx % 2 == 0:
            num_A = 10 * num_A + num  # Push current number by one decimal place and add new element in ones place
        else:
            num_B = 10 * num_B + num
    return [num_A, num_B]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

class TestRearrangeDigits(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        test_function([[1, 2, 3, 4, 5], [542, 31]])

    def test_case2(self):
        test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    def test_case3(self):
        test_function([[], [0, 0]])

    def test_case4(self):
        test_function([[4, 9], [9, 4]])

    def test_case5(self):
        test_function([[9], [9, 0]])


if __name__ == '__main__':
    unittest.main()


"""
Expected Solution- 


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
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK

"""

