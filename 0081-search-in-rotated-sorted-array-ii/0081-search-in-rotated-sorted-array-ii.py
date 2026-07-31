class Solution(object):
    def search(self, nums, target):
        for i in nums:
            if target==i:
                return True
        return False
        