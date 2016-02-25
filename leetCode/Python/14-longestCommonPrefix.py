
# Time:  O(n)
# Space: O(1)
#
# Write a function to find the longest common prefix string amongst an array of strings.
#

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longest = strs[0]
        for string in strs[1:]:
            i = 0
            while i < len(string) and i < len(longest) and string[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest

class Solution1:
    # @return a string
    def longestCommonPrefix(self, strs):
        common_prefix = ""; idx = 0
        if len(strs) == 0: return common_prefix
        while True:
            current_char = ""
            for string in strs:
                if idx < len(string): # check if out of rang already
                    if current_char == "": # no current string yet
                        current_char = string[idx] # assign
                    else: # hv current char to compare, we need to check
                        if current_char != string[idx]: 
                            return common_prefix
                else: # out of range for string, need to return
                    return common_prefix
            common_prefix += current_char #all strings hv char, add to prefix
            idx += 1

def main():
    s = Solution()
    strs = []
    print s.longestCommonPrefix(strs)

if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)