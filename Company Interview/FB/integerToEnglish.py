# Convert a non-negative integer to its english words representation.
# Given input is guaranteed to be less than 2^31 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# Hint:
#
# 1. Did you see a pattern in dividing the number into chunk of words?
# For example, 123 and 123000.
#
# 2. Group the number by thousands (3 digits). You can write a helper
# function that takes a number less than 1000 and convert just that chunk to words.
#
# 3. There are many edge cases. What are some good test cases?
# Does your code work with input such as 0? Or 1000010?
# (middle chunk is zero and should not be printed out)
#

class Solution(object):
    '''
    Time:  O(logn)
    Space: O(1)
    '''
    def __init__(self):
        self.lookup =  {
                          0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four",
                          5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                          10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
                          14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                          17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                          20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
                          60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
                        }
        self.unit = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return self.lookup[num]
        res = []; i = 0
        while num:
            curr = num % 1000
            if curr:
                res.append(self.three_digit(curr, self.unit[i]))
            num //= 1000
            i += 1
        return ' '.join(res[::-1])

    def three_digit(self, num, unit):
        res = []
        if num // 100:
            res.append(self.lookup[num // 100] + ' ' + "Hundred")
        if num % 100:
            res.append(self.two_digit(num % 100))
        if unit:
            res.append(unit)
        return ' '.join(res)

    def two_digit(self, num):
        if num in self.lookup:
            return self.lookup[num]
        return self.lookup[(num / 10) * 10] + ' ' + self.lookup[num % 10]

if __name__ == "__main__":
    s = Solution()
    print s.numberToWords(12345)
    print s.numberToWords(12)
    print s.numberToWords(3521)
    print s.numberToWords(99)



