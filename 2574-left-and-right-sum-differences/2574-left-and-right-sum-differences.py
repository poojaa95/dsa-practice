class Solution(object):
    def leftRightDifference(self, nums):
        n=len(nums)
        l=[]
        k=[]
        ans=[]
        sum=0
        sam=0
        for i in range(n):
            l.append(sum)
            sum+=nums[i]
        for i in range(n-1,-1,-1):
            k.append(sam)
            sam+=nums[i]
        k.reverse()
        for i in range(n):
            ans.append(abs(l[i]-k[i]))
        return ans
        

        