class Solution(object):
    def sortColors(self, nums):
        # l=[]
        # for i in nums:
        #     if i==0:
        #         l.append(i)
        # for j in nums:
        #     if j==1:
        #         l.append(j)
        # for i in nums:
        #     if i == 2:
        #         l.append(i)
        # for i in range(len(l)):
        #     nums[i]=l[i]
        left,mid=0,0
        right=len(nums)-1
        while mid<=right:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
        return nums