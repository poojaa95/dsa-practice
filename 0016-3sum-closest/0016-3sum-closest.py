class Solution(object):
    def threeSumClosest(self, nums, target):
        # l=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):  
        #             l.append(nums[i]+nums[j]+nums[k])
                    
        # ans=l[0]
        # for i in range(len(l)):
        #     if abs(target-l[i])<abs(target-ans) :
        #         ans=l[i]
        # return ans
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(target - s) < abs(target - closest):
                    closest = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target

        return closest

        