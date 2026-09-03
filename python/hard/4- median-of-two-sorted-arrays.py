class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_array = []
        total_array.extend(nums1)
        total_array.extend(nums2)
        total_array.sort()
        n = len(total_array)
        if n % 2 == 1:
            return float(total_array[n // 2])
        else:
            return (total_array[n // 2 - 1] + total_array[n // 2]) / 2.0