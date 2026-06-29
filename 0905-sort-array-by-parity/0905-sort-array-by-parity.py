class Solution(object):
    def sortArrayByParity(self, nums):
        l=[]
        ev=[]
        od=[]
        for i in range(len(nums)):
          if nums[i]%2==0:
            ev.append(nums[i])
          else:
            od.append(nums[i])
        l=ev+od
        return l
        