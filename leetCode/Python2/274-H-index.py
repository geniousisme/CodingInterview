'''
TC: O(nlogn + n) nlogn is for sorting, n is for iterate the List
SC: O(n), create a sorted list there
some good reference: https://github.com/kamyu104/LeetCode/blob/master/Python/h-index.py
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        # can use .sort, but it is not good to change the parameter.
        citations = sorted(citations)
        count     = 0
        total_citations = len(citations)
        for i in xrange(total_citations):
            if total_citations - i <= citations[i]:
                count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    citations = [3, 0, 6, 1, 5]
    print s.hIndex(citations)



