class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i,j in enumerate(nums): 
            if j in dic:
                return [dic[j], i]
            dic[target-j] = i
        