class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(set(nums))  
        res = 0
        current = 1  

        for num in nums:
            if num > current:
                count = min(k, num - current)
                res += count * (current + current + count - 1) // 2
                k -= count
                if k == 0:
                    return res
            current = num + 1  

        if k > 0:
            res += k * (current + current + k - 1) // 2

        return res