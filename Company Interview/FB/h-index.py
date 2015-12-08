# Given an array of citations (each citation is a non-negative integer)
# of a researcher, write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia:
# "A scientist has index h if h of his/her N papers have at least h citations each,
# and the other N − h papers have no more than h citations each."

# For example, given citations = [3, 0, 6, 1, 5],
# which means the researcher has 5 papers in total
# and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each
# and the remaining two with no more than 3 citations each, his h-index is 3.

# Note: If there are several possible values for h, the maximum one is taken as the h-index.


class Solution(object):
    def hIndex(self, citations):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        if not citations:
            return 0
        count = [0] * len(citations)
        for citation in citations:
            if citation >= len(citations):
                count[len(citations)] += 1
            else:
                count[citation] += 1
        hIdx = 0
        for i in xrange(len(citations), -1, -1):
            hIdx += count[i]
            if hIdx >= i:
                return i
        return hIdx

class Solution(object):
    def hIndex(self, citations):
        '''
        Time:  O(nlogn)
        Space: O(1)
        '''
        if not citations:
            return 0
        citations = sorted(citations)
        total_citatios = len(citations)
        hIdex = 0
        for i in xrange(len(citations)):
            if total_citatios - i <= citations[i]:
                return total_citatios - i
        return hIdex

class  Solution(object):
    def hIndex(self, citations):
        '''
        Time:  O(logn)
        Space: O(1)
        '''
        total_citations = len(citations)
        start = 0; end = total_citations - 1
        while start < end:
            mid = (start + end) / 2
            if citations[mid] - mid <= citations[mid]:
                end = mid
            else:
                start = mid + 1
        return n - start