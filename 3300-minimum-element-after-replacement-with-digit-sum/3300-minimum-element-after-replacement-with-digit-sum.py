class Solution(object):
    def minElement(self, nums):
        n=len(nums)
        for i in range(n):
            x=nums[i]
            sum=0
            while x>0:
                sum+=x%10
                x=x//10
            nums[i]=sum
        return min(nums)

        