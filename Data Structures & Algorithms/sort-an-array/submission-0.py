class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # mergeSort implementation
        def mergeSort(f: int, e: int) -> List[int]:
            if f == e:
                return [nums[f]]

            mid = (f + e) // 2
            left = mergeSort(f, mid)
            right = mergeSort(mid + 1, e)
            return merge(left, right)

        def merge(l: List[int], r: List[int]) -> List[int]:
            outlist = []
            i = j = 0
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    outlist.append(l[i])
                    i += 1
                else:
                    outlist.append(r[j])
                    j += 1
            while i < len(l):
                outlist.append(l[i])
                i += 1
            while j < len(r):
                outlist.append(r[j])
                j += 1
            return outlist

        return mergeSort(0, len(nums)-1)
        