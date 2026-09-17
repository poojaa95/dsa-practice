class Solution(object):

    def numIdenticalPairs(self, nums):
        freq = {}
        x = 0

        for i in nums:
            if i in freq:
                x += freq[i]
                freq[i] += 1
            else:
                freq[i] = 1

        return x
        