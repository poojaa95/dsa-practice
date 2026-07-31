class Solution(object):
    def majorityElement(self, nums):
        fre={}
        for i in nums:
            if i not in fre:
                fre[i]=1
            else:
                fre[i]+=1
        mx = max(fre.values())
        for key in fre:
            if fre[key]==mx:
                return key
        