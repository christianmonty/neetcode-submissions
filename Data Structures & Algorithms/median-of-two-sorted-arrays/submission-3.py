class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n: # flip order for smallest is m, so we don't have to later check if n == 0...
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0: # only one left, rest discarded
            return b[b_start + k - 1]
        if k == 1: # two left
            return min(a[a_start], b[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return self.get_kth(nums1, len(nums1), nums2, len(nums2), total // 2 + 1)
        else:
            return (self.get_kth(nums1, len(nums1), nums2, len(nums2), total // 2) + self.get_kth(nums1, len(nums1), nums2, len(nums2), total // 2 + 1)) / 2
        
        # brute force is we do merge sort, O((m+n)log(m+n) time)
        # but instead, we have to do via binary search, to reach O(log(m+n)) time

        # wait think about it, this is kind of like merge step (two sorted arrays)
        # now we have to go from there, but to median (middle value) among all elements

         # must attempt binary search solution as well!!
         # attempted binary search version below

         # implementation below for tricky "binary search" solution copied from solutions
         # so that I can build proper intuition

         
        


        '''
        totlen = len(nums1) + len(nums2)
        even = (totlen) % 2 == 0 # to average medians or not

        # two pointers method (linear scan)
        i = j = 0
        processed = 0
        median1 = median2 = None

        while processed < totlen // 2 + 1:
            median2 = median1
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
                processed += 1
            elif i < len(nums1):
                median1 = nums1[i]
                i += 1
                processed += 1
            elif j < len(nums2):
                median1 = nums2[j]
                j += 1
                processed += 1

        if even:
            return (median1 + median2) / 2
        else:
            return median1
        '''

   

        
        