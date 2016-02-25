# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network
# and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);
# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Note:
# The string may contain any possible characters out of 256 valid ascii characters.
# Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states.
# Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods.
# You should implement your own encode/decode algorithm.

class Codec(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def encode(self, strings):
        encode_strs = []
        for string in strings:
            encode_strs.append("%0*x" % (8, len(string)) + string)
        return "".join(encode_strs)

    def decode(self, encode_str):
        idx = 0
        strings = []
        while idx < len(encode_str):
            length = int(encode_str[idx:idx + 8], 16)
            strings.append(encode_str[idx + 8:idx + 8 + length])
            idx += 8 + length
        return strings

if __name__ == "__main__":
    c = Codec()
    strings = ["123", "abc", "", "$$%^&*()@"]
    print c.encode(strings)
    print c.decode(c.encode(strings))
