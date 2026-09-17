class Solution(object):
    def numIdenticalPairs(self, nums):
        x=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j:
                    x+=1
        return x
        