class Solution(object):
    def maxProduct(self, nums):
        sma=nums[0]
        lar=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            if x<0:
                lar,sma=sma,lar
            lar = max(x, lar * x)
            sma = min(x, sma * x)
            ans = max(ans, lar)
        return ans