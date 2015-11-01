class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return self.getKth(nums1, nums2, total_len / 2 + 1)
        else:
            return (self.getKth(nums1, nums2, total_len / 2 + 1) + self.getKth(nums1, nums2, total_len / 2)) * 0.5

    def getKth(self, lst1, lst2, k):
        if len(lst1) > len(lst2):
            return self.getKth(lst2, lst1, k)
        if not lst1: # notice the boundary conditions!
            return lst2[k - 1]
        if k == 1:   # notice, which mean whose first one is smallest, use min to find
            return min(lst1[0], lst2[0])
        ptr1 = min(len(lst1), k / 2)
        ptr2 = k - ptr1
        if lst1[ptr1 - 1] > lst2[ptr2 - 1]:
            return self.getKth(lst1, lst2[ptr2:], ptr1)
        else:
            return self.getKth(lst1[ptr1:], lst2, ptr2)
