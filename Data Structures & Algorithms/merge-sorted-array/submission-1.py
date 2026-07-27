class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # DELETE WHEN ATTEMPT AGAIN...TRICY PROBLEM

        # had to look up algorithm, and implementation for solution here

        # 3 pointers, space optimized. Clever work from back and can reuse space in 1st array

        i, j = m - 1, len(nums2) - 1
        k = len(nums1) - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1





        '''
        # first solution
        # brute force is add to end, then sort! N log N runtime

        i = m
        while i < len(nums1):
            nums1[i] = nums2[i-m]
            i += 1
        # or nums1[m:] = nums2[:n]
        
        nums1.sort()

        # can we do better? This was my hacky attempt but not 2 pointers!!
        '''