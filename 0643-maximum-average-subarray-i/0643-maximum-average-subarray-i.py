class Solution(object):
    def findMaxAverage(self, nums, k):
        sum=0
        for i in range(k):
            sum+=nums[i]
        maxsum=sum
        i,j=0,k
        while j<len(nums):
            sum-=nums[i]
            i+=1
            sum+=nums[j]
            j+=1
            maxsum=max(maxsum,sum)
        return float(maxsum)/k
        
        