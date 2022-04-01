class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for num in nums:
            if num == 0:
                return 0
            product *= num
        if product>0: return 1
        if product<0: return -1
