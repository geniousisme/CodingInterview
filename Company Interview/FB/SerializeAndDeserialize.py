class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec(object):
    def serialize(self, root):
        def serializer(root):
            if root is None:
                res.append('#')
                return
            res.append(str(root.val))
            serializer(root.left)
            serializer(root.right)
        res = []
        serializer(root)
        return ' '.join(res)

    def deserialize(self, data):
        def deserializer():
            node_val = next(node_vals)
            if node_val == '#':
                return None
            node = TreeNode(int(node_val))
            node.left = deserializer()
            node.right = deserializer()
            return node
        node_vals = iter(data.split())
        return deserializer()


if __name__ == "__main__":
    codec = Codec()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    print codec.serialize(t1)
