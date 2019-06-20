import sys
import heapq

class HuffmanData(object):
    def __init__(self, c):
        self.c = c
        self.code = None

class HuffmanNode(object):
    def __init__(self, freq, data=None):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def is_internal(self):
        return self.data == None

    def set_code(self, code):
        if self.data is None:
            raise ValueError('Cannot set code for internal node')
        self.data.code = ''.join(code)

class HuffmanTree(object):
    def __init__(self, freq, data=None):
        self.root = HuffmanNode(freq, data)

    def __lt__(self, other):
        return self.root < other.root

    def assign_codes(self):
        self._assign_codes(self.root)

    @staticmethod
    def _assign_codes(node, code=[]):
        if not node.is_internal():
            node.set_code(code)
            return
        if node.left:
            code.append('0')
            HuffmanTree._assign_codes(node.left, code)
            code.pop()
        if node.right:
            code.append('1')
            HuffmanTree._assign_codes(node.right, code)
            code.pop()

    def get_code_dict(self):
        code_dict = dict()
        self._get_code_dict(self.root, code_dict)
        return code_dict

    @staticmethod
    def _get_code_dict(node, code_dict):
        if not node.is_internal():
            code_dict[node.data.c] = node.data.code
        if node.left:
            HuffmanTree._get_code_dict(node.left, code_dict)
        if node.right:
            HuffmanTree._get_code_dict(node.right, code_dict)

def build_freq_dict(data):
    freq_dict = dict()
    for c in data:
        freq_dict[c] = freq_dict.get(c, 0) + 1
    return freq_dict

def huffman_encoding(data):
    if len(data) == 0:
        return
    freq_dict = build_freq_dict(data)
    h = []
    for c, freq in freq_dict.items():
        heapq.heappush(h, HuffmanTree(freq, HuffmanData(c)))
    while len(h) > 1:
        tree1 = heapq.heappop(h)
        tree2 = heapq.heappop(h)
        new_freq = tree1.root.freq + tree2.root.freq
        new_tree = HuffmanTree(new_freq)
        new_tree.root.left = tree1.root
        new_tree.root.right = tree2.root
        heapq.heappush(h, new_tree)
    final_tree = heapq.heappop(h)
    final_tree.assign_codes()
    code_dict = final_tree.get_code_dict()
    encoded_data = [code_dict[c] for c in data]
    return ''.join(encoded_data), final_tree

def huffman_decoding(data, tree):
    curr_node = tree.root
    decoded_data = []
    for digit in data:
        if digit == '0':
            curr_node = curr_node.left
        if digit == '1':
            curr_node = curr_node.right
        if not curr_node.is_internal():
            decoded_data.append(curr_node.data.c)
            curr_node = tree.root
    return ''.join(decoded_data)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))