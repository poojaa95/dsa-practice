class Solution(object):
    def removeElement(self, nums, val):
       l=[]
       n=len(nums)
       for i in range(n):
          l.append(nums[i])
          if nums[i]==val:
            l.remove(nums[i])
       for i in range(len(l)):
            nums[i]=l[i]
       return len(l)