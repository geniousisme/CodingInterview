class Solution:
    # @param {string} s
    # @return {integer}
    def juinorLengthOfLongestSubstringTwoDistinct(self, s):
        two_word_dict     = {}
        distinct_count    = 0
        max_len = tmp_len = 0
        if s:
           for i in xrange(len(s)):
               if two_word_dict.get(s[i], False):
                  tmp_len += 1
                  # diff_idx = i
               else:
                  distinct_count += 1
                  if distinct_count > 2:
                     two_word_dict = {}
                     two_word_dict[s[i]] = True
                     two_word_dict[s[i - 1]] = True
                     j = i - 1
                     while j > 0 and s[j] == s[j - 1]:
                           j -= 1
                     tmp_len = 1 + i - j
                  else:
                     two_word_dict[s[i]] = True
                     tmp_len += 1
               max_len = max(max_len, tmp_len)
        return max_len

    def lengthOfLongestSubstringTwoDistinct(self, s):
        '''
        TC: O(N)
        SC: O(1)
        use three pointer to solve it
        prev_two_chars_ptr: to store the previous two chars pointer
        two_chars_start: where the two chars start position
        two_chars_ptr: curr idx for the nums
        '''
        prev_two_chars_ptr = -1
        two_chars_start = 0
        max_len = 0
        for two_chars_ptr in xrange(1, len(s)):
            if s[two_chars_ptr - 1] == s[two_chars_ptr]:
                continue
            else:
                if s[two_chars_ptr] != s[prev_two_chars_ptr]:
                    max_len = max(max_len, two_chars_ptr - two_chars_start)
                    two_chars_start = prev_two_chars_ptr + 1
                prev_two_chars_ptr = two_chars_ptr - 1
        return max(max_len, len(s) - two_chars_start)

if __name__ == '__main__':
   s = Solution()
   print s.lengthOfLongestSubstringTwoDistinct('eceba')
   print s.lengthOfLongestSubstringTwoDistinct('eecebaaaaa')
   print s.lengthOfLongestSubstringTwoDistinct('ee')
   print s.lengthOfLongestSubstringTwoDistinct("abaccc")
   print s.lengthOfLongestSubstringTwoDistinct('ccaabbb')




