class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1 = max(nums)
        nums.remove(max(nums))
        num2 = max(nums)
        return (num1-1)*(num2-1)
        