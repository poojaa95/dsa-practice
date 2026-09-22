class Solution(object):
    def removeElement(self, nums, val):
    #    l=[]
    #    n=len(nums)
    #    for i in range(n):
    #       l.append(nums[i])
    #       if nums[i]==val:
    #         l.remove(nums[i])
    #    for i in range(len(l)):
    #         nums[i]=l[i]
    #    return len(l)

        left=0
        right=len(nums)-1
        while left<=right:
           if nums[left]==val:
             nums[left]=nums[right]
             right-=1
           else:
             left+=1
        return left