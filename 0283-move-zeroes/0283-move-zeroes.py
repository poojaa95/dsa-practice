class Solution(object):
    def moveZeroes(self, nums):
        k=[]
        for i in nums[:]:
            if i==0:
                k.append(i)
                nums.remove(i)
        nums=nums.extend(k)
            
        