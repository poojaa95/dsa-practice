class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        fre={}
        for i in range(len(nums)):
            if nums[i] in fre:
                if i - fre[nums[i]] <= k:
                    return True
            fre[nums[i]] = i
        return False
        