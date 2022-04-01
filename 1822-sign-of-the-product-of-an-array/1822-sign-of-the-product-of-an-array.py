class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for num in nums:
            product *= num
        if product>0 : return 1
        if product==0: return 0 
        if product<0: return -1
