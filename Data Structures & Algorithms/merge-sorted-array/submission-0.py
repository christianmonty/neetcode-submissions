class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # brute force is add to end, then sort! N log N runtime

        i = m
        while i < len(nums1):
            nums1[i] = nums2[i-m]
            i += 1
        
        nums1.sort()

        # can we do better?