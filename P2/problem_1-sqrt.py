import unittest

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        print("Since, the number is a negative integer, the square root value returned is imaginary and should be considered multiplied by i, that is sqrt(-1)")
        number = - number
    left = 0
    right = number

    floor_sqrt = 0

    while left <= right:
        middle = left + (right - left) // 2
        square = middle * middle
        # print(left, middle, right)
        if square == number:
            return middle
        elif square < number:
            floor_sqrt = middle  # Remember the lowest value encountered before we exceeded square
            left = middle + 1
        elif square > number:
            right = middle - 1
    return floor_sqrt

class TestSqrt(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def print_pass_fail(self, expected_sqrt, number):
        print ("Pass" if (expected_sqrt == sqrt(number)) else "Fail")

    def test_case1(self):
        self.print_pass_fail(3, 9)

    def test_case2(self):
        self.print_pass_fail(0, 0)

    def test_case3(self):
        self.print_pass_fail(4, 16)

    def test_case4(self):
        self.print_pass_fail(1, 1)

    def test_case5(self):
        self.print_pass_fail(5, 27)

    def test_case6(self):
        self.print_pass_fail(4, 24)

    def test_case7(self):
        self.print_pass_fail(5, -25)

    def test_case8(self):
        self.print_pass_fail(2, 5)

if __name__ == '__main__':
    unittest.main()