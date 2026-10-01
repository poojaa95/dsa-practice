class Solution(object):
    def threeSum(self, nums):
        # l=[]
        # tem=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             sum=nums[i]+nums[j]+nums[k]
        #             if sum==0:
        #                 tem=sorted([nums[i],nums[j],nums[k]])
        #                 if tem not in l:
        #                     l.append(tem)
        # return l
        nums.sort()
        a=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    a.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        return a
        