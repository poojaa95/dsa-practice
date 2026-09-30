class Solution(object):
    def majorityElement(self, nums):
        fre={}
        for i in nums:
            if i not in fre:
                fre[i]=1
            else:
                fre[i]+=1
        ans=[]
        for key in fre:
            if fre[key]>len(nums)//3:
                ans.append(key)
        return ans
        