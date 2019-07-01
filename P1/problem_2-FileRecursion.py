import unittest
import os
from pprint import pprint

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_list = list()  # empty list to hold results
    visited = set()  # Set to hold realpath of all visited subdirectories - this is needed for softlinks that could cause infinite loop
    _find_files(suffix, path, path_list, visited)  # Recursive Helper
    return path_list


def _find_files(suffix, path, path_list, visited):
    candidates = os.listdir(path)
    for candidate in candidates:
        # Form full-path by merging candidate name with base-path, converting any softlinks and relpath to absolute path
        candidate = os.path.join(os.path.realpath(path), candidate)
        if os.path.isfile(candidate):
            if candidate.endswith(suffix):  # Check for match with given suffix
                path_list.append(candidate)
        elif os.path.isdir(candidate):
            # recurse on sub-directories if not already visited (only applicable to circular softlinks)
            if candidate not in visited:
                visited.add(candidate)
                _find_files(suffix, candidate, path_list, visited)

class TestFileRecursion(unittest.TestCase):
    BASEPATH = '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/'

    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        pprint(find_files('.c', os.path.join(self.BASEPATH, 'testdir')))
        """
        Returns
['/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir/subdir3/subsubdir1/b.c',
 '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir/t1.c',
 '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir/subdir5/a.c',
 '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir/subdir1/a.c']

        """

    #@unittest.skip('')
    def test_case2_softlink_inf_loop(self):
        pprint(find_files('.c', os.path.join(self.BASEPATH, 'testdir-2')))
        """
        Returns
['/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir-2/subdir3/subsubdir1/b.c',
 '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir-2/t1.c',
 '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir-2/subdir5/a.c',
 '/vagrant/GitHub/ADSND/P1/data/problem_2-FileRecursion/testdir-2/subdir1/a.c']

        """

    def test_case3_no_result(self):
        pprint(find_files('.c', os.path.join(self.BASEPATH, 'testdir-3')))
        # Returns []

if __name__ == '__main__':
    unittest.main()