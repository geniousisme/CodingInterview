import collections


class Solution(object):
    def minWindow(self, S, T):
        t1_dict = collections.defaultdict(int)
        t2_dict = collections.defaultdict(int)
        for t in T:
            t1_dict[t] += 1
            t2_dict[t] += 1
        count = len(T); start = 0; min_start = 0; min_size = 2147483647
        for end in xrange(len(S)):
            if S[end] in t2_dict and t2_dict[S[end]] > 0:
                t1_dict[S[end]] -= 1
                if t1_dict[S[end]] >= 0:
                    count -= 1
            if count == 0:
                while True:
                    if S[start] in t2_dict and t2_dict[S[start]] > 0:
                        if t1_dict[S[start]] >= 0:
                            break
                        else:
                            t1_dict[S[start]] += 1
                    start += 1
                if min_size > end - start + 1:
                    min_size = end - start + 1
                    min_start = start
        if min_size == 2147483647:
            return ''
        else:
            return S[min_start:min_start + min_size]

if __name__ == "__main__":
    s = Solution()
    print s.minWindow("ADOBECODEBANC", "ABC")