class Solution(object):
    def combinations(self, string):
        def comb_helper(comb, start):
            if len(comb) == length:
                res.append(comb)
                return
            if string[start].upper() == string[start].lower():
                comb_helper(comb + string[start], start + 1)
            else:
                for letter in (string[start].upper(), string[start].lower()):
                    comb_helper(comb + letter, start + 1)
        length = len(string); res = []
        comb_helper("", 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.combinations("")
    print s.combinations("ab7")
    print s.combinations("098765432===---__")
    # print s.combinations("RTYUIKNBG")

