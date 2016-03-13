# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buffer, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buff4 = ['', '', '', '']
        idx   = 0
        curr  = min(n - idx, read4(buff4))
        while True:
            for i in xrange(curr):
                buffer[idx] = buff4[i]
                idx += 1
            if curr != 4 or idx == n:
                return idx