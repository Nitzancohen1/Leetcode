class Solution(object):
    def twoSum(self, nums, target):
        dic1 = {}
        for i,j in enumerate(nums): 
            if j in dic1:
                return [dic1[j], i]
            dic1[target-j] = i
        
