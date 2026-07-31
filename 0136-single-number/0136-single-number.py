class Solution(object):
    def singleNumber(self, nums):
        fre={}
        for i in nums:
            if i not in fre:
                fre[i]=1
            else:
                fre[i]+=1
        for key in fre:
            if fre[key]==1:
                return key
        