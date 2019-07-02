import sys
import heapq
import unittest

class HuffmanData(object):
    """
    Description: Object to store every character and its associated Huffman code
    """
    def __init__(self, c):
        self.c = c
        self.code = None

class HuffmanNode(object):
    """
    Description: Adds frequency context to huffman data and make it into a binary tree node
    """
    def __init__(self, freq, data=None):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def is_internal(self):
        """
        Description: Check if its an intermediate node of Huffman tree not associated with a single character (those nodes are at the leaf)
        Arguments:
            None

        Returns:
            Boolean indicating internal or not
        """
        return self.data is None

    def set_code(self, code):
        """
        Description: Store given list of chars as string code
        Arguments:
            code built by traversing tree

        Returns:
            None
        """
        if self.is_internal():
            raise ValueError('Cannot set code for internal node')
        self.data.code = ''.join(code)

class HuffmanTree(object):
    """
    Description: Huffman tree formed by combining Leaf nodes under an internal node
    """
    def __init__(self, freq, data=None):
        self.root = HuffmanNode(freq, data)

    def __lt__(self, other):
        return self.root < other.root

    def assign_codes(self):
        """
        Description: Recurse on this Huffman tree starting from root and assign codes to leaf nodes
        Arguments:
            None

        Returns:
            None
        """
        self._assign_codes(self.root)

    @staticmethod
    def _assign_codes(node, code=[]):
        """
        Description: Build Huffman code depending on direction of traversal in Binary Huffman Tree
        Arguments:
            None

        Returns:
            None
        """
        if not node.is_internal():
            node.set_code(code)
            return
        if node.left:
            # If you are going left in the tree, append a 0
            code.append('0')
            HuffmanTree._assign_codes(node.left, code)
            code.pop() # Backtrack
        if node.right:
            # Append 1 if going right
            code.append('1')
            HuffmanTree._assign_codes(node.right, code)
            code.pop() # Backtrack

    def get_code_dict(self):
        """
        Description: Build dictionary of character to huffman code from a given Huffman tree
        Arguments:
            None

        Returns:
            Dictionary of code character to huffman code
        """
        code_dict = dict()
        self._get_code_dict(self.root, code_dict)
        return code_dict

    @staticmethod
    def _get_code_dict(node, code_dict):
        """
        Description: Recursive helper for get_code_dict
        Arguments:
            None

        Returns:
            None
        """
        if not node.is_internal():
            code_dict[node.data.c] = node.data.code
        if node.left:
            HuffmanTree._get_code_dict(node.left, code_dict)
        if node.right:
            HuffmanTree._get_code_dict(node.right, code_dict)

def build_freq_dict(data):
    """
    Description: Count frequency of occurrence of characters in given string and build map
    Arguments:
        String data

    Returns:
        Dictionary of characters and their frequency of occurrence
    """
    freq_dict = dict()
    for c in data:
        freq_dict[c] = freq_dict.get(c, 0) + 1
    return freq_dict

def huffman_encoding(data):
    if len(data) == 0: # To satisfy int(encoded_data) return 0 with None for tree incase of empty string
        return '0', None
    freq_dict = build_freq_dict(data)
    h = []
    for c, freq in freq_dict.items():
        heapq.heappush(h, HuffmanTree(freq, HuffmanData(c))) # Push Huffman Trees made of individual character nodes into min heap
    while len(h) > 1: # Since you will always have one tree left at the end
        tree1 = heapq.heappop(h)
        tree2 = heapq.heappop(h)
        new_freq = tree1.root.freq + tree2.root.freq
        new_tree = HuffmanTree(new_freq)
        new_tree.root.left = tree1.root
        new_tree.root.right = tree2.root
        heapq.heappush(h, new_tree)
    final_tree = heapq.heappop(h) # Pop the one tree that's left
    if not final_tree.root.is_internal(): # In case of strings with just one character, root will be a HuffmanData node, so convert it to left child of a dummy tree.
        new_tree = HuffmanTree(final_tree.root.freq)
        new_tree.root.left = final_tree.root
        new_tree.root.right = None
        final_tree = new_tree
    final_tree.assign_codes()
    # Build code dict in assign codes
    code_dict = final_tree.get_code_dict()
    encoded_data = [code_dict[c] for c in data]
    return ''.join(encoded_data), final_tree

def huffman_decoding(data, tree):
    decoded_data = []
    if tree:
        curr_node = tree.root
        for digit in data:
            if digit == '0':
                curr_node = curr_node.left
            if digit == '1':
                curr_node = curr_node.right
            if not curr_node.is_internal():
                decoded_data.append(curr_node.data.c)
                curr_node = tree.root
    return ''.join(decoded_data)


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        print("\n\n****{}****".format(self._testMethodName))

    def encode_and_decode(self, a_great_sentence):

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

    #@unittest.skip('')
    def test_case1(self):
        self.encode_and_decode("The bird is the word")
        # The size of the data is: 57
        # The content of the data is: The bird is the word
        # The size of the encoded data is: 36
        # The content of the encoded data is: 1011111011000111010111110000101111110100100001110110001000111011100001
        # The size of the decoded data is: 57
        # The content of the encoded data is: The bird is the word

    def test_case2_empty_string(self):
        self.encode_and_decode('')
        # The size of the data is: 37
        # The content of the data is
        # The size of the encoded data is: 24
        # The content of the encoded data is: 0
        # The size of the decoded data is: 37
        # The content of the encoded data is:

    def test_case3_single_char(self):
        self.encode_and_decode('a')
        # The size of the data is: 38
        # The content of the data is: a
        # The size of the encoded data is: 24
        # The content of the encoded data is: 0
        # The size of the decoded data is: 38
        # The content of the encoded data is: a


if __name__ == "__main__":
    unittest.main()