class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        lower_idx = 0
        for i in xrange(len(chars)):
            if 96 < ord(chars[i]) < 123:
                chars[i], chars[lower_idx] = chars[lower_idx], chars[i]
                lower_idx += 1

if __name__ == "__main__":
    s = Solution()
    chars = "abAcD"
    print s.sortLetters("abAcD")
    print chars

