class Solution(object):
    def __init__(self):
        self.offset = 0
        self.buff4  = ['', '', '', '']
        self.buffsize = 0

    def read(self, buffer, n):
        read_idx = 0
        eof = False
        while not eof and read_idx < n:
            # if self.buffsize == 0, then reget all the buff info
            if self.buffsize == 0:
                self.buffsize = read4(self.buff4)
                eof = self.buffsize < 4
            # check which one is the smallest one
            bytes = min(n - read_idx, self.buffsize)
            # save the info into buffer
            for i in xrange(bytes):
                buffer[i + read_idx] = self.buff4[i + self.offset]
            # reset the original settings
            self.offset = (self.offset + bytes) % 4
            self.buffsize -= bytes
            read_idx += bytes
        return read_idx