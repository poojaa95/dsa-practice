class Solution(object):
    def moveZeroes(self, nums):
        # k=[]
        # for i in nums[:]:
        #     if i==0:
        #         k.append(i)
        #         nums.remove(i)
        # nums=nums.extend(k)
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0

            
        