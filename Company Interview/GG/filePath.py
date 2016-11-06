import re

# class Solution(object):
# 	def file_distance(self, file_path_str):
# 		file_paths = file_path_str.split("\n")
# 		curr_layer = curr_length = final_length = 0
# 		stack = []
# 		final_length = 0
# 		for file_path in file_paths:
# 			trimmed_file_path = file_path.strip()
# 			file_layer = file_path.index(trimmed_file_path)
# 			while stack and file_layer <= curr_layer:
# 				last_path = stack.pop()
# 				curr_layer -= 1
# 				curr_length -= len(last_path)
# 			curr_layer = file_layer
# 			stack.append("/" + trimmed_file_path)
# 			curr_length += len(stack[-1])
# 			if self.is_image(trimmed_file_path):
# 				final_length += curr_length
# 		return final_length


# 	def is_image(self, filename):
# 		result = re.match('([-\w]+\.(?:jpg|jpeg|gif|png))', filename)
# 		return result != None

def is_image(file_path):
    result = re.match('([-\w]+\.(?:jpg|jpeg|gif|png))', file_path)
    return result != None

def solution(file_path_str):
    # write your code in Python 2.7
    file_paths = file_path_str.split("\n")
    curr_layer = curr_length = final_length = 0
    stack = []
    for file_path in file_paths:
        trimmed_file_path = file_path.strip()
        file_layer = file_path.index(trimmed_file_path)
        while stack and file_layer <= curr_layer:
            last_path = stack.pop()
            curr_layer -= 1
            curr_length -= len(last_path)
        curr_layer = file_layer
        stack.append("/" + trimmed_file_path)
        curr_length += len(stack[-1])
        if is_image(trimmed_file_path):
            final_length += curr_length
    return final_length

if __name__ == "__main__":
	# s = Solution()
	print solution("dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif")
