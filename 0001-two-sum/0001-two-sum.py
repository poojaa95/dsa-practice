class Solution(object):
    def twoSum(self, nums, target):
        # sum=0
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return i,j
        sem={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in sem:
                return [sem[rem],i]
            sem[nums[i]]=i

        