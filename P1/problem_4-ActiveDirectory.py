#Active Directory
#In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
import unittest

class Group(object):
    """
    Description: Group obj holding a list of sub-groups and sub-users
    """
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    # Getter/ Setter methods for Group attributes
    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def _is_user_in_group(user, group, visited):
    """
    Recursive helper for is_user_in_group. Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
      visited(set): set of visited groups
    """
    if not isinstance(user, str) or not isinstance(group, Group):
        return False  # Invalid input
    for current_user in group.get_users():
        if user == current_user:
            return True
    for sub_group in group.get_groups():
        if sub_group not in visited:
            visited.add(sub_group)
            return _is_user_in_group(user, sub_group, visited)
    return False

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    visited = set()
    return _is_user_in_group(user, group, visited)

class TestActiveDirectory(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def test_case1(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)
        print(is_user_in_group("sub_child_user", parent))  # Returns True

    def test_case2_not_in_group(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user_2"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)
        print(is_user_in_group("sub_child_user", parent))  # Returns False

    def test_case3_empty_group(self):
        parent = Group("parent")
        print(is_user_in_group("child", parent))  # Returns False


if __name__ == '__main__':
    unittest.main()