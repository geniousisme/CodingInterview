class Solution(object):
    def binaryPlusOne(self, num):
        return self.add(num, 1)

    def add(self, a, b): # recursive
        if b == 0:
            return a
        sum = a ^ b
        carry = (a & b) << 1
        return self.add(sum, carry)

    def add(self, a, b): # iterative
        while b:
            sum = a ^ b
            carry = (a & b) << 1
            a = sum
            b = carry
        return a

if __name__ == "__main__":
    s = Solution()
    print s.binaryPlusOne(12)
    print s.binaryPlusOne(99)
    print s.binaryPlusOne(0)

