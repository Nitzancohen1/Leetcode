class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while len(nums1)>m:
            nums1.pop(len(nums1)-1)
        for i in range(n):
            nums1.append(nums2[i])
        return nums1.sort()