class Solution(object):
    def twoSum(self, nums, target):
        # sum=0
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return i,j
        arr = []

        for i in range(len(nums)):
            arr.append([nums[i], i])

        arr.sort()

        left, right = 0, len(arr)-1

        while left < right:
            if arr[left][0] + arr[right][0] == target:
                return [arr[left][1], arr[right][1]]
            elif arr[left][0] + arr[right][0] > target:
                right -= 1
            else:
                left += 1

        return []