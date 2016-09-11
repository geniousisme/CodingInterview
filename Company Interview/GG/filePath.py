import re

class Solution(object):
	def file_distance(self, file_path_str):
		file_paths = file_path_str.split("\n")
		curr_layer = curr_length = final_length = 0
		stack = []
		final_length = 0
		for file_path in file_paths:
			trimmed_file_path = file_path.strip()
			file_layer = file_path.index(trimmed_file_path)
			while stack != None and file_layer <= curr_layer:
				last_path = stack.pop()
				file_layer -= 1
				curr_length -= len(last_path)
			curr_layer = file_layer
			stack.append(file_path)
			curr_length += len(stack[-1]) + 1
			if self.is_image(file_path):
				final_length += curr_length
		return final_length


	def is_image(self, filename):
		result = re.match('([-\w]+\.(?:jpg|jpeg|gif|png))', filename)
		return result != None

if __name__ == "__main__":
	s = Solution()
	s.file_paths()