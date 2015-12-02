class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class RecursiveSolution(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def inorderTraversal(self, root):
        def inorder_helper(root):
            if root:
                inorder_helper(root.left)
                res.append(root.val)
                inorder_helper(root.right)
            return
        res = []
        inorder_helper(root)
        return res

    def preorderTraversal(self, root):
        def preorder_helper(root):
            if root:
                res.append(root.val)
                preorder_helper(root.left)
                preorder_helper(root.right)
            return
        res = []
        preorder_helper(root)
        return res

    def postorderTraversal(self, root):
        def postorder_helper(root):
            if root:
                postorder_helper(root.left)
                postorder_helper(root.right)
                res.append(root.val)
            return
        res = []
        postorder_helper(root)
        return res

class IterativeSolution(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def inorderTraversal(self, root):
        stack = []; res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                res.append(root.val)
                top = stack.pop()
                root = top.right
        return res

    def preorderTraversal(self, root):
        stack = []; res = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                top = stack.pop()
                root = top.right
        return res

    def postorderTraversal(self, root):
        stack = []; res = []; last_traversed = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                parent = stack[-1]
                if parent.right in (None, last_traversed):
                    res.append(parent.val)
                    last_traversed = stack.pop()
                else:
                    root = parent.right
        return res

class MorrisSolution(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def inorderTraversal(self, root):
        curr = root; res = []; succ = None
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                succ = curr.left
                while succ.right and succ.right != curr:
                    succ = succ.right
                if succ.right is None:
                    succ.right = curr
                    curr = curr.left
                else:
                    res.append(curr.val)
                    succ.right = None
                    curr = curr.right
        return res

    def preorderTraversal(self, root):
        curr = root; res = []; succ = None # succ means successor, succeed from curr
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                succ = curr.left
                while succ.right and succ.right != curr:
                    succ = succ.right
                if succ.right is None:
                    res.append(curr.val)
                    succ.right = curr
                    curr = curr.left
                else:
                    succ.right = None
                    curr = curr.right
        return res

    def postorderTraversal(self, root):
        dummy = TreeNode(0)
        dummy.left = root
        result, cur = [], dummy
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur = cur.right
        return result

    def traceBack(self, frm, to):
        result, cur = [], frm
        while cur is not to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result



