class Solution(object):
    def search(self, nums, target):
        # for i in nums:
        #     if target==i:
        #         return True
        # return False
        low=0
        high=len(nums)-1
        if low<=high:
            mid=(low+high)//2
            for i in nums:
                if i==target:
                    return True
                elif i>target:
                    low=mid+1
                else:
                    high=mid-1
        return False
        