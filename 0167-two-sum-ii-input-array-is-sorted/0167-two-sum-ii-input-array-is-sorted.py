class Solution(object):
    def twoSum(self, numbers, target):
        # sem={}
        # for i in range(len(numbers)):
        #     rem=target-numbers[i]
        #     if rem in sem:
        #         return (sem[rem]+1,i+1)
        #     sem[numbers[i]]=i
        left=0
        right=len(numbers)-1
        while left<right:
            sem=numbers[left]+numbers[right]
            if sem==target:
                return (left+1,right+1)
            elif sem>target:
                right-=1
            else:
                left+=1
        