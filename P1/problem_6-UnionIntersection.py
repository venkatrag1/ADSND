class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value


class LinkedList:
    def __init__(self):
        self.head = None
        self._sorted = False

    @classmethod
    def from_head(cls, head):
        # Alternative constructor to wrap an already build list into Linked List class using the head
        new_ll = cls()
        new_ll.head = head
        new_ll._sorted = False
        return new_ll

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        self._sorted = False  # If adding new node, reset the sorted flag

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next: # Traverse to end of llist
            node = node.next

        node.next = Node(value) # Add at end

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    @staticmethod
    def _front_back_split(head):
        slow = head
        fast = head
        # Get slow node to one node before the mid-point, so move fast pointer first
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
        # Split into two llists using slow.next as the second llist head and disconnect the first llist after slow
        front = head
        back = slow.next
        slow.next = None
        return front, back


    @staticmethod
    def get_nodes_ascending(left_head, right_head):
        # Generator to yield the lower of the values and none for the other value, when
        # traverse the two llist side by side. If both values are same, yield both
        # left and right nodes.
        left_curr = left_head
        right_curr = right_head
        while left_curr and right_curr:
            if left_curr < right_curr:
                left_next = left_curr.next
                yield (left_curr, None)
                left_curr = left_next
            elif left_curr > right_curr:
                right_next = right_curr.next
                yield (None, right_curr)
                right_curr = right_next
            else:
                 # Save reference to next- needed when yielding from both since we will manipulate left next to point to right before returning incase of merge operation
                left_next, right_next = left_curr.next, right_curr.next
                yield (left_curr, right_curr)
                left_curr, right_curr = left_next, right_next
        while left_curr:
            # Yield the remaining in left llist if right llist is empty
            left_next = left_curr.next
            yield (left_curr, None)
            left_curr = left_next
        while right_curr:
            # Yield the remaining in right llist if left llist is empty
            right_next = right_curr.next
            yield (None, right_curr)
            right_curr = right_next

    @staticmethod
    def _sorted_merge(front, back):
        # Merge two sorted llist
        head = None
        curr = None
        for left_node, right_node in LinkedList.get_nodes_ascending(front, back):
            if left_node:
                if not head:
                    head = left_node
                else:
                    curr.next = left_node
                curr = left_node
            if right_node:
                if not head:
                    head = right_node
                else:
                    curr.next = right_node
                curr = right_node
        return head

    @staticmethod
    def _merge_sort(head):
        if head is not None and head.next is not None:
            front, back = LinkedList._front_back_split(head)
            front = LinkedList._merge_sort(front)
            back = LinkedList._merge_sort(back)
            head = LinkedList._sorted_merge(front, back)
        return head

    def sort(self):
        if not self._sorted and self.head and self.head.next:
            new_head = self._merge_sort(self.head)
            self.head = new_head
            self._sorted = True
        return self


def union(llist_1, llist_2):
    # Your Solution Here
    llist_union = LinkedList()
    llist_1 = llist_1.sort()
    llist_2 = llist_2.sort()
    for left_node, right_node in LinkedList.get_nodes_ascending(llist_1.head, llist_2.head):
        if left_node: # If present in left or in both lists pick from left
            llist_union.append(left_node.value)
        elif right_node: # Pick from right if only present in right
            llist_union.append(right_node.value)
    return llist_union

def intersection(llist_1, llist_2):
    # Your Solution Here
    llist_intersection = LinkedList()
    llist_1 = llist_1.sort()
    llist_2 = llist_2.sort()
    for left_node, right_node in LinkedList.get_nodes_ascending(llist_1.head, llist_2.head):
        if left_node and right_node: # Only add if present in both ll
            llist_intersection.append(left_node.value)
    return llist_intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
