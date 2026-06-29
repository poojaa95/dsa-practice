class Solution(object):
    def searchRange(self, nums, target):
        l=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                l.append(i)
        if len(l)==0:
            return [-1,-1]

        return [l[0],l[-1]]
        