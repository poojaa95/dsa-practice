class Solution(object):
    def intersection(self, nums1, nums2):
        num1=set(nums1)
        num2=set(nums2)
        x=num1.intersection(num2)
        x=list(x)
        return x
        