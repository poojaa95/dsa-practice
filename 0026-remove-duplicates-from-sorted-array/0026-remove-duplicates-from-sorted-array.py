class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        l=[]
        for i in range(n):
            if nums[i] not in l:
                l.append(nums[i])
            for i in range(len(l)):
                nums[i] = l[i]

        return len(l)
        

            

        