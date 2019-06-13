import os

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
    path_list = list()
    _find_files(suffix, path, path_list)
    return path_list


def _find_files(suffix, path, path_list):
    candidates = os.listdir(path)
    for candidate in candidates:
        candidate = os.path.join(path, candidate)
        if os.path.isfile(candidate):
            if candidate.endswith(suffix):
                path_list.append(candidate)
            # Check suffix endswith
        elif os.path.isdir(candidate):
            _find_files(suffix, candidate, path_list)


print(find_files('.c', 'testdir'))
"""
## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))
"""