import unittest

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, rootHandler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(rootHandler)

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr = self.root
        for part in parts[:-1]:
            curr.insert(part)
            curr = curr.children[part]
        curr.insert(parts[-1], handler)


    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root
        for part in parts:
            if part not in curr.children:
                # Break out whenever a route is not present in trie
                return None
            curr = curr.children[part]
        # Return the last at which prefix ended
        return curr.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = dict()

    def insert(self, part, handler=None):
        # Insert the node as before
        if part not in self.children:
            self.children[part] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, rootHandler='root handler', notFoundHandler='not found handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routerTrie = RouteTrie(rootHandler)
        self.notFoundHandler = notFoundHandler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts = self.split_path(path)
        self.routerTrie.insert(parts, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        parts = self.split_path(path)
        handler = self.routerTrie.find(parts)
        if not handler:
            return self.notFoundHandler
        return handler

    @staticmethod
    def split_path(path):
    # you need to split the path into parts for
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
        parts = path.split('/')
        if parts[0] == '':
            parts = parts[1:]
        if len(parts) == 0:
            return []
        if parts[-1] == '':
            parts = parts[:-1]
        return parts

# Here are some test cases and expected outputs you can use to test your implementation
class TestHTTPRouter(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))
        self.router = Router("root handler", "not found handler")

    def test_case1(self):
        # create the router and add a route
        # remove the 'not found handler' if you did not implement this
        self.router.add_handler("/home/about", "about handler")  # add a route

        # some lookups with the expected output
        print(self.router.lookup("/"))  # should print 'root handler'
        print(self.router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
        print(self.router.lookup("/home/about"))  # should print 'about handler'
        print(self.router.lookup(
            "/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
        print(self.router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
        print(self.router.lookup(""))  # should print 'root handler'


    def test_case3(self):
        # Test case 2 - Empty Router
        # create the router and add a route

        # some lookups with the expected output
        print(self.router.lookup("/home/about"))  # should print 'not found handler'
        print(self.router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


if __name__ == '__main__':
    unittest.main()
