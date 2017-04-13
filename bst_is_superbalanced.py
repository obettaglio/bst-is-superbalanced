class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        # return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        # return self.right


def is_superbalanced(node, curr_depth=0, min_depth=None, max_depth=None):
    """Find all possible combinations of coins with given denominations
    that add up to the given monetary amount in cents.

    Test cases:


            10
        7           14
    5       8    11     16
                   13

    >>> root = BinaryTreeNode(10)

    >>> root.insert_left(7)
    >>> root.left.insert_left(5)
    >>> root.left.insert_right(8)
    >>> root.insert_right(14)
    >>> root.right.insert_left(11)
    >>> root.right.left.insert_right(13)
    >>> root.right.insert_right(16)

    >>> is_superbalanced(root)
    True



            10
        7             14
    5       8    11         16
                    13
                  12

    >>> root2 = BinaryTreeNode(10)

    >>> root2.insert_left(7)
    >>> root2.left.insert_left(5)
    >>> root2.left.insert_right(8)
    >>> root2.insert_right(14)
    >>> root2.right.insert_left(11)
    >>> root2.right.left.insert_right(13)
    >>> root2.right.left.right.insert_left(12)
    >>> root2.right.insert_right(16)

    >>> is_superbalanced(root2)
    False



                10
            7             14
        5       8    11         16
    3
      4

    >>> root3 = BinaryTreeNode(10)

    >>> root3.insert_left(7)
    >>> root3.left.insert_left(5)
    >>> root3.left.left.insert_left(3)
    >>> root3.left.left.left.insert_right(4)
    >>> root3.left.insert_right(8)
    >>> root3.insert_right(14)
    >>> root3.right.insert_left(11)
    >>> root3.right.insert_right(16)

    >>> is_superbalanced(root3)
    False

    """

    if (not node.left) and (not node.right):
        if (min_depth is None) or (curr_depth < min_depth):
            min_depth = curr_depth
        if (max_depth is None) or (curr_depth > max_depth):
            max_depth = curr_depth
        if (max_depth - min_depth > 1):
            return (False, min_depth, max_depth)
        return (True, min_depth, max_depth)

    if node.left:
        left_check, min_depth, max_depth = is_superbalanced(node.left, curr_depth+1, min_depth, max_depth)
        if not left_check:
            if curr_depth != 0:
                return (False, min_depth, max_depth)
            return False

    if node.right:
        right_check, min_depth, max_depth = is_superbalanced(node.right, curr_depth+1, min_depth, max_depth)
        if not right_check:
            if curr_depth != 0:
                return (False, min_depth, max_depth)
            return False

    if curr_depth != 0:
        return (True, min_depth, max_depth)

    return True


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
