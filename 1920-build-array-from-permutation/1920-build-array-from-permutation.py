class Solution(object):
    def buildArray(self, nums):
        ans=[]
        for i in range(len(nums)):
            y=nums[nums[i]]
            ans.append(y)
        return ans
        