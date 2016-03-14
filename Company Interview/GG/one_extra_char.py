
# abcd
# abxcd
# abcdx
# x

# abcd, abcd; abcd, abce => None

def one_extra_char(str1, str2):
    if len(str1)> len(str2):
        return one_extra_char(str2, str1)
    for i in xrange(len(str1)):
        if str1[i] != str2[i]:
            return str2[i]
    return str2[-1]

# TC: O(N), N = str1 length
# SC: O(1)

# test case1: abcd, xabcd
# test case2: abcd, abxcd
# test case3: abcd, abcdx
# test case4: abcdx, abcd
# edge case: “”, “x”

# dcab
# dxbca
# time complexity: sorted(str) => abcd, abcdx => original
# algo O(n) -> O(nlogn), space O(1)

# space complexity: dictionary => iterate str1 => iter str2 => delete str2
# algo O(n), space O(n)

def one_extra_char_with_dict(str1, str2):
    if len(str1) > len(str2):
        return one_extra_char_with_dict(str2, str1)
    dict = {char: i for char in str2} # {d:0, x:1, b:2, c:3, a:4}
    for char in str2:
        if dict.get(char) is not None:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in str1:
        if dict.get(char) is not None: # {x:1, b:2, c:3, a:4} => {x:1}
            dict[char] -= 1
    for key, val in dict.item():
        if dict[key] != 0:
            return key
    # aaa, aaax => first algo
    # => 1. remove duplicate at first # xxx, xxxx => x, x
    #    2. {a:count, x:[3]} #



