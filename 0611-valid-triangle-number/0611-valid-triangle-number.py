class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        x=0
        for k in range(len(nums)-1,1,-1):
            i=0
            j=k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    x+=j-i
                    j-=1
                else:
                    i+=1
        return x

        