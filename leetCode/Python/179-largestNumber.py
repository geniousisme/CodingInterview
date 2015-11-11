class Solution1:
    # @param {integer[]} nums
    # @return {string}
    # Chris:TODO:: worship the following algo and learn it forever!
    # cmp: please read this article: https://docs.python.org/2/library/functions.html#sorted
    def largestNumber(self, nums):
        new_nums = sorted([str(num) for num in nums], cmp=self.compare)
        num_str  = ''.join(new_nums).lstrip('0')
        return num_str or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a] # should put 1 first, but it can reverse the string with the order we want

class Solution(object):
    def largestNumber(self, nums):
        num_str_list = [str(num) for num in nums]
        sorted_num_str_list = sorted(num_str_list, cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(sorted_num_str_list).lstrip('0') or '0'

if __name__ == '__main__':
   s = Solution()
   print s.largestNumber([3, 30, 34, 5, 9])
