# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"


class Solution(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def simplifyPath(self, path):
        stack = []; tokens = path.split('/')
        for token in tokens:
            if token == ".."and stack:
                stack.pop()
            if token != "." and token != ".." and token: # notice since token might be "", and we dont want that.
                stack.append(token)
        return '/' + '/'.join(stack)

