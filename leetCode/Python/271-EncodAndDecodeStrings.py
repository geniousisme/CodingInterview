class Codec(object):
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
