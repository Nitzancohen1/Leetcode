class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(ans)):
            ans.append(nums[i])
        return ans