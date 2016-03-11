class Solution(object):
    def read(self, buffer, n):
        buff = [''] * 4
        idx  = 0
        bytes = 4
        while bytes == 4 and idx < n:
            bytes = min(n - idx, read4(buff))
            for i in xrange(bytes):
                buffer[idx] = buff[i]
                idx += 1
        return idx