class Solution(object):
    def __init__(self):
        self.lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    def findStrobogrammatic(self, n):
        return self.find_strobogram_helper(n, n)

    def find_strobogram_helper(self, n, k):
        if k == 0:
            return ['']
        if k == 1:
            return ['0', '1', '8']
        res = []
        for num in self.find_strobogram_helper(n, k - 2):
            for key, val in self.lookup.items():
                if num != '0' or n != k:
                    res.append(key + num + val)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.findStrobogrammatic(2)
    print s.findStrobogrammatic(3)
