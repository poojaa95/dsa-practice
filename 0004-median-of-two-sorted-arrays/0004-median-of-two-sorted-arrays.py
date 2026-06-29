class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1=len(nums1)
        n2=len(nums2)
        x=0
        nums=[]
        for i in range(n1):
             nums.append(nums1[i])
        for j in range(n2):
            nums.append(nums2[j])
        nums=sorted(nums)
        x=len(nums)
        if x%2!=0:
            return nums[x//2]        
        else:
            return (nums[x//2-1]+nums[x//2])/2.0
        