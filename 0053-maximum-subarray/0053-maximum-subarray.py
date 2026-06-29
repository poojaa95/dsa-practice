class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        cur=0
        bes=nums[0]
        for i in range(n):
            cur+=nums[i]
            if cur>bes:
                bes=cur
            if cur<0:
                cur=0
        return bes
        