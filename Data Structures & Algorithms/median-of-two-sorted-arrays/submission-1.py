class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # brute force is we do merge sort, O((m+n)log(m+n) time)
        # but instead, we have to do via binary search, to reach O(log(m+n)) time

        # wait think about it, this is kind of like merge step (two sorted arrays)
        # now we have to go from there, but to median (middle value) among all elements
        
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

        
        