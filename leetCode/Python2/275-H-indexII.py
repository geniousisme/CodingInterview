class Solution(object):
    def hIndexI(self, citations):
        """
        TC: O(n)
        SC: O(1)
        """
        if not citations:
            return 0
        total_citations = len(citations)
        count           = 0
        for i in xrange(total_citations - 1, -1, -1):
            if total_citations - i > citations[i]:
                break
            else:
                count += 1
        return count

    def hIndex(self, citations):
        '''
        TC: O(logn)
        SC: O(1)
        '''
        if not citations:
            return 0
        total_citations = len(citations)
        start = 0; end = total_citations - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if total_citations - mid > citations[mid]:
                start = mid
            else:
                end   = mid
        if citations[start] + start >= total_citations:
            return total_citations - start
        elif citations[end] + end >= total_citations:
            return total_citations - end
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    citations = [0, 1, 3, 5, 6]
    print s.hIndex(citations)
    citations = [0]
    print s.hIndex(citations)
    citations = [1]
    print s.hIndex(citations)


