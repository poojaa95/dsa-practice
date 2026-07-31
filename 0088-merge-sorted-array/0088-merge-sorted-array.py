class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k=[]
        k.extend(nums1[:m])
        k.extend(nums2[:n])   
        k.sort()
        for i in range(m+n):
            nums1[i]=k[i]
        return k     