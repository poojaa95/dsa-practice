class Solution(object):
    def pivotArray(self, nums, pivot):
        less=[]
        great=[]
        equa=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]==pivot:
                equa.append(nums[i])
            else:
                great.append(nums[i])
        return less+equa+great