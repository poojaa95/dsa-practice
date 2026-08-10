class Solution(object):
    def moveZeroes(self, nums):
        l=[]
        k=[]
        for i in range(len(nums)):
            if nums[i]==0:
                l.append(nums[i])
        for j in range(len(nums)):
            if nums[j]!=0:
                k.append(nums[j])
        k.extend(l)
        for i in range(len(k)):
            nums[i]=k[i]
        return nums
            
        