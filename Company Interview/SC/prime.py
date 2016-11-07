from math import sqrt

class Solution(object):
    def is_prime(self, n):
        if n < 2:
            return False
        for factor in xrange(2, int(sqrt(n))):
            if n % factor == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        num = n / 2
        is_prime_list = [True] * n

        for i in xrange(3, n, 2):
            if i * i >= n:
                break

            if not is_prime_list[i]:
                continue

            for j in xrange(i * i, n, i * 2): # why i * 2?
                if not is_prime_list[j]:
                    continue
                # print j
                num -= 1
                is_prime_list[j] = False

        for i, val in enumerate(is_prime_list):
            print i + 1, val

        return num

if __name__ == "__main__":
    s = Solution()
    # print s.is_prime(13)
    # print s.is_prime(14)
    # print s.is_prime(2)
    # print s.is_prime(1)
    # print s.is_prime(101)
    print s.countPrimes(12)

    print s.countPrimes(13)
    # print s.countPrimes(14)




