# Time:  O(n)
# Space: O(h)

# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can
# be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# For example, you may serialize the following tree
#
#     1
#   / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
# a binary tree. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    Time:  O(n)
    Space: O(h)
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_helper(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                serialize_helper(node.left)
                serialize_helper(node.right)
        vals = []
        serialize_helper(root)
        return ' '.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_helper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(val)
                node.left  = deserialize_helper()
                node.right = deserialize_helper()
                return node

        def split_data(data, sep):
            sepsize = len(sep)
            start   = 0
            while True:
                idx = data.find(sep, start)
                if idx == -1:
                    yield data[start:]
                    return
                yield data[start:idx]
                start = idx + sepsize

        vals = iter(split_data(data, ' '))
        return deserialize_helper()

