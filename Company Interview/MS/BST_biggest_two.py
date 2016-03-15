class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def find_biggest_two(self, root):
		stack = []; res = []
		count = 0
		while stack or root:
			if root:
				stack.append(root)
				root = root.right
			else:
				top = stack.pop()
				res.append(top.val)
				count += 1
				if count == 2:
					return res
				root = top.left
		return res

if __name__ == "__main__":
	s = Solution()
	t7 = TreeNode(7)

	t7.left = TreeNode(3)
	t7.left.left = TreeNode(1)
	t7.left.right = TreeNode(4)

	t7.right = TreeNode(9)
	t7.right.left = TreeNode(5)
	t7.right.right = TreeNode(10)

	print s.find_biggest_two(t7)