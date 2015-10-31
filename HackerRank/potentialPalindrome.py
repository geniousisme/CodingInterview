class Solution(object):
    def is_potential_palindrome(self, string):
        string = ''.join(sorted(string))
        start_pos = last_pos = 0
        odd_count = 0
        while last_pos < len(string):
            if string[start_pos] == stxring[last_pos]:
                last_pos += 1
            else:
                if (last_pos - start_pos) % 2 == 1:
                    odd_count += 1 # since we only can have one char with odd numbers length, use this count to track
                    if odd_count > 1: # once there is another one exceeding the number, return False
                        return False
                    else:
                        start_pos = last_pos
                else:
                    start_pos = last_pos
        # since the last part (aka, "aaabbccc", the 'ccc' part) we have no one the interrupt,
        # we need to check the last part string length
        if (last_pos - start_pos) % 2 == 1: # check the last part of string
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    # print s.is_potential_palindrome("aaaab")
    # print s.is_potential_palindrome("aaa")
    print s.is_potential_palindrome("accbb")
    print s.is_potential_palindrome("accbbdd")
    # print s.is_potential_palindrome("a")
    # print s.is_potential_palindrome("cccc")



