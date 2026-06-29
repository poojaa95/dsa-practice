class Solution(object):
    def getConcatenation(self, nums):
        num=[]
        for i in range(len(nums)):
            num.append(nums[i])
        return nums+num