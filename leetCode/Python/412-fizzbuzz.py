class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        for x in xrange(1, n + 1):
            out_num_str = str(x)

            if x % 15 == 0:
                out_num_str = "FizzBuzz"

            elif x % 5 == 0:
                out_num_str = "Buzz"

            elif x % 3 == 0:
                out_num_str = "Fizz"

            ans.append(out_num_str)
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.fizzBuzz(15)